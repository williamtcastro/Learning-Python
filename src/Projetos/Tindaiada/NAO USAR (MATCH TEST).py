#coding: utf-8



import csv

def testeCSV():

#-----------------LEITURA CSV--------------------------------

	with open('dadosUsuarios.csv') as dadosUser:
		lerCSV = csv.reader(dadosUser, delimiter=',')

		users =[]
		idades=[]
		filmes=[]
		series =[]

		for row in lerCSV:

			user = row[0]
			idade = row[1]
			users.append(user)
			idades.append(idade)

#-------------PROCURA MATCH IDADE----------------------------

		qualNome = input('Digite seu nome = ')
		indade = users.index(qualNome.lower()) #indade = index idade
		aIdade = idades[indade]
		print('Sua idade =',aIdade.lower())


'''
--------------TO TENTANDO FAZER UM TESTE----------------------

		z = aIdade

		if any(z == aIdade for x in idades):
			print ('Não entendi')

		else:
			print ('Não')
'''
