from cryptos.models import Crypto
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

all_crypto_list = cg.get_coins_list()

def run():
    for crypto in all_crypto_list:
        new_crypto = Crypto(ids=crypto['id'], symbol=crypto['symbol'], name=crypto['name'])
        new_crypto.save()
        print("--loaded:",new_crypto)

if __name__ == '__main__':
    run()

