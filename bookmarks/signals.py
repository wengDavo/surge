from django.db.models.signals import pre_save
from bookmarks.models import Bookmark

# def check_bookmark(sender, instance, **kwargs):
#     limit = 10
#     if instance.author is None:
#         return
#     if Bookmark.objects.count() >= limit:
#         Bookmark.objects.get(crypto=instance.slug)
#         print("count me",Bookmark.objects.count())
#         raise Exception

#     # Bookmark.objects.create(
#     #     user = instance.user,
#     #     crypto = instance.crypto
#     # )
    

# pre_save.connect(check_bookmark, sender=Bookmark)