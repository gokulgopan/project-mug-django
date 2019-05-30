from django import forms
from . import models

class CreateUpdate(forms.ModelForm):
    class Meta:
        model = models.Update
        fields = ['title','body']
