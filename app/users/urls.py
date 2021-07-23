from django.urls import path

from users.views import UserList, UserCreate, UserUpdate, UserDelete, SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('user-list', UserList.as_view(), name='user-list'),
    path('user-create', UserCreate.as_view(), name='user-create'),
    path('user/<int:pk>/update', UserUpdate.as_view(), name='user-update'),
    path('user/<int:pk>/delete', UserDelete.as_view(), name='user-delete'),
]
