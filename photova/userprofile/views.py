from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from gallery.models import Collection, Image

class UserListView(generic.ListView):
    model = User
    template_name = 'user_list.html'

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('gallery:gallery')
    template_name = 'signup.html'


