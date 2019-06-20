from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import BlogPost

class HomeView(ListView):
    model = BlogPost
    template_name = 'blog_index.html'

    def get_queryset(self):
        return BlogPost.objects.all().order_by('-created')

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_detail.html'