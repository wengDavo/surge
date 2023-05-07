from django.urls import path
from .views import (
    CryptoListView, CryptoDetailView, CryptoTrendingView, CryptoSearchView,
    # AddBookmarkView
    )

app_name = 'crypto'

urlpatterns = [
    path('all/', CryptoListView.as_view(), name='cryptolist'),
    path('detail/<slug:slug>/', CryptoDetailView.as_view(), name='cryptodetail'),
    path('trending/', CryptoTrendingView.as_view(), name='cryptotrending'),
    path('search/', CryptoSearchView.as_view(), name='cryptosearch'),
]
