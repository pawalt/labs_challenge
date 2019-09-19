from django.db import models


class Club(models.Model):
    name = models.TextField()
    description = models.TextField()
    tags = models.ManyToManyField('Tag')


class Tag(models.Model):
    name = models.TextField()
