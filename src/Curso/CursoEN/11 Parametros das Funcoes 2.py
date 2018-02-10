#coding: utf-8
#Parametros da Função 2

def matematicaSimples(num1, num2):
	pass #sempre escreva PASS na funcão se não houver ações nela 

def matematicaSimples(num1, num2=5): #num2=5 esta com o valor padrão ja estabelecido / é usado caso não é necessário customização
	print (num1, num2)

matematicaSimples(2) #nesse caso eu não coloquei o parametro do num2 pois ele ja está preenchido na função padrão

'''
se precisar mudar o valor é so colocar preencher na hora de chamar função 
ex matematicaSimples(2,6) ou matematicaSimples(2,num2=6)
'''
