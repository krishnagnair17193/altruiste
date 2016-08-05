from django.shortcuts import render
from django.views.generic import TemplateView


from general.models import ContactAddress
from contacts.forms import ContactUsForm


class HomeView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['contact_address'] = ContactAddress.objects.get()
        context['contact_form'] = ContactUsForm
        return context
