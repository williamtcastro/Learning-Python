#coding: utf-8
# FOR LOOP

listaExemplo = [1,43,3,6,7,8,5,4,75,4,37,78]

for cadaNum in listaExemplo:
	print (cadaNum) # Para cada numero da lista printe ele como se fosse uma váriavel unica
	print ('Numero') #Se colocado indentado ele aparecerá apos cada numero printado

print ('Fim dos numeros') #Se colocado fora da indentação ele aparecerá so no final do FOR


#FOR pode ser usado como contador

for x in range(1,10): #range é do numero inicial até o penultimo numero/ serve como contador tbm
	print(x)
