from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from gallery.models import Image

def homeView(request):
    images = Image.objects.order_by('title')
    context = {
        'images': images,
    }
    return render(request,'index.html',context)
