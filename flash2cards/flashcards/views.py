from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from .models import Flashcard, FlashcardSet, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .forms import FlashcardCreateForm


class IndexPageView(TemplateView):
    template_name = 'flashcards/index.html'


class FlashcardsListView(ListView):
    model = Flashcard
    template_name = 'flashcards/flashcard_list.html'
    context_object_name = 'flashcards'
    paginate_by = 10

    # posts = Flashcard.objects.all().order_by('-modification_date')
    # @property
    # def flashcards_for_frontpage(self):
    #     return self.flashcards.order_by('-date_posted')[:5]


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


def ten_fcards(request):
    # get the blog posts that are published
    posts = Flashcard.objects.all().order_by('-modification_date')
    # now return the rendered template
    return render(request, 'blog/about.html', {'post': posts})
