from django import forms
from .models import ImageUploadModel

class SimpleUploadForm(forms.Form):
    title = forms.CharField(max_length=50)
    # file = forms.FileField < File을 받아오려고 할때!
    image = forms.ImageField()

class ImageUploadForm(forms.ModelForm):

    class Meta:
        model = ImageUploadModel

        fields = ('description', 'document',)
