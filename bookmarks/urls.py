from django.urls import path
from .views import BookmarkListView, AddBookmarkView, DeleteBookmarkView

app_name = 'bookmarks'

urlpatterns = [
    path('', BookmarkListView.as_view(),name='bookmarklist'),
    path('add/<slug:slug>', AddBookmarkView.as_view(), name='addbookmark'),
    path('reomve/<int:pk>', DeleteBookmarkView.as_view(), name='deletebookmark'),

]