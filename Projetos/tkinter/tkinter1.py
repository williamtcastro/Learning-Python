# -*- coding: utf-8 -*-
import tkinter as tk
import urllib.parse
import urllib.request
import re
import csv

window = tk.Tk()


#------------LAYOUT--------------
window.title("Boletim eletrônico")
window.geometry("400x400")

#-------------FUNCOES---------------

def logic():

    aluno = int(inAluno.get())
    bimestre = int(inBimestere.get())

    txtResultado = tk.Text(master=window, height=200, width=400)
    txtResultado.grid(column=0, row=6)

    if bimestre > 4:
        msgErro = str("Só existem 4 bimestres em um ano !")
        txtResultado.insert(tk.END,msgErro)

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
            txtResultado.insert(tk.END,c7)


#----TEXT---------------------
txtIntro = tk.Label(text ='Olá, Bem Vindo ao boletim eletrônico')
txtIntro.grid(column=0,row=0)

txtAluno = tk.Label(text='Digite o numero do aluno.')
txtAluno.grid(column=0,row=1)

txtBimestre = tk.Label(text='Digite o bimestre')
txtBimestre.grid(column=0,row=3)


#----INPUT---------------------
inAluno = tk.Entry()
inAluno.grid(column=0,row=2)

inBimestere = tk.Entry()
inBimestere.grid(column=0,row=4)

#------BUTTONS---------------------
buttonSend = tk.Button(text="Enviar Dados", command=logic)
buttonSend.grid(column=0,row=5)

window.mainloop()
