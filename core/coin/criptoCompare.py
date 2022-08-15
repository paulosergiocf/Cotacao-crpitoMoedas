import requests

class CriptoCompare():
    def __init__(self, keyApi):
        self.keyApi = keyApi
        
    def cotar(self, fsym, tsyms):
        return requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={fsym}&tsyms={tsyms}&api_key={self.keyApi}")