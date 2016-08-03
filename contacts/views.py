from django.shortcuts import render

from django.views.generic import FormView ,CreateView

from contacts.forms import ContactUsForm


class ContactUsView(CreateView):
    template_name = 'index.html'
    form_class = ContactUsForm
    success_url = '/'

    def form_invalid(self, form):
        return self.render_to_response({'contact_form': form})
