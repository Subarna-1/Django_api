from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=255)
    user = User.objects.get(username='Amit1')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Artist(models.Model):
    name = models.CharField(max_length=255)
    works = models.ManyToManyField('Work')

class Work(models.Model):
    LINK_TYPES = (
        ('Y', 'Youtube'),
        ('I', 'Instagram'),
        ('O', 'Other')
    )
    link = models.CharField(max_length=255)
    link_type = models.CharField(max_length=1, choices=LINK_TYPES)


