from django.db.models.signals import pre_save
from django.utils.text import slugify
from .models import Crypto

def slugify_ids(sender, instance, **kwargs):
    if instance.slug is None:
        instance.slug = slugify(instance.ids)

pre_save.connect(slugify_ids, sender=Crypto)