#coding: utf-8
#FUNÇÃO APPEN = PARA GRAVAÇÃO EM ARQUIVOS

appendEu = '\nUm pouco de informação (Append)' #Variavel comum

appendFile = open('exemplo14.txt', 'a') #Função OPEN usando 'a' para 'Agregar'(APPEND)
appendFile.write(appendEu) #.write para chamar a função de escrita seguido da varivel com o texto
appendFile.close() #Fechar arquivo como sempre