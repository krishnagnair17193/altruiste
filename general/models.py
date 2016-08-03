from __future__ import unicode_literals

from django.db import models

from solo.models import SingletonModel
from geoposition.fields import GeopositionField


class ContactAddress(SingletonModel):
    contact_description = models.TextField()
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='India')
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    location = GeopositionField()

    def __str__(self):
        return '%s, %s' % (self.address_line_1, self.address_line_2)

