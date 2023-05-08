from typing import Any, Dict
from django.db.models.query import QuerySet
from django.views.generic import ListView, View
from cryptos.models import Crypto
from .models import Bookmark
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class BookmarkListView(LoginRequiredMixin, ListView):
    template_name = 'bookmarks/bookmarklist.html'
    context_object_name = 'bookmarks'
    
    def get_queryset(self) -> QuerySet[Any]:
        bookmarks = Bookmark.objects.filter(author=self.request.user)
        return bookmarks
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.my_bookmarks = Bookmark.objects.filter(author=self.request.user)
        context['info'] = {
            'total_count':self.my_bookmarks.count()
        }
        return context


class AddBookmarkView(View):
    def post(self, request, slug):
        self.limit = 10
        self.crypto_marked = Crypto.objects.get(slug=slug)
        self.my_bookmarks = Bookmark.objects.filter(author=self.request.user)

        self.my_bookmarks_count = self.my_bookmarks.count()
        self.bookmark_exists = self.my_bookmarks.filter(crypto=self.crypto_marked).exists()
        
        self.previous_path = self.request.META.get('HTTP_REFERER')

        if self.bookmark_exists:
            messages.warning(request, f" '{self.crypto_marked}' bookmark already exist")
            return redirect(self.previous_path)
        if self.my_bookmarks_count >= self.limit:
            messages.warning(request, "bookmark limit reached delete a bookmark")
            return redirect(self.previous_path)
        
        Bookmark.objects.create(
            author = self.request.user,
            crypto = self.crypto_marked
        )
        messages.success(request, f"'{self.crypto_marked}' was bookmarked")
        return redirect(self.previous_path)

class DeleteBookmarkView(View):
    def post(self, request, pk):
        my_bookmarks = Bookmark.objects.filter(author=self.request.user)
        remove_bookmark = my_bookmarks.filter(id=pk)
        remove_bookmark.delete()
        messages.success(request, f"bookmark was removed")
        return redirect('bookmarks:bookmarklist')

