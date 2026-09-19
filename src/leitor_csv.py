##Código para abrir e ler o doc csv##  
## Seu objetivo aqui é criar uma função que abra o arquivo data/dataset.csv, pegue a coluna que você quer pesquisar (por exemplo, o nome do jogo) e retorne isso como uma lista no Python.##
##Importante: Use "with open" para garantir que o arquivo seja fechado corretamente!##

import csv

class leitor:
    
    def __init__(self):
        with open("data/jogos.csv", "r", encoding="utf-8") as arquivo:
            arquivo_csv = csv.reader(arquivo, delimiter=",")
            self.nome_jogos = []
            for i,jogo in enumerate(arquivo_csv):
                if i == 0:
                    self.nome_jogos.append(jogo[2])
                else:
                    self.nome_jogos.append(jogo[2])

    def buscar_jogo(self):
        # primeiro = self.nome_jogos[61]
        # segundo = self.nome_jogos[62]
        # terceiro = self.nome_jogos[63]
        # quarto = self.nome_jogos[3]
        # print(primeiro,'/',segundo,'/',terceiro,'/',quarto)
        print(self.nome_jogos)

c1=leitor()
c1.buscar_jogo()


