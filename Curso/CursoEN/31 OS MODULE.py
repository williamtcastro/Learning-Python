#coding: utf-8
#MODULOS QUE JA VEM
#OS Module

import os
import time

dirAtual = os.getcwd()

print(dirAtual)

os.mkdir('Diretorio novo') #Criar diretorio novo

time.sleep(2)

os.rename('Diretorio novo','Dirnv2') #Renomear Diretorio ('Antigo , para o novo ')

time.sleep(2)

os.rmdir('Dirnv2') #Remover diretorio

#EXISTEM VARIAS OPÇÕES COM O OS MODULE