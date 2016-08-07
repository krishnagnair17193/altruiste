from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    profile_picture = models.ImageField(upload_to='profiles/images', null=True, blank=True)
    address_line_one = models.CharField(max_length=255, null=True, blank=True)
    address_line_two = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.email
