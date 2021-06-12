from django.urls import path
from django.views.generic import DetailView

from . import views
from .views import FlashcardsListView, FlashcardDetailView, FlashcardSetListView, FlashcardCreateView, \
                   FlashcardUpdateView, FlashcardDeleteView, CategoryDetailView
from .models import Category

app_name = 'flashcards'

urlpatterns = [
    path('', FlashcardsListView.as_view(), name='flashcards'),
    path('flashcardsets/', FlashcardSetListView.as_view(), name='flashcardsets'),
    path('create/flashcard/', FlashcardCreateView.as_view(), name='create_flashcard'),
    path('flashcard/detail/<int:pk>', FlashcardDetailView.as_view(), name='flashcard_detail'),
    path('flashcard/update/<int:pk>', FlashcardUpdateView.as_view(), name='flashcard_update'),
    path('flashcard/<int:pk>/delete', FlashcardDeleteView.as_view(), name='flashcard_delete'),
    path('category/detail/<int:pk>', CategoryDetailView.as_view(), name='category_detail')

]
