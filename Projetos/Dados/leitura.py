import csv


def procura():
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

        qualNome = input('Digite o nome = ')
        inNome = nomeIn.index(qualNome.lower())
        oNum = numeroIn[inNome]
        print (oNum)


    # CRIAR LISTA SEQUENCIAL DE DADOS

    # for i in range(len(tempoIn)):
    #	tempo1= tempoIn[i]
    #	print(tempo1)


procura()
