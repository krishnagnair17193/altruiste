from django.shortcuts import render

from django.views.generic import FormView ,CreateView

from contacts.forms import ContactUsForm
from general.mixins import AjaxableResponseMixin


class ContactUsView(AjaxableResponseMixin, CreateView):
    form_class = ContactUsForm
