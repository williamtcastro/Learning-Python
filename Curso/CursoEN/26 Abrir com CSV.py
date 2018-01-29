#coding: utf-8

#Abrindo arquivo CSV

import csv #importar tal modulo

with open('teste.csv') as csvfile: #Abrir 'arquivo' como talNome
	readCSV = csv.reader(csvfile, delimiter=',') # 'VAR = MODULO.FUNCAO(talNome, delimitador='limitador')'

	dates = []
	colors =[]

	for row in readCSV:

		color = row[4]
		date = row[0]

		dates.append(date)
		colors.append(color)

	qualCor = input('Escreva a COR para saber a data ! =')
	coldex = colors.index(qualCor.lower) #coldex = color index

	aData = dates[coldex]

	print('A data de',qualCor,'é',aData)
'''
	LOCALIZAR DATA POR PERGUNTA(COR)

	dates = []
	colors =[]

	for row in readCSV:

		color = row[4] #.lower é usado pra forçar o codigo ler letras minusculas mesmo se escrito maiuscula
		date = row[0]

		dates.append(date)
		colors.append(color)

	qualCor = input('Escreva a COR para saber a data ! =')
	coldex = colors.index(qualCor.lower) #coldex = color index

	aData = dates[coldex]

	print('A data de',qualCor,'é',aData)

'''
'''
	Printar itens puros

	for row in readCSV:
		print(row)

'''
'''
	Separar itens de um arquivos em categorias(listas)

	dates = []
	colors =[]

	for row in readCSV:

		color = row[4]
		date = row[0]

		dates.append(date)
		colors.append(color)

	print(dates)
	print(colors)

'''