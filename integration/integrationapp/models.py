from distutils.command.upload import upload
from django.db import models

# Create your models here.

class info(models.Model):

    name=models.CharField(max_length=20)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    price=models.IntegerField
    offer=models.BooleanField(default=False)
    