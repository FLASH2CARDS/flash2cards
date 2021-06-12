from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Flashcard, CustomUser

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'nick', 'description')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'nick', 'description')


class SignupForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'nick']

    def save(self, user):
        user.save()


class FlashcardCreateForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ('avers', 'revers', 'category', 'user')

        widgets = {
            'avers': forms.Textarea(attrs={'class': 'form-control', 'rows': '4',
                                           'placeholder': 'Avers fiszki (słowo, defnicja, pytanie, etc.'}),
            'revers': forms.Textarea(
                attrs={'class': 'form-control', 'rows': '4', 'placeholder': 'Treść odpowiadająca na avers fiszki'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'})
        }
