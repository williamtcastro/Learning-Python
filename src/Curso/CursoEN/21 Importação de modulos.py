#coding: utf-8
# Importação de modulos

import statistics as s

'''
1 - import statistics #importando o modulo inteiro
1.1 - import statistics as s #importanto o modulo inteiro e simplificando o nome
2 - from statistics import mean #importanto só uma função especifica do modulo
2.1 - from statistics import mean as m #importanto só uma função especifica do modulo e simplificando o nome
3 - from statistics import variance, mean #importando duas funções apenas do modulo
3.1 - from statistics import variance as v, mean as m #importando duas funções apenas do modulo e simplificando o nome
4 - from statistics import * #importando todas as funções do modulo

2- Quando importado só a função você pode usala como -- var = função(var)
1.1 - Quando importado simplificado o modulo você pode usar como -- var = nomeSimplificado.função(var)
2.1 - Quando importado só a função com o nome simplificado é só usar como -- var = nomeSimplificado(var)
4 - Quando importado modulo usando * significa que você importou todas as funções e pode deve ser usado como -- var = funcão(var)

'''

listaExemplo = [4, 6, 7, 6, 7, 4, 5, 4, 3, 4, 4, 2, 5, 6, 3, 6, 6, 1, 3, 5, 3]

x = s.mean(listaExemplo)  # media

print(x)
