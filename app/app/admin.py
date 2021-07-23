from django.contrib import admin

from app.models import Article, Category, User

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(User)
