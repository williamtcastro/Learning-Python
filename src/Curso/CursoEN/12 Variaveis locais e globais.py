#coding: utf-8
#Variaveis Globais e locais

'''
Variavel global pode ser acessado em qualquer lugar
Variavel local so pode ser acessado no modulo expecifico

Muitas empresas ou locais não gostam de usar variaveis locais
'''
 
x = 6 #ainda não é uma variavel global sozinha

#Global
print ('Usando a função como global\n') # \n significa quebra linha

def exemplo():
	global x #esse é o meio de resolver o problema da variavel local
	print (x) #você pode usalá ou modifica lá até um ponto 
	print (x+5)
	#x +=6 aqui ele acha que é uma variavel local

exemplo()

print ('--------------------------------------------------\n')

#----------------------------------------------------------------------------------

#local para global

print ('Usando a função como local e retornando valor global\n')
'''
outro meio de usar uma variavel global é criando outra função local
EX:
'''
def exemplo():
	globx = x #globx - variavel local puxando de x global
	print ('Esse é o x porem como globx:',globx)
	globx +=5 #modificar globx
	print ('Essa é globx: ', globx)

	'''
	se precisar usar essa variavel local em outros lugares
	você dever retornar o valor dela sendo assim
	usando a função RETURN GLOBX
	'''

	return globx #quando ela rodar ela vai retornar o valor final dela

x = exemplo() #voce vai colocar = para pegar o valor e dps modificar com as ações da função

print ('Essa é o return global de globx:', x)