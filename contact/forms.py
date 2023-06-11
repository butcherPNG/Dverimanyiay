from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    email = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email", "id": ""}))

    class Meta:
        model = Contact
        fields = ('email',)