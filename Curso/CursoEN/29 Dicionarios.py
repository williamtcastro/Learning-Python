#coding: utf-8

#Dicionarios 
'''
São desorgarnizados
Podem ter qualquer valor
Você pode mencionar outros dicionarios em um dicionario
'''

exDict = {'Nath':[17,'Ruivo'], 'Cris':[18,'Castanho'], 'Will':[19,'Loiro'], 'Renan':[18,'Preto']}

# MOSTRAR O DICIONARIO
print(exDict)

'''
	#METODOS DE MODIFICAR DICIONARIO#

# MOSTRAR A IDADE DA 'NATH'
print(exDict['Nath'])

# MOSTRAR CABELO DE 'NATH'
print(exDict['Nath'][1])

# ADICIONAR 'IGOR' NO DICIONARIO
exDict['Igor'] = 18
print('+IGOR = ',exDict)

# MUDAR O VALOR DE 'IGOR' NO DICIONARIO
exDict['Igor'] = 19
print(exDict)

# DELETAR IGOR DO DICIONARIO
del exDict['Igor']

print(exDict)

'''

