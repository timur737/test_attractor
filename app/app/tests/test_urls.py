from django.urls import resolve

from app.views import ArticleView, CategoryView


class TestUrls:

    def test_resolution_urls(self):
        resolver = resolve('/article-list')
        assert resolver.func.view_class == ArticleView
        resolver = resolve('/category-list')
        assert resolver.func.view_class == CategoryView
