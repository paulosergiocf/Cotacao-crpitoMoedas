
class AcessoApi:
    def __init__(self, path):
        self.__key = ''
        self.__path = path
        self.importKey()
        
    @property
    def key(self):
        return self.__key

    def importKey(self):
        try:
            fileKey = open(self.__path)
            self.__key = fileKey.readline()
            fileKey.close()
            
        except Exception as erro:
            raise erro

        
