from django.db import models
from .categories import CATEGORIES
from django.contrib.auth.models import (
BaseUserManager, AbstractBaseUser
)

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
        verbose_name='your mail adress',#optional, inform what is a login
        max_length=255,
        unique=True
    )
    name = models.CharField(max_length=255, null=True, blank=True) #optional, maybe nick or something?
    description = models.TextField(null=True, blank=True, default="write something about yourself") #optional
    country = models.CharField(max_length=255, null=True, blank=True) #optional, maybe location or something?
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # something like admin
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
    category_name = models.CharField(max_length=20, choices=CATEGORIES, default="Language")

    def __str__(self):
        return f"{self.category_name}"

    class Meta:
        ordering = ['category_name']
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=20, choices=CATEGORIES, default="Language")

    def __str__(self):
        return f"{self.subcategory_name}"

    class Meta:
        ordering = ['subcategory_name']
        verbose_name = "Sub-Category"
        verbose_name_plural = "Sub-Categories"


class Flashcard(models.Model):
    avers = models.TextField(blank=False, unique=True)
    revers = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.avers}"

    class Meta:
        ordering = ['modification_date', 'category']


class FlashcardSet(models.Model):
    set_name = models.TextField(max_length=45, blank=False)
    user = models.ManyToManyField(User)
    flashcard = models.ManyToManyField(Flashcard)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    is_private = models.BooleanField(verbose_name="Private ?", default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.set_name}"

    class Meta:
        ordering = ['modification_date']


