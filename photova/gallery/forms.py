from django import forms
from .models import Image, Collection

class UploadPhotoForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['title','photo']
        widgets = {
            'photo': forms.FileInput(
                attrs={
                    # 'class' : 'file-input',
                    'multiple': True
                }
            )
        }

