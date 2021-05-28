from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import Flashcard, FlashcardSet, Category

User = get_user_model()

admin.site.unregister(Group)


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ['email', 'admin']
    list_filter = ['admin']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password_2')}
         ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()


class FlashcardsAdmin(admin.ModelAdmin):
    list_display = ('category', 'avers', 'user')
    list_filter = ('category', 'user')


admin.site.register(User, UserAdmin)

admin.site.register(FlashcardSet)
admin.site.register(Category)

admin.site.register(Flashcard, FlashcardsAdmin)
