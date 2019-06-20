from django.db import models
from django.urls import reverse
from datetime import timedelta

from gallery.models import Image

class BlogPost(models.Model):
    title = models.CharField(max_length=40)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    images = models.ManyToManyField(Image,blank=True)
    thumbnail_image= models.ForeignKey(Image,related_name="thumbnails", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

