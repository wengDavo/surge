from django.db import models
from django.conf import settings
from cryptos.models import Crypto
# Create your models here.
# class Bookmark(models.Model):

class Bookmark(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    crypto = models.ForeignKey(
        Crypto,
        on_delete=models.CASCADE
    )