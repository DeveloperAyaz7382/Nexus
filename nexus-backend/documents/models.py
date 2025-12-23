from django.db import models

# Create your models here.
from django.db import models
from users.models import User

class Document(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    file = models.FileField(upload_to='docs/')
    status = models.CharField(
        choices=[('Draft','Draft'),('Reviewed','Reviewed'),('Signed','Signed')],
        max_length=20
    )
