import pytest

from app.models import User


@pytest.mark.django_db
class TestUser:
    def test_can_sign_up(self):
        user = User.objects.create_user(username='test_user', password='testpasswd')
        user_from_db = User.objects.get(id=user.id)
        assert user.id == user_from_db.id

    def test_user_on_sign_up_page(self, client):
        response = client.get('/signup/')
        assert response.template_name[0] == 'user/registration.html'
