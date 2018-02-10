
# -*- coding: utf-8 -*-
import urllib.parse
import urllib.request
import re
import csv

continuar = 's'
while continuar == 's':

    aluno = input('\nDigite o numero do aluno: ')
    bimestre = int(input('Digite o bimestre: '))

    if bimestre > 4:
        print('Só existem 4 bimestres em um ano !')

    else:
        url = 'http://www.pelicano.itstelecom.com.br/form_mostra_boletim.php?busca={}&teste={}&Submit=Enviar'.format(aluno,bimestre)
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req)
        respData = resp.read()

        geral = re.findall(r'<table>(.*?)</table>',str(respData))
        paragrafos = re.findall(r'<strong>(.*?)</strong>',str(geral))
#        print(paragrafos)

        for cada in paragrafos:
            c1 = cada.replace('\\\\xf3','o')
            c2 = c1.replace('\\\\xf4', 'o')
            c3 = c2.replace('\\\\xe1','a')
            c4 = c3.replace('\\\\xe7','c')
            c5 = c4.replace('\\\\xea','e')
            c6 = c5.replace('\\\\xe3','a')
            c7 = c6.replace('\\\\xe9','e')
            print(c7)

#            notas = re.findall(r'\d{1,6}', c7)
#            materias = re.findall(r'[A-Z][a-z]*', c7)
#            print('-'*72,'\n')
#            print(notas)
#            print(materias)


#        with open('notas.csv', 'a', newline='') as notas:
#            lognotas = csv.writer(notas)
#            lognotas.writerow(paragrafos)
#            notas.close()

 #    continuar = input('Deseja perquisar novamente ? ').lower()