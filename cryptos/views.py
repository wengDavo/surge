from typing import Any, Dict
from django.db.models.query import QuerySet
from .models import Crypto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage
from pycoingecko import CoinGeckoAPI
# Create your views here.
cg = CoinGeckoAPI()

class MyPaginator(Paginator):
    def validate_number(self, number):
        try:
            return super().validate_number(number)
        except EmptyPage:
            if int(number) > 1:
                return self.num_pages
            elif int(number) < 1:
                return 1
            else:
                raise
    
class CryptoListView(LoginRequiredMixin,   ListView):
    template_name = 'cryptos/cryptolist.html'
    context_object_name = 'cryptos'
    model = Crypto
    paginate_by = 500
    paginator_class = MyPaginator

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_number_crypto'] = Crypto.objects.count()
        return context

class CryptoDetailView(LoginRequiredMixin, DetailView):
    template_name = 'cryptos/cryptodetail.html'
    context_object_name = 'crypto'
    
    def get_queryset(self):
        slug = self.kwargs.get('slug', None)
        return Crypto.objects.filter(slug=slug)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        detail = cg.get_coins_markets(ids=self.get_object().ids, vs_currency='usd')[0]
        context['detail'] = detail
        return context

class CryptoTrendingView(LoginRequiredMixin, ListView):
    template_name = 'cryptos/cryptotrending.html'
    context_object_name = 'trending_crypto'

    def get_queryset(self) -> QuerySet[Any]:
        search = cg.get_search_trending()
        trending = search['coins']
        return trending

class CryptoSearchView(LoginRequiredMixin, ListView):
    template_name = 'cryptos/searchresults.html'
    context_object_name = 'search_results'
    model = Crypto

    def get_queryset(self):
        self.item = self.request.GET.get('search')
        if self.item == None:
            return 0
        self.search_results = Crypto.objects.filter(name__icontains=self.item)
        return self.search_results

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.search_results.count()
        return context
