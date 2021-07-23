import pytest

from app.models import User


@pytest.mark.django_db
class TestView:
    def test_view_redirect(self, client):
        url = '/article-create'
        response = client.get(url)
        assert response.url == f'/accounts/login/?next={url}'  # redirected to login
        response = client.post(url)
        assert response.status_code == 302

    def test_view_with_user(self, client):
        client.force_login(User.objects.create(username='testuser', password='testpassuser'))
        response = client.get('/category-list')
        assert response.status_code == 200
