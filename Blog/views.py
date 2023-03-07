from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Article
from .forms import ArticleForm
from django.views.generic import (
CreateView, DetailView, ListView, UpdateView, DeleteView
)

# Create your views here.

# this goes over class based views
class ArticleListView(ListView):
    template_name = 'Blog/article_list.html'
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'Blog/article_detail.html'
    # queryset = Article.objects.filter(id__gt=1) greater than

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

class ArticleCreateView(CreateView):
    template_name = 'Blog/article_create.html'
    form_class = ArticleForm
    # success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    # def get_success_url(self):
        # return '/'

class ArticleUpdateView(UpdateView):
    template_name = 'Blog/article_create.html'
    form_class = ArticleForm

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

    # success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    # def get_success_url(self):
    # return '/'

class ArticleDeleteView(DeleteView):
    template_name = 'Blog/article_delete.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)
    def get_success_url(self):
        return reverse('Blog:article_list')

