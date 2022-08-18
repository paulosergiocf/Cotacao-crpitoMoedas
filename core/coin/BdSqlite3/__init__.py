import sqlite3
from datetime import datetime 


class BancoDeDados:
    def __init__(self):
        self.conexao = sqlite3.connect(r'core/db.sqlite3')
        self.criarTabela()
    
    def criarTabela(self):
        try:
            c = self.conexao.cursor()
            c.execute("""create table if not exists coin_cotacoes (
                        id integer primary key autoincrement,
                        coin varchar(200),
                        valor real,
                        dateCoin datetime)""")

            self.conexao.commit()
            c.close()
    
        except Exception as erro:
            raise erro
            
    def insertDados(self, coin: str, valor: float):
        try:
            c = self.conexao.cursor()
            c.execute('INSERT INTO coin_cotacoes (coin, valor, dateCoin) VALUES (?, ?, ?)', (coin, valor, datetime.now()))
            self.conexao.commit()
            c.close()


        except Exception as erro:
            raise erro
    
    def insertDadoRetroativo(self, coin: str, valor: float, data):
        try:
            c = self.conexao.cursor()
            c.execute('INSERT INTO coin_cotacoes (coin, valor, dateCoin) VALUES (?, ?, ?)', (coin, valor, data))
            self.conexao.commit()
            c.close()


        except Exception as erro:
            raise erro
    def buscardados(self):
        
        try:
            c = self.conexao.cursor()
            c.execute("SELECT * from coin_cotacoes")
            data = c.fetchall()
            self.conexao.commit()
            c.close()
            return data

        except Exception as erro:
            raise erro