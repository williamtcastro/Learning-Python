# ABRIR E SALVAR EM UM ARQUIVO
#coding: utf-8

#WRITE É ESCREVER EM CIMA DO QUE ESTIVER LA
#APPEND É ADICIONAR NO ARQUIVO

texto = 'Esse é o meu texto\nEssa é uma nova linha' #variavel comum

saveFile = open ('exemplo14.txt', 'w') # Open é o comando para abrir , seguido do local do arquivo, seguido da ação
saveFile.write (texto) #.write é comando para escitra seguido da variavel que será escrita
saveFile.close() #.close é comando para fechar o arquivo

'''
W = Abrir apagar e escrever (WRITE)
A = Append (Agregar) no arquivo
R = Ler arquivos
'''


'''
SE INICIADO ELE IRÁ RODAR O CÓDIGO
E CRIAR UM ARQUIVO COM O TEXTO DA VARIAVEL
'''


