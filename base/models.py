from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User

class User(AbstractUser):
  name = models.CharField(max_length=200, null=True)
  email = models.EmailField(unique=True, null=True)
  bio = models.TextField(null=True, blank=True)

  avatar = models.ImageField(null=True, default="avatar.svg")

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []


class Topic(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name  

class Room(models.Model):
  host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
  name = models.CharField(max_length=200)
  description = models.TextField(null=True, blank=True)
  participants = models.ManyToManyField(User, related_name='participants', blank=True)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-updated', '-created']

  def __str__(self):
    return self.name
  
  def descshort(self):
    return self.body[0:50]
  
  def short_description(self):
    if self.description:
      if len(self.description) > 50:
        return f"{self.description[:50]}..."
      else:
        return self.description
    return ''
  

  
class Message(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  room = models.ForeignKey(Room, on_delete=models.CASCADE)
  body = models.TextField()
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-updated', '-created']

  def __str__(self):
    if len(self.body) > 50:
      return f"{self.body[0:50]}..."
    return self.body[0:50]