from django.db import models
from django.urls import reverse
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    description = models.CharField(max_length=1000, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    # notice the absence of a "Password field", that is built in.

    object = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin


class Category(MPTTModel):
    """Category class for setting main Category and subcategory of flashcard or flashcards set.
    Attribute:
        1. category_name (CharField) With MPTT library takes names for main categories and subcategories(as children).
    """
    category_id = models.AutoField(primary_key=True, unique=True, editable=False, null=False)
    category_name = models.CharField(max_length=50, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.category_name

    class MPTTMeta:
        order_insertion_by = ['category_name']
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Flashcard(models.Model):
    """Flashcard class to create a single flashcard.
    Attributes:
        1. avers (RichTextField) Takes in avers content. Required.
        2. revers (RichTextField) Takes in revers content.Required.
        3. user (ForeignKey to User model) The field has a relationship of many (flashcards) to one (user).
        4. category (ForeignKey to Category model) The field has a relationship of many (flashcards) to one (category).
        5. creation_date (DateTimeField) Takes in the date and time for flashcard creation (completing automatically).
        6. modification_date (DateTimeField) Takes in the date and time for flashcard update (completing automatically).
    """
    avers = models.TextField(max_length=500, blank=True, null=True, unique=True)
    revers = models.TextField(max_length=500, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.avers}"

    def get_absolute_url(self):
        return reverse('flashcards:flashcards')

    class Meta:
        ordering = ['-modification_date']

    @property
    def flashcards_for_frontpage(self):
        return self.avers.order_by('-modification_date')[:5]


class FlashcardSet(models.Model):
    """FlashcardSet class to create a single set of several flashcard.
    Attributes:
        1. set_name (TextField) Takes in avers content. Required.
        2. is_private (BooleanField) The field to mark if set could be visible for others users  (Default: Public).
        3. user (ManyToManyField to User model) The field has a relationship of many (flashcards sets) to many (users).
        4. flashcard (ManyToManyField to Flashcard model) The field has a relationship of many (flashcards sets) to many (flashcards).
        5. category (ForeignKey to Category model) The field has a relationship of many (flashcard sets) to one (category).
        6. creation_date (DateTimeField) Takes in the date and time for flashcard creation (completing automatically).
        7. modification_date (DateTimeField) Takes in the date and time for flashcard update (completing automatically).
    """
    set_name = models.TextField(max_length=45, blank=False)
    is_private = models.BooleanField(verbose_name="Private ?", default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    flashcard = models.ManyToManyField(Flashcard)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.set_name}"

    class Meta:
        ordering = ['-modification_date']


class Comment(models.Model):
    """Comment class for taking in comments per flashcard.
    Attributes:
        1. flashcard (ForeignKey to Flashcard model) The field has a relationship of many (comments) to one (flashcard).
        1. flashcardset (ForeignKey to FlashcardSet model) The field has a relationship of many (comments) to one (flashcardset).
        2. user (ManyToManyField to User model) The field has a relationship of many (flashcards sets) to many (users).
        3. comment_body (RichTextField) Takes in comment text. Required.
        4. creation_date (DateTimeField) Takes in the date and time for flashcard creation (completing automatically).
    """
    flashcard = models.ForeignKey(Flashcard, on_delete=models.SET_NULL, null=True)
    flashcardset = models.ForeignKey(FlashcardSet, on_delete=models.SET_NULL, null=True)
    user = models.ManyToManyField(CustomUser)
    comment_body = models.TextField(blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} commented on {self.creation_date}"

    class Meta:
        ordering = ['creation_date']
