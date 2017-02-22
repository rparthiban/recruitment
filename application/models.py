from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Application(models.Model):
    """
    Need fields to be defined for the this table with their attributes.
    """

    email = models.EmailField("Email", max_length=254, blank=False)
    first_name = models.CharField("First Name", max_length=32, blank=False)
    last_name = models.CharField("Last Name", max_length=32, blank=True)
    address = models.TextField("Address", blank=True)
    current_company = models.CharField("Current Company", max_length=100, blank=True)
    skills = models.TextField("Skills", blank=False)
    submitted = models.DateField(db_index=True, auto_now_add=True)
    active = models.BooleanField(default=True)
    accepted = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s' % self.email

    class Meta:
        ordering = ['-submitted']
