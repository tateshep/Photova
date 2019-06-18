from django.db import models
from django.urls import reverse


class Image(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='data/')

    def __str__ (self):
        return self.title

    def get_absolute_url (self):
        return reverse('gallery:gallery')


class Collection(models.Model):
    title = models.CharField(max_length=50)
    images = models.ManyToManyField(Image,blank=True) # manytomany relationship with Collection
    description = models.TextField(blank=True)
    showcase_gallery = models.BooleanField(default=False)
    permitted_users = models.ManyToManyField('auth.User',blank=True)
    
    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url (self):
        return reverse('gallery:collection_detail', args=[str(self.id)])

