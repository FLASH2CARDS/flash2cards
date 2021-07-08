from django.urls import path
from django.views.generic import DetailView

from .views import FlashcardsListView, FlashcardDetailView, FlashcardSetListView, FlashcardCreateView, \
    FlashcardUpdateView, FlashcardDeleteView, CategoryDetailView, SetCategoryDetailView, FlashcardSetDetailView, \
    IndexPageView

app_name = 'flashcards'

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('flashcards_list/', FlashcardsListView.as_view(), name='flashcards_list'),
    path('create/flashcard/', FlashcardCreateView.as_view(), name='create_flashcard'),
    path('flashcard/<int:pk>', FlashcardDetailView.as_view(), name='flashcard_detail'),
    path('flashcard/update/<int:pk>', FlashcardUpdateView.as_view(), name='flashcard_update'),
    path('flashcard/<int:pk>/delete', FlashcardDeleteView.as_view(), name='flashcard_delete'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
    path('set/category/<int:pk>', SetCategoryDetailView.as_view(), name='set_category_detail'),
    path('flashcardsets/', FlashcardSetListView.as_view(), name='flashcardsets'),
    path('flashcardset/<int:pk>', FlashcardSetDetailView.as_view(), name='flashcardset_detail')

]
