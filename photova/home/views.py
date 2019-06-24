from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User

from gallery.models import Image, Collection
from blog.models import BlogPost

def homeView(request):
    return render(request,'index.html', {})

def adminView(request):
    image_list = Image.objects.order_by('title')
    collection_list = Collection.objects.order_by('title')
    blogpost_list = BlogPost.objects.order_by('created')
    user_list = User.objects.order_by('username')
    context = {
        'image_list': image_list,
        'collection_list': collection_list,
        'blogpost_list': blogpost_list,
        'user_list': user_list,
    }
    return render(request,'admin_view.html', context)
