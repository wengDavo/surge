from django.db import models
# Create your models here.

class Crypto(models.Model):
    slug = models.SlugField(blank=True, null=True, max_length=500)
    ids = models.CharField(max_length=500)
    symbol = models.CharField(max_length=500)
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.ids
    
    class Meta:
        ordering = ['id']


