#coding: utf-8
#Calculadora

#--------------Inicio----------------------------

print('1- Adição\n2- Subtração\n3- Multiplicação\n4- Divisão\n')
resp = int(input('Escolha a opção = '))
numero1 = input('Digite o primeiro numero = ')
numero2 = input('Digite o segundo numero = ')

#----------Core Calculadora----------------------

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

#----------Chamada de função----------------------------

#Para funçoes de calculo a variavel dever ser int,boolean ou float

if resp == 1:
	calculadora.adicao(int(numero1),int(numero2))

elif resp == 2:
	calculadora.subtracao(int(numero1),int(numero2))

elif resp == 3:
	calculadora.multiplicacao(int(numero1),int(numero2))

elif resp == 4:
	calculadora.divisao(int(numero1),int(numero2))

else:
	print('Deu não !')
