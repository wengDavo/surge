from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(unique=True, blank=False, null=False, max_length=100)

    def __str__(self):
        return self.username
