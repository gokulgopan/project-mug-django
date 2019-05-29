from django import forms
from .models import Update
from . import models

class UpdateForm(forms.Form):
    class meta:
        model = Update
        fields = ['title','body']

form = UpdateForm()