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


class Team(models.Model):
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=150)
    bio = models.TextField()
    photo = models.ImageField(upload_to='team/images', help_text='Size 140x140')
    facebook_link = models.URLField(null=True, blank=True)
    google_link = models.URLField(null=True, blank=True)
    twitter_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Team'


class GalleryImage(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='gallery/images')
    description = models.TextField()

    def __str__(self):
        return self.title
