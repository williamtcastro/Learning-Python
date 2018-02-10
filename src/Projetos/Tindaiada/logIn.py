#coding: utf-8
import csv

#-------------------LOG IN SISTEMA----------------------------

def logIn():

	with open('dadosUsuarios.csv') as dadosUser:
		lerCSV = csv.reader(dadosUser, delimiter=',')

		users =[]
		senhas=[]

		for row in lerCSV:

			user = row[0]
			senha = row[4]
			users.append(user)
			senhas.append(senha)

		qualNome = input('Digite seu nome = ')
		inSen = users.index(qualNome.lower()) #inSen = Index da senha
		aSen = senhas[inSen]
		senLog = input('Digite sua senha = ')
	
		if  senLog.lower() == aSen:
			print ('\nBEM-VINDO,',qualNome,'\n')
			#menu.inicio()

		else:
			print ('\nTENTE NOVAMENTE\n')
			logIn()