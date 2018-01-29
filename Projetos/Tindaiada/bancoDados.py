# coding: utf-8

# ----------------------BANCO DE DADOS------------------------

def dadosUsuario():
    nome = input('\nQual é seu nome ? ')
    idade = input('Qual é sua idade ? ')
    filme = input('Filme favorito ? ')
    serie = input('Serie favorita ? ')
    password = input('Digite uma senha= ')

    # ---------------------PRINT-------------------------------------

    nomeResultado = open('dadosUsuarios.csv', 'a')
    nomeResultado.write(nome.lower())
    nomeResultado.write(',')
    nomeResultado.write(idade.lower())
    nomeResultado.write(',')
    nomeResultado.write(filme.lower())
    nomeResultado.write(',')
    nomeResultado.write(serie.lower())
    nomeResultado.write(',')
    nomeResultado.write(password.lower())
    nomeResultado.write('\n')
    nomeResultado.close()

# -------------------------------------------------------------
