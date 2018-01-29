#coding: utf-8

#-------------IMPORTS---------------------------

import bancoDados as bD
import logIn

#---------------MENU---------------------------

def menu():
	print ('''Bem-Vindo ao Tindaiada

Digite:

1 - Cadastrar Usuário e Logar a seguir
2 - Entrar com Usuário existente
''')
#------------------TEXTO---------------------	
	opcao = int(input ('Opção = '))

	if opcao == 1:
		bD.dadosUsuario()
		print('\nLogIn\n')
		logIn.logIn()


	elif opcao == 2:
		logIn.logIn()

	else:
		print('Opção não válida !')

menu()

#----------------FUNCOES-----------------------

#logIn.logIn()

'''
 
logIn.logIn()
bD.dadosUsuario()
mT.testeCSV()


'''
