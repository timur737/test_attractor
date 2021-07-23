from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from app.models import User
from users.forms import UserRegisterForm


# Auth

class SignUpView(CreateView):
    template_name = 'user/registration.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm


# User CRUD from Admin

@method_decorator(login_required, name='dispatch')
class UserList(ListView):
    model = User
    template_name = 'user/list.html'


@method_decorator(login_required, name='dispatch')
class UserCreate(CreateView):
    model = User
    template_name = 'user/create.html'
    fields = ('username', 'password')
    success_url = reverse_lazy('user-list')


@method_decorator(login_required, name='dispatch')
class UserUpdate(UpdateView):
    model = User
    template_name = 'user/update.html'
    fields = ('username', 'password')
    context_object_name = 'user'
    success_url = reverse_lazy('user-list')


@method_decorator(login_required, name='dispatch')
class UserDelete(DeleteView):
    model = User
    template_name = 'user/delete.html'
    success_url = reverse_lazy('user-list')
