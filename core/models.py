from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

AGE_CHOICES = (
  ('All','All'),
  ('Kids','Kids'),

)

MOVIE_CHOICES=(
    ('seasonal','Seasonal'),
    ('single','Single')
 )
class Profile(models.Model):
    name=models.CharField(max_length=225)
    age_limit=models.CharField(max_length=10,choices=AGE_CHOICES)
    uuid=models.UUIDField(default=uuid.uuid4)

class CustomUser(AbstractUser):
    profiles = models.ManyToManyField(Profile, blank=True)  # Corrected this line

    def __str__(self):
        return self.username



class Movie(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)  # Corrected the typo here
    uuid = models.UUIDField(default=uuid.uuid4)
    type = models.CharField(max_length=10, choices=MOVIE_CHOICES)
    videos = models.ManyToManyField('Video')
    flyer = models.ImageField(upload_to='flyers')
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)

    def __str__(self):
        return self.title

class Video(models.Model):
    title=models.CharField(max_length=225,blank=True,null=True)
    file=models.FileField(upload_to='movies')



