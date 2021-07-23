from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from rest_framework.generics import ListAPIView

from app.models import Article, Category
from app.serializers import ArticleSerializer, CategorySerializer


class IndexView(TemplateView):
    template_name = 'index.html'


class MainView(TemplateView):
    template_name = 'main.html'


# Views for Clients

class ArticleAPI(ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    model = Article


class CategoryAPI(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    model = Category


# Article
@method_decorator(login_required, name='dispatch')
class ArticleView(ListView):
    model = Article
    template_name = 'article/list.html'
    ordering = ['id']


@method_decorator(login_required, name='dispatch')
class ArticleCreate(CreateView):
    model = Article
    template_name = 'article/create.html'
    fields = '__all__'
    success_url = reverse_lazy('article-list')


@method_decorator(login_required, name='dispatch')
class ArticleUpdate(UpdateView):
    model = Article
    template_name = 'article/update.html'
    fields = '__all__'
    context_object_name = 'article'
    success_url = reverse_lazy('article-list')


@method_decorator(login_required, name='dispatch')
class ArticleDelete(DeleteView):
    model = Article
    template_name = 'article/delete.html'
    success_url = reverse_lazy('article-list')


# Category

@method_decorator(login_required, name='dispatch')
class CategoryView(ListView):
    model = Category
    template_name = 'category/list.html'
    ordering = ['id']


@method_decorator(login_required, name='dispatch')
class CategoryCreate(CreateView):
    model = Category
    template_name = 'category/create.html'
    fields = '__all__'
    success_url = reverse_lazy('category-list')


@method_decorator(login_required, name='dispatch')
class CategoryUpdate(UpdateView):
    model = Category
    template_name = 'category/update.html'
    fields = '__all__'
    context_object_name = 'category'
    success_url = reverse_lazy('category-list')


@method_decorator(login_required, name='dispatch')
class CategoryDelete(DeleteView):
    model = Category
    template_name = 'category/delete.html'
    success_url = reverse_lazy('category-list')
