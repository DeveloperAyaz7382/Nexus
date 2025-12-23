from django.db import models

# Create your models here.
from django.db import models
from users.models import User

class Transaction(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sent')
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='received')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
