   #coding: utf-8


#TRY/EXCEPT ERRO HANDLING

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

	try: #TENTE PROCURAR SE NÃO CONTINUE E NÃO QUEBRE

		qualCor = input('Escreva a COR para saber a data ! =')
		
		if qualCor in colors: #USANDO IF É OUTRA FORMA DE USAR UM 'TRY'
			coldex = colors.index(qualCor.lower()) #coldex = color index
			aData = dates[coldex]
			print('A data de',qualCor,'é',aData)


		else: 
			print('Não é uma cor, ou não existe na lista !')


	except Exception as e: #CRIA UMA EXCEÇÃO PARA TUDO (SE TUDO FALHAR CONTINUE)
		print(e)

	print('continua')

