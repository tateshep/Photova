from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Image, Collection
from .forms import UploadPhotoForm

class HomeView(ListView):
    model = Collection
    template_name = 'gallery.html'
    # print(Collection.images_set.all())

    # not actually sure if this is necessary
    def get_queryset(self):
        return Collection.objects.all()


# def upload_image(request):
#     if request.method == 'POST':
#         form = UploadPhotoForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])

class NewImage(CreateView):
    model = Image
    # form_class = UploadPhotoForm
    template_name = 'image_new.html'
    fields = ['title','photo','author']

    success_url = reverse_lazy('gallery:gallery')


        #add this for user authentication
    # def form_valid(self,form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)
