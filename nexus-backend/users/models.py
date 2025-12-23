from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=[('investor','Investor'),('entrepreneur','Entrepreneur')]
    )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    portfolio = models.URLField(blank=True)
    preferences = models.JSONField(default=dict)
