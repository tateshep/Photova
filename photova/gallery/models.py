from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='data/',default='data/no-img.jpg')

    def __str__(self):
        return self.title

class Collection(models.Model):
    title = models.CharField(max_length=50)
    images = models.ManyToManyField(Image,blank=True) #this will be a manytomany relationship with Collection

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


