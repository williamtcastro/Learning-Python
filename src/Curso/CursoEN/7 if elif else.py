#coding: utf-8
#If /elif /else

# se if falhar else rodará porêm se o else falhar elif entrará em ação

x = 5
y = 10
z = 22

if x > y: #nesse caso é falso 
	print ('X é maior que Y')

elif x < z: #nesse caso é verdadeiro / se esse for verdadeiro ele para aqui porem se for falso continuara até achar o verdadeiro
	print ('x é menot que Z')

elif 5 > 2: #elif pode ser adicionado quantas vezes necessário no programa
	print ('5 é maior que 2')

else: #se o else for ativado quer dizer que elif é falso !
	print ('Falhou')

