from django.contrib.auth.models import AbstractUser
from django.db import models

class Joke(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    datetime = models.DateTimeField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('USER', 'User'),
    )

    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default='USER')

    def __str__(self):
        return self.username





