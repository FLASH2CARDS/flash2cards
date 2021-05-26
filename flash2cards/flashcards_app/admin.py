from django.contrib import admin
from .models import Flashcard, FlashcardSet, Category


admin.site.register(FlashcardSet)
admin.site.register(Category)


class FlashcardsAdmin(admin.ModelAdmin):
    list_display = ('category', 'avers', 'user')
    list_filter = ('category', 'user')

admin.site.register(Flashcard, FlashcardsAdmin)