from django.conf.urls import url

from contacts.views import ContactUsView


urlpatterns = [
    url(r'^$', ContactUsView.as_view(), name='contact_us'),
]
