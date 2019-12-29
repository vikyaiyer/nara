from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Account(models.Model):
    title = models.CharField(max_length=500, unique=True)
    address = models.TextField()
