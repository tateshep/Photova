from django import forms
from .models import Image

class UploadPhotoForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['title','photo','author']