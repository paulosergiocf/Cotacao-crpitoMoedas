import requests

class CriptoCompare():
    def __init__(self, keyApi):
        self.keyApi = keyApi
        
    def cotarPorMoeda(self, fsym, tsyms):
        requestHttp = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={fsym}&tsyms={tsyms}&api_key={self.keyApi}").json()
        return requestHttp
