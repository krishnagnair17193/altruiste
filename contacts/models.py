from __future__ import unicode_literals

from django.db import models


class ContactRequest(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subscribed_newsletter = models.BooleanField(default=True)
    message = models.TextField()

    def __str__(self):
        return self.name
