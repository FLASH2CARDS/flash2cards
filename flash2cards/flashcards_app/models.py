from django.db import models
from .categories import CATEGORIES
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from ckeditor.fields import RichTextField


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('you must enter an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_staff_user(self, email, password):

        if not email:
            raise ValueError('you must enter an email address')

        user = self.create_user(
            email,
            password=password
        )

        user.staff = True
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password):

        if not email:
            raise ValueError('you must enter an email address')

        user = self.create_user(
            email,
            password=password
        )

        user.staff = True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser):
    object = UserManager()
    email = models.EmailField(
        verbose_name='your mail adress',  # optional, inform what is a login
        max_length=255,
        unique=True
    )
    name = models.CharField(max_length=255, null=True, blank=True)  # optional, maybe nick or something?
    description = models.TextField(null=True, blank=True, default="write something about yourself")  # optional
    country = models.CharField(max_length=255, null=True, blank=True)  # optional, maybe location or something?
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # something like admin
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the users have a specific permisions?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permisions to viev the app 'app_label'?"
        return True

    @property
    def is_staff(self):
        "Does the user is staff?"
        return self.staff

    @property
    def is_admin(self):
        "Does the user is admin?"
        return self.admin


class Category(models.Model):
    """Category class for setting main Category of flashcard or flashcards set.
    Attribute:
        1. category_name (CharField) Takes in main category name.
    """
    category_name = models.CharField(max_length=20, choices=CATEGORIES, default="Language")

    def __str__(self):
        return f"{self.category_name}"

    class Meta:
        ordering = ['category_name']
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class SubCategory(models.Model):
    """Subcategory class for setting main subcategory of flashcard or flashcards set.  Subcategories are defined
    separately within each main category.
    Attribute:
        1. category (ForeignKey to Category model) The field has a relationship of many (subctagories) to one (category).
        2. subcategory_name (CharField) Takes in subcategory name.
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=20, choices=CATEGORIES, default="Language")

    # TODO: SUBCATEGORIES choices

    def __str__(self):
        return f"{self.subcategory_name}"

    class Meta:
        ordering = ['subcategory_name']
        verbose_name = "Sub-Category"
        verbose_name_plural = "Sub-Categories"


class Flashcard(models.Model):
    """Flashcard class to create a single flashcard.
    Attributes:
        1. avers (RichTextField) Takes in avers content. Required.
        2. revers (RichTextField) Takes in revers content.Required.
        3. user (ForeignKey to User model) The field has a relationship of many (flashcards) to one (user).
        4. category (ForeignKey to Category model) The field has a relationship of many (flashcards) to one (category).
        5. subctegory (ForeignKey to SubCategory model) The field has a relationship of many (flashcards) to one (subcategory).
        6. creation_date (DateTimeField) Takes in the date and time for flashcard creation (completing automatically).
        7. modification_date (DateTimeField) Takes in the date and time for flashcard update (completing automatically).
    """
    avers = RichTextField(blank=False, unique=True)
    revers = RichTextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.avers}"

    class Meta:
        ordering = ['modification_date', 'category']


class FlashcardSet(models.Model):
    """FlashcardSet class to create a single set of several flashcard.
    Attributes:
        1. set_name (TextField) Takes in avers content. Required.
        2. is_private (BooleanField) The field to mark if set could be visible for others users  (Default: Public).
        3. user (ManyToManyField to User model) The field has a relationship of many (flashcards sets) to many (users).
        4. flashcard (ManyToManyField to Flashcard model) The field has a relationship of many (flashcards sets) to many (flashcards).
        5. category (ForeignKey to Category model) The field has a relationship of many (flashcard sets) to one (category).
        6. subctegory (ForeignKey to SubCategory model) The field has a relationship of many (flashcards sets) to one (subcategory).
        7. creation_date (DateTimeField) Takes in the date and time for flashcard creation (completing automatically).
        8. modification_date (DateTimeField) Takes in the date and time for flashcard update (completing automatically).
    """
    set_name = models.TextField(max_length=45, blank=False)
    is_private = models.BooleanField(verbose_name="Private ?", default=False)
    user = models.ManyToManyField(User)
    flashcard = models.ManyToManyField(Flashcard)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.set_name}"

    class Meta:
        ordering = ['modification_date']


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
    user = models.ManyToManyField(User)
    comment_body = RichTextField(blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} commented on {self.creation_date}"

    class Meta:
        ordering = ['creation_date']
