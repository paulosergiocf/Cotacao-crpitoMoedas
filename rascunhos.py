from core.coin.Api.criptoCompareApi import CriptoCompare
from core.coin.Api.apiKey import AcessoApi
from core.coin.BdSqlite3 import BancoDeDados
from core.coin.Graficos import Grafico

from datetime import datetime
api = AcessoApi('apiKey.key')
cc = CriptoCompare(api.key)
sqlite = BancoDeDados()

# dado = cc.cotarPorMoeda("BTC", "BRL")["BRL"]

# data = datetime(year=2022,month=8,day=15)

data = sqlite.buscardados()

grafico = Grafico(data)

dataBitcoin, valorBitcoin = grafico.separarMoedas('etherium')
grafico.gerarGrafico(dataBitcoin, valorBitcoin, 'Etherium')



# for i in data:
#     print('-'*30)
#     for l in i:
#         print(l)

# sqlite.insertDados("Bitcoin", dado["BRL"])

# sqlite.insertDadoRetroativo("Bitcoin", valor, data)

# data = {
#     # "bitcoin":{
#     #     "15/08/2022":125205.92,
#     #     "16/08/2022":123933.69,
#     #     "17/08/2022":121238.58,
#     #     "18/08/2022":122104.57
#     # },
#     # "etherium":{
#     #     "15/08/2022":9879.4,
#     #     "16/08/2022":9759.03,
#     #     "17/08/2022":9537.92,
#     #     "18/08/2022":9696.29
#     # }
#     # "binance":{
#     #     "15/08/2022":1661.53,
#     #     "16/08/2022":1643.9,
#     #     "17/08/2022":1596.00,
#     #     "18/08/2022":1571.09
#     # }
# }
    
    
# for moeda, dados in data.items():
#     print(f"{moeda}")
#     for data, valor in dados.items():
#         sqlite.insertDadoRetroativo(moeda, valor, datetime.strptime(data, '%d/%m/%Y').date())
    
# data = "15/08/2022"
# data1 = datetime.strptime(data, '%d/%m/%Y').date()

# sqlite.insertDadoRetroativo("Bitcoin", valor, data)

