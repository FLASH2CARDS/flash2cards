from django.db import models
from .categories import CATEGORIES
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=20, choices=CATEGORIES, default="Language")

    def __str__(self):
        return f"{self.category_name}"

    class Meta:
        ordering = ['category_name']
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Flashcard(models.Model):
    avers = models.TextField(blank=False, unique=True)
    revers = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.avers} | {self.category}"

    class Meta:
        ordering = ['modification_date', 'category']


class FlashcardSet(models.Model):
    set_name = models.TextField(max_length=45, blank=False)
    user = models.ManyToManyField(User)
    flashcard = models.ManyToManyField(Flashcard)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    is_private = models.BooleanField(verbose_name="Private ?", default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.set_name} | {self.category}"

    class Meta:
        ordering = ['modification_date']
