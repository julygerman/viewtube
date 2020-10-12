from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from embed_video.fields import EmbedVideoField
from django.contrib.auth import get_user_model

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length= 100, unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.CharField(max_length=200)
    videos = models.ManyToManyField('Video')

class Video(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    url = EmbedVideoField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'video_id': self.id})
