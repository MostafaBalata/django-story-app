from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Upload(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True, max_length=255)
    modified_datetime = models.DateTimeField(default=timezone.now, null=True, blank=True)


class Story(models.Model):
    user = models.ForeignKey(User, null=False)
    upload = models.ForeignKey(Upload, null=True)
    note = models.CharField(max_length=5000, null=True)
    location = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=40, null=False, default="story")

    status = models.IntegerField(default=1)
    create_datetime = models.DateTimeField(default=timezone.now, null=True, blank=True)
    modified_datetime = models.DateTimeField(default=timezone.now, null=True, blank=True)
