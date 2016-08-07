from django.forms import ModelForm

from contacts.models import ContactRequest


class ContactUsForm(ModelForm):

    class Meta:
        model = ContactRequest
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactUsForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['message'].widget.attrs['placeholder'] = 'Message'
