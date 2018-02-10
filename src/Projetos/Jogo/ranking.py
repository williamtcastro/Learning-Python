
import csv
import math
import time
import numpy as np

#--------- Funcoes --------------

def ranking():
    with open('jogadores.csv') as jogadores:
        rankJogadores = csv.reader(jogadores, delimiter=',')

        nome = []
        ponto = []
        data = []

        for row in rankJogadores:

            nomes = row[0]
            pontos = row[1]
            datas = row[2]

            nome.append(str(nomes))
            ponto.append(int(pontos))
            data.append(datas)

        print(nome)
        print(ponto)
        print(data)

        print('--------------------------------------------------------')


'''

def perguntasCSV():
    global idsPgs
    with open('perguntas.csv') as perguntas:
        pgLog = csv.reader(perguntas, delimiter=',')

        indices = []
        perguntasIN = []
        #respostasIN = []

        for row in pgLog:
            ids = row[0]
            pgs = row[1]
            #rps = row[2]

            indices.append(ids)
            perguntasIN.append(pgs)
            #respostasIN.append(rps)

        idsPgAt = str(idsPgs)

        perguntaInicial = idsPgAt
        perguntaAtual = indices.index(perguntaInicial)
        aPerguntaAtual = perguntasIN[perguntaAtual]
        print(perguntaInicial)
        print(perguntaAtual)
        print(aPerguntaAtual)
        pass

perguntasCSV()

'''
ranking()