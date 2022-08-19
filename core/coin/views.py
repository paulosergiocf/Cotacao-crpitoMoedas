from django.http import HttpResponse
from django.shortcuts import render
from .models import Cotacoes
from coin.Api.criptoCompareApi import CriptoCompare
from coin.Api.apiKey import AcessoApi


# Create your views here.
api = AcessoApi('apiKey.key')
cc = CriptoCompare(api.key)



def update():
    index

def index(request):

    dados = {
        "cotacoes": 
            [
                {
                    "BitCoin":cc.cotarPorMoeda("BTC", "BRL"), 
                    "Etherium":cc.cotarPorMoeda("ETH", "BRL"),
                    "Binance":cc.cotarPorMoeda("BNB", "BRL"),
                    "Ripple":cc.cotarPorMoeda("XRP", "BRL"),
                    "Tether":cc.cotarPorMoeda("USDT", "BRL"),
                    "USD Coin":cc.cotarPorMoeda("USDC", "BRL"),
                    "Cardano":cc.cotarPorMoeda("ADA", "BRL"),
                    "Solana":cc.cotarPorMoeda("SOL", "BRL"),
                    "Dogecoin":cc.cotarPorMoeda("DOGE", "BRL"),
                    "Polkadot":cc.cotarPorMoeda("DOT", "BRL"),
                    "Shiba Inu":cc.cotarPorMoeda("SHIB", "BRL"),
                    "Moreno":cc.cotarPorMoeda("XMR", "BRL"),
                    "Litecoin":cc.cotarPorMoeda("LTC", "BRL"),
                    "CHZ":cc.cotarPorMoeda("CHZ", "BRL"),
                    "Chiliz":cc.cotarPorMoeda("XLM", "BRL"),
                    "VeChain":cc.cotarPorMoeda("VET", "BRL"),
                    "Filecoin":cc.cotarPorMoeda("FIL", "BRL"),
                    "Cosmos":cc.cotarPorMoeda("ATOM", "BRL")
                }
                ],
    }

    return render(request,'index.html',dados)
  
