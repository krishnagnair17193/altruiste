from django.forms import ModelForm

from contacts.models import ContactRequest


class ContactUsForm(ModelForm):

    class Meta:
        model = ContactRequest
        fields = '__all__'
