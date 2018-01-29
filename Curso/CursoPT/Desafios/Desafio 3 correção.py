#coding: utf-8
print ('Desafio 03')

primeiroNum = int (input('Primeiro Numero = '))
segundoNum = int (input('Segundo Numero = '))

soma = primeiroNum+segundoNum

'''
print ('A soma entre,',primeiroNum,'e',segundoNum,'é =',primeiroNum+segundoNum)
print ('A soma é =',primeiroNum+segundoNum)
'''
#NOVO MÉTODO DE PRINT
print('A soma entre {} e {} vale = {}'.format(primeiroNum,segundoNum,soma))


#int + input separados por () significa que será interpretado como um numero         var= int(input('TEXTO AQUI !'))

