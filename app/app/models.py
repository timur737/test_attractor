from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=256, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='image_for_articles', null=True, blank=True)
