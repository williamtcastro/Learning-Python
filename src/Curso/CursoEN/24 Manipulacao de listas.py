#coding: utf-8
#Manipulação de lista

#------------Append------------------

lista = [3,7,3,5,1,2,5,6,7,8,1,2,4]

lista.append(2) #var.append(var) --- adicionar alguma coisa na lista, você pode adicionar qualquer coisa

print('Append = ',lista)

#-------------Insert--------------

lista.insert(2,44) #Inserir o valor --- var.insert(local,valor) | ele será inserido sem apagar nada

print('Insert = ',lista)

#------------Remove---------------

lista.remove(3) #Remover valor -- var.remove(valor) ele removera o primeiro valor igaul ao indicado 

print('Remove = ',lista)


#-----------Remove w/ index--------

lista.remove(lista[1]) #Remover valor expericicado no index -- var.remove(var[index])

print ('Remove index = ',lista)

#-----------

'''
Print de lista 
#------------Slice------------
print (var[inicioIndex:ultimoIndex]) ele se iniciará no inicioIndex e irá um antes do ultimoIndex

#-----------Print ultimos da lista--------
print (var[-index]) quando o sinal negativo for usado ele começara do fim para o começo

#----------Print o index do valor-------
print (var.index(valor)) descobrirá o index do valor

#---------Quantas vezes o valor repete-----
print (var.count(valor)) irá contar quantas vezes repete

#---------Organizar-------------
var.sort() irá organizar em forma crescente, tanto numeros quanto palavras

print(var)

#--------
'''

#--------Exemplos--------------
print('\n------------Exemplos-----------------\n')

print ('Slice = ',lista[3:6])
print ('Print ultimos da lista = ',lista[-1])
print ('Print o index do valor = ',lista.index(2))
print ('Quantas vezes o valor repete = ',lista.count(2))

lista.sort()
print('Organizar = ',lista)

#------------
print()