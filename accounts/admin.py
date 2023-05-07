from django.contrib import admin
from django.contrib.admin import TabularInline
from .models import CustomUser
from bookmarks.models import Bookmark
# Register your models here.

class BookmarkInline(admin.TabularInline):
    model = Bookmark

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    inlines = [BookmarkInline]
