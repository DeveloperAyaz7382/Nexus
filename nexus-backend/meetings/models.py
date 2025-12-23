from django.db import models

# Create your models here.
from django.db import models
from users.models import User

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField()
    participants = models.ManyToManyField(User)
    status = models.CharField(max_length=20)
