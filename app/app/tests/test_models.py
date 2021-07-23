import pytest
from django.core.files.uploadedfile import SimpleUploadedFile

from app.models import Article, Category


@pytest.mark.django_db
class TestSimple:
    def test_add_article(self):
        data = {
            'title': 'Test',
            'description': 'testing',
        }
        img = SimpleUploadedFile('test_image',
                                 content=open(
                                     '/home/timur/test_attractor_junior/app/app/tests/media_for_test/fl-shape-1.png',
                                     'rb').read(), content_type='image/png')
        article = Article.objects.create(title=data['title'], description=data['description'], image=img)
        assert article.title == data['title']

    def test_parent_category(self):
        data = {
            'category1': {
                'title': 'test_category1',
                'parent_id': None
            },
            'category2': {
                'title': 'test_category2',
            },
        }
        category1 = Category.objects.create(title=data['category1']['title'],
                                            parent_id=data['category1']['parent_id'])
        category2 = Category.objects.create(title=data['category2']['title'],
                                            parent_id=category1.id)
        assert category2.parent_id == category1.id
