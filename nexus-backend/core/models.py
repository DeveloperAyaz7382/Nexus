from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    INVESTOR = 'investor'
    ENTREPRENEUR = 'entrepreneur'

    ROLE_CHOICES = [
        (INVESTOR, 'Investor'),
        (ENTREPRENEUR, 'Entrepreneur'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True)
    portfolio_url = models.URLField(blank=True)
    preferences = models.JSONField(default=dict)

    def __str__(self):
        return self.user.username
