##Código para abrir e ler o doc csv##

import csv

class leitor:
    
    def __init__(self):
        with open("data/jogos.csv", "r", encoding="utf-8") as arquivo:
            arquivo_csv = csv.reader(arquivo, delimiter=",")
            self.nome_jogos = []
            for i,jogo in enumerate(arquivo_csv):
                if i == 0:
                    pass #pula o cabeçalho e adiciona somente os jogos
                else:
                    self.nome_jogos.append(jogo[2]) #Adiciona os jogos na lista, buscando exatamente a terceira coluna do arquivo csv

    def buscar_jogo(self):
        primeiro = self.nome_jogos[0]
        segundo = self.nome_jogos[1]
        terceiro = self.nome_jogos[2]
        quarto = self.nome_jogos[3]
        print(primeiro,'/',segundo,'/',terceiro,'/',quarto)
        # print(self.nome_jogos)

c1=leitor()
c1.buscar_jogo()


