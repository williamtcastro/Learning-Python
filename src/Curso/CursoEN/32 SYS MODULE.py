#coding: utf-8
#Sys Modules

import sys

sys.stderr.write('Isso é um stderr') #ESCREVER VERMELHO
sys.stderr.flush() # --------
sys.stderr.write('Isso é um stdout') #ESCREVER NORMAL

print(sys.argv) #Printar argumento atual

if len(sys.argv) > 1: #se o tamanho é maior que x então print o 1
	print(float(sys.argv[1])+5)

#SYS MODULE PODE SER USADO PARA INTERCOMUNICAR COM OUTRAS LINGUAS