from django.http import HttpResponse
from django.shortcuts import render
from .models import Cotacoes

from coin.criptoCompare import CriptoCompare

# Create your views here.

cc = CriptoCompare("e2fd112ffaf6388810cb1d315ad76a3093d2a28e1a7b0135060f30ef89207b1f")
 
def index(request):
    
    dados = {
        'btc': cc.cotar("BTC", "USD")
    }
    return render(request,'index.html', dados)
  
