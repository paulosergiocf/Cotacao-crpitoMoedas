from django.http import HttpResponse
from django.shortcuts import render
from .models import Cotacoes
from coin.Api.criptoCompareApi import CriptoCompare
from coin.Api.apiKey import AcessoApi
from coin.BdSqlite3 import BancoDeDados
from coin.Graficos import Grafico


# Create your views here.
api = AcessoApi('apiKey.key')
cc = CriptoCompare(api.key)
bd = BancoDeDados()


def update():
    index

def index(request):

    dados = {
        "cotacoes": 
            [
                {
                    "BitCoin":cc.cotarPorMoeda("BTC", "BRL"), 
                    "Etherium":cc.cotarPorMoeda("ETH", "BRL"),
                    "BnB":cc.cotarPorMoeda("BNB", "BRL"),
                    "XRP":cc.cotarPorMoeda("XRP", "BRL"),
                    "USDT":cc.cotarPorMoeda("USDT", "BRL"),
                    "USDC":cc.cotarPorMoeda("USDC", "BRL"),
                    "ADA":cc.cotarPorMoeda("ADA", "BRL"),
                    "BUSD":cc.cotarPorMoeda("BUSD", "BRL"),
                    "SOL":cc.cotarPorMoeda("SOL", "BRL"),
                    "DOGE":cc.cotarPorMoeda("DOGE", "BRL"),
                    "DOT":cc.cotarPorMoeda("DOT", "BRL"),
                    "SHIB":cc.cotarPorMoeda("SHIB", "BRL"),
                    "XMR":cc.cotarPorMoeda("XMR", "BRL"),
                    "LTC":cc.cotarPorMoeda("LTC", "BRL"),
                    "CHZ":cc.cotarPorMoeda("CHZ", "BRL"),
                    "XLM":cc.cotarPorMoeda("XLM", "BRL"),
                    "VET":cc.cotarPorMoeda("VET", "BRL"),
                    "FIL":cc.cotarPorMoeda("FIL", "BRL"),
                    "ATOM":cc.cotarPorMoeda("ATOM", "BRL")
                }
                ],
    }

    return render(request,'index.html',dados)
  
