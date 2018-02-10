#coding: utf-8

import random

def rolar():

	num =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
	escolha = random.choice(num)
	print('Resultado = ',escolha)


def inicio():
	input ('Aperte enter para rodar o dado !')
	rolar()

	rodarNovo = input('Digite "sim" para rodar novamente ? ')
	
	if rodarNovo == 'sim':
		rolar()

	else:
		print('Até logo !')


inicio()
