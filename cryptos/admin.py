from django.contrib import admin
from .models import Crypto

# Register your models here.
@admin.register(Crypto)
class CryptoAdmin(admin.ModelAdmin):
    list_display = ('ids','slug','symbol','name')
