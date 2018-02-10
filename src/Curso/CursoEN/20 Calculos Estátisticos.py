#coding: utf-8
#Calcluos Estátisticos

import statistics

listaExemplo = [4,6,7,6,7,4,5,4,3,4,4,2,5,6,3,6,6,1,3,5,3]

'''
x = statistics.mean(variavel)#media
x = statistics.median(listaExemplo)#mediana
x = statistics.stdev(listaExemplo)#desvio padrão
x = statistics.variance(listaExemplo)#variança
'''
x = statistics.mean(listaExemplo)#media

print (x)