from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
# from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey


class CustomUser(AbstractUser):
    email = models.EmailField(
        verbose_name='your mail adress',  # optional, inform what is a login
        max_length=255,
        unique=True)

    username = models.CharField(max_length=255, null=True, blank=True)
    nick = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True, default="write something about yourself")  # optional
    country = models.CharField(max_length=255, null=True, blank=True)  # optional, maybe location or something?
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # something like admin
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nick', 'username']

    def __str__(self):
        return self.nick


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
