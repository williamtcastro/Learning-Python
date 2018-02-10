largura = int(input('Digite a largura da parede: '))
altura = int(input('Digite a altura da parede: '))

area = largura*altura
tinta = area/2

print('A area de sua parede é {}m quadrados, e a tinta necessária para pinta-lá {}L de tinta !'.format(area,tinta))