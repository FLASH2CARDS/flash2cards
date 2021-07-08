from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from .models import Flashcard, FlashcardSet, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .forms import FlashcardCreateForm


class FlashcardsListView(ListView):
    model = Flashcard
    template_name = 'flashcards/flashcard_list.html'
    context_object_name = 'flashcards'
    paginate_by = 10


def index_multi_sections(request):
    cards = Flashcard.objects.all()
    sets = FlashcardSet.objects.all()
    fcards = Flashcard.objects.all().order_by('-modification_date')[:7]
    fsets = FlashcardSet.objects.all().order_by('-modification_date')[:7]
    context = {'flashcards': fcards, "flashcardsets": fsets, "cards_count": cards.count(), "sets_count": sets.count()}
    return render(request, "flashcards/index.html", context)


class FlashcardSetListView(ListView):
    model = FlashcardSet
    template_name = 'flashcards/flashcardset_list.html'
    context_object_name = 'flashcardsets'
    paginate_by = 10


class FlashcardDetailView(DetailView):
    model = Flashcard
    template_name = 'flashcards/flashcard_detail.html'


class FlashcardSetDetailView(DetailView):
    model = FlashcardSet
    template_name = 'flashcards/flashcardset_detail.html'


class FlashcardCreateView(CreateView):
    model = Flashcard
    form_class = FlashcardCreateForm
    template_name = 'flashcards/flashcard_form.html'


class FlashcardSetCreateView(CreateView):
    pass


class FlashcardUpdateView(UpdateView):
    model = Flashcard
    template_name = 'flashcards/flashcard_update.html'
    fields = ['avers', 'revers', 'category']


class FlashcardSetUpdateView(UpdateView):
    pass


class FlashcardDeleteView(DeleteView):
    model = Flashcard
    template_name = 'flashcards/flashcard_delete.html'
    success_url = reverse_lazy('flashcards:flashcards')


class FlashcardSetDeleteView(DeleteView):
    pass


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'flashcards/category_detail.html'


class SetCategoryDetailView(DetailView):
    model = Category
    template_name = 'flashcards/flashcardset_category.html'
