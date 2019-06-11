from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Image, Collection

class HomeView(ListView):
    model = Collection
    template_name = 'gallery.html'
    # print(Collection.images_set.all())

    def get_queryset(self):
        return Collection.objects.all()