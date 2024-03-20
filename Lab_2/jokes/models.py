from django.db import models


class Joke(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    datetime = models.DateTimeField()

    def __str__(self):
        return self.name


from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom User model extending Django's built-in AbstractUser class.
    Adds a username field with a maximum length of 20 characters.
    """
    username = models.CharField(max_length=20, unique=True)

    def __str__(self):
        """
        Returns the user's username as the string representation of the object.
        """
        return self.username
