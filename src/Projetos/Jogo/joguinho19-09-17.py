#Joguinho 2 - dia 18-09
#-------imports--------------------

import csv
import time

#-----------VARS-------------------

idsPgs = 0
ponto = 0
resp = 0
pgsAtual= 0
nome = 0

#---------Log Jogadores------------------------------------

def logJogo():
    global nome,ponto
    date = time.strftime('%d/%m/%Y')
    with open('jogadores.csv', 'a', newline='' ) as jogadores:
        logJogadores = csv.writer(jogadores)
        logJogadores.writerow([nome,ponto,date])

    jogadores.close()

#---------Perguntas-----------------------

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
        print(aPerguntaAtual)
        pass

#-----------Respostas----------------

def resposta():
    global ponto, resp,idsPgs
    certo = 'sim'
    if resp == certo:
        print('Acertou!')
        ponto = ponto +1
        print('Voce tem', ponto,'pontos.\n')
        idsPgs= idsPgs +1
        return ponto, idsPgs

    else:
        print('Errou!')
        print('Voce tem', ponto, 'pontos.\n')
        idsPgs = idsPgs +1
        return idsPgs

#------------Contagem------------------
def contagem():
    global pgsAtual
    while (pgsAtual < 10):
        perResp()
        pgsAtual = pgsAtual +1

    print('Obrigado por Jogar !')


def perResp():
    global resp
    perguntasCSV()
    resp = input('R= ')
    resposta()
    return resp


def inicio():
    global ponto, nome
    print('Olá, Seja Bem-vindo !')
    nome = input('Qual é o seu nome?\nNome = ')
    print('Olá', nome, 'Vamos começar !\n')
    contagem()
    print('Voce conseguiu =', ponto, 'pontos !\n')
    print('Até logo', nome, '!')
    return nome, resp

def mainFinal():
    inicio()
    logJogo()

#mainFinal()