from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from app.views import IndexView, ArticleView, ArticleCreate, ArticleUpdate, \
    ArticleDelete, CategoryView, CategoryCreate, \
    CategoryUpdate, CategoryDelete, ArticleAPI, CategoryAPI, MainView

urlpatterns = [
                  path('', IndexView.as_view(), name='index'),
                  path('admin/', MainView.as_view(), name='main'),
                  path('articles', ArticleAPI.as_view(), name='articles'),
                  path('categories', CategoryAPI.as_view(), name='categories'),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('article-list', ArticleView.as_view(), name='article-list'),
                  path('article-create', ArticleCreate.as_view(), name='article-create'),
                  path('article/<int:pk>/update', ArticleUpdate.as_view(), name='article-update'),
                  path('article/<int:pk>/delete', ArticleDelete.as_view(), name='article-delete'),
                  path('category-list', CategoryView.as_view(), name='category-list'),
                  path('category-create', CategoryCreate.as_view(), name='category-create'),
                  path('category/<int:pk>/update', CategoryUpdate.as_view(), name='category-update'),
                  path('category/<int:pk>/delete', CategoryDelete.as_view(), name='category-delete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
