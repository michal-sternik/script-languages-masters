from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('USER', 'User'),
    )

    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default='USER')

    def __str__(self):
        return self.username

class Joke(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    datetime = models.DateTimeField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class ReviewRating(models.Model):
    joke = models.ForeignKey(Joke, on_delete=models.CASCADE)
    review = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.review



