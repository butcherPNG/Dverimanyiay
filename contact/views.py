from django.shortcuts import render
from django.views.generic import CreateView

from .models import *
from .forms import *
from .service import send

class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = "/"
    template_name = 'contact/tags/form.html'

    def form_valid(self, form):
        form.save()
        send(form.instance.email)

        return super().form_valid(form)