#coding: utf-8
#FUNCOES BUILT IN

#(abs)Valor Absoluto = Quando necessário um numero positivo ou distancia do zero

exNum1 = -5
exNum2 = 5

print(abs(exNum1))

if abs(exNum1) == exNum2:
	print('Eles são o mesmo!')

#FUNÇÃO HELP
'''

help() #busca geral

----------------
import time

help(time) #Pede ajuda em Help

------------------------
'''
#Maximo e minimo 

exList = [5,7,3,9,2,0]
print ('max',max(exList)) #Dá o valor maximo da lista
print ('min',min(exList)) #Dá o valor minimo da lista

#---------------------

# Arredondamento

x = 5.6

print('round',round(x)) #Arredonda o valor dependendo do valor da casa decimal | 0.5 vai pra cima | 0.49 vai para baixo |

#----------------------

# MATH FLOOR(ARREDONDAMENTO PARA BAIXO) | CEIL(ARREDONDAMENTO PARA CIMA)

import math

print ('cima =',math.floor(x)) # para cima
print ('baixo =',math.ceil(x)) # para baixo

#TRANFORMAR EM INT E FLOAT
intMe = '55'

print (int(intMe)) #tranformando em int
print (float(intMe)) #transformando em float

#--------------------------

# TRANSFORMAR EM STRING

strMe = 77
print(str(strMe))