from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.TextField()
    user_name = models.TextField()
    clubs = models.ManyToManyField('Club', blank=True)


class Club(models.Model):
    name = models.TextField()
    description = models.TextField()
    tags = models.ManyToManyField('Tag')


class Tag(models.Model):
    name = models.TextField()
