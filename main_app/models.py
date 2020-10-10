from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from embed_video.fields import EmbedVideoField

# Create your models here.

class Video(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    url = EmbedVideoField()
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'video_id': self.id})

class User(AbstractUser):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.CharField(max_length=200)
    videos = models.ManyToManyField(Video)