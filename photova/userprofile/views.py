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

class MyCollections (generic.ListView):
    model = Collection
    template_name = 'userprofile_collections.html'
    # print(auth.User)
    # print (Collection.permitted_users)

    def get_queryset(self):
        return self.request.user.collection_set.all()
        
        # filter(permitted_users= 'auth.User' )
