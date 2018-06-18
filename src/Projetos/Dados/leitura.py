import csv

def procura():
    query = input("Digite o nome para receber a lista das ultimas ligações.\n >>> ")
    index(query)

def index(query):
    with open('Phonelog.csv') as chamadaLog:
        phoneLog = csv.reader(chamadaLog, delimiter=',')

        tempoIn = []
        numeroIn = []
        nomeIn = []
        dataIn = []

        for row in phoneLog:
            nome = row[2]
            data = row[0]
            numero = row[1]
            tempo = row[3]

            nomeIn.append(nome.lower())
            dataIn.append(data)
            numeroIn.append(numero)
            tempoIn.append(int(tempo))

    if query in nomeIn:
        for i in nomeIn[query]:
            print(i)


    # CRIAR LISTA SEQUENCIAL DE DADOS

    # for i in range(len(tempoIn)):
    #	tempo1= tempoIn[i]
    #	print(tempo1)

procura()
