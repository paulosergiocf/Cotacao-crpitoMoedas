import matplotlib.pyplot as plt

class Grafico:
    def __init__(self, dados):
        self.dados = dados
    
    def gerarGrafico(self, listaDatas, listaValores, nome):
        plt.plot(listaDatas, listaValores, linestyle = 'dashed', label=f'{nome}')
        plt.grid(True)
        plt.legend()
        plt.xlabel('dia')
        plt.ylabel('Valor (R$)')
        plt.show()
        
    def separarMoedas(self, moeda):
        lista = []
        listaValor = []
        listaData = []
        
        for dado in self.dados:
            if dado[1] == moeda:
                lista.append(dado)
        
        for linha in lista:
            listaValor.append(linha[2])
            listaData.append(linha[3])
            
        return listaData, listaValor
    