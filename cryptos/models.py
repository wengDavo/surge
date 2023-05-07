from django.db import models
# Create your models here.

class Crypto(models.Model):
    slug = models.SlugField(blank=True, null=True)
    ids = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.ids
    
    class Meta:
        ordering = ['id']


