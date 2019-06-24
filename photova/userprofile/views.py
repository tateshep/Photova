
from django.conf import settings
from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from gallery.models import Collection, Image
from .forms import UserCreationFormEmail

class UserListView(generic.ListView):
    model = User
    template_name = 'user_list.html'

class SignUpView(generic.CreateView):
    form_class = UserCreationFormEmail
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class MyCollections (generic.ListView):
    model = Collection
    template_name = 'userprofile_collections.html'

    def get_queryset(self):
        return self.request.user.collection_set.all()

class DownloadPhotoView(generic.DetailView):
    # Download photos functionality, get the pk, from selection
    # Uses pk to respond with file attachement titled by image title
    def get(self, request, *args, **kwargs):
        image_pk = self.kwargs.get('pk',None)
        if image_pk is None:
            raise ValueError ("Found empty image_pk")
        my_file = Image.objects.get(id=image_pk)
        my_filename = my_file.title + '.jpg'
        response = FileResponse(my_file.photo, as_attachment=True, filename=my_filename)
        return response