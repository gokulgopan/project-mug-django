from django import forms

class FormName(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
