from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Flashcard, CustomUser

User = get_user_model()


class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, help_text='Required. 100 characters or fewer.')

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('full_name', 'age',)


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

