#coding: utf-8
#Classes do Python

'''
É UM MEIO DE AGRUPAMENTO DE COISAS
DEVE CONTER DEFINICOES DA CLASSE COMO UMA CALCULADORA DEVE CONTER (SUBTRAÇÃO,ADIÇÃO...)
'''

class calculadora:

	def adicao(x,y):
		add = x + y
		print(add)

	def subtracao(x,y):
		sub = x - y
		print(sub)

	def multiplicacao(x,y):
		mult = x * y
		print(mult)

	def divisao(x,y):
		div = x / y
		print (div)


calculadora.multiplicacao(5,3) #função para chamar a classe (classe.função(variaveis))
