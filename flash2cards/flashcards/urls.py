from django.urls import path
from django.views.generic import DetailView
from .views import *
from . import views

app_name = 'flashcards'

urlpatterns = [
    path('', views.index_multi_sections, name='index'),
    path('flashcards_list/', FlashcardsListView.as_view(), name='flashcards'),
    path('create/flashcard/', FlashcardCreateView.as_view(), name='create_flashcard'),
    path('flashcard/<int:pk>', FlashcardDetailView.as_view(), name='flashcard_detail'),
    path('flashcard/update/<int:pk>', FlashcardUpdateView.as_view(), name='flashcard_update'),
    path('flashcard/<int:pk>/delete', FlashcardDeleteView.as_view(), name='flashcard_delete'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
    path('set/category/<int:pk>', SetCategoryDetailView.as_view(), name='set_category_detail'),
    path('flashcardsets_list/', FlashcardSetListView.as_view(), name='flashcardsets_list'),
    path('flashcardset/<int:pk>', FlashcardSetDetailView.as_view(), name='flashcardset_detail'),
    path('search_results/', views.search_results, name='search_results')

]
