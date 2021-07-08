from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Flashcard, FlashcardSet, Category, CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = (
        (None, {'fields': ('email', 'password', 'nick', 'username')}),
        ('Personal info', {'fields': ('is_active', 'country', 'description', 'staff')}),
        ('Permissions', {'fields': ('admin',)}),
    )
    list_display = ['username', 'email', 'nick', 'description']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'nick', 'username')}
        ),
    )



class FlashcardsAdmin(admin.ModelAdmin):
    list_display = ('category', 'avers', 'user')
    list_filter = ('category', 'user')


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(FlashcardSet)
admin.site.register(Category)

admin.site.register(Flashcard, FlashcardsAdmin)
