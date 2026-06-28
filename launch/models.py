# landing/models.py

from django.db import models


class Waitlist(models.Model):
    # Changed from EmailField to CharField to accept any alphanumeric string
    # max_length is required for CharField
    email = models.CharField(max_length=254, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    # Changed here as well if you want this to accept any text/numbers too
    email = models.CharField(max_length=254)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name