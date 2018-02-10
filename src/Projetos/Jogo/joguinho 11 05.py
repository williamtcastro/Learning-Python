# coding: utf-8
# Jogo

# Variaveis Globais

ponto = 0
certo = 'sim'
resp = 0


# ------------TESTE REPOSTA-------------
def testeResposta():
    global certo, ponto, resp
    if resp == certo:
        print('Acertou\n')
        ponto += 1
        print('Voce tem', ponto, 'pontos')

    else:
        print('Errou !\n')
        print('Voce tem', ponto, 'pontos')


# ------------PERGUNTAS----------------------

def pergunta1():
    global resp
    resp = input('A capital do Brasil e brasilia?\nR=')
    testeResposta()


# -----------------------------------------------------------

def pergunta2():
    global resp
    resp = input('\O\nR=')
    testeResposta()


# -----------------------------------------------------------

def pergunta3():
    global resp
    resp = input('\nO XBOX ONE e melhor que o PS4?\nR=')
    testeResposta()


# -----------------------------------------------------------

def pergunta4():
    global resp
    resp = input('\nDiamante e grafite de lápis são coisas praticamente iguais, mudando apenas a organização dos átomos?\nR=')
    testeResposta()


# ------Inicio--------------------------------------------------------

def inicioJogo():
    print('Responda apenas com sim ou nao\n')
    avancar = input('Aperte enter para avancar !\n')
    return nome


# ----------------------------LOG DE JOGADORES---------------------------------

def logJogo():
    logJogadores = open('jogadores.txt', 'a')
    logJogadores.write('Jogador = ')  # no .write a variavel sempre dever ser str(var)
    logJogadores.write(str(nome))
    logJogadores.write(' | Pontos feitos = ')
    logJogadores.write(str(ponto))
    logJogadores.write('\n')
    logJogadores.close()


# ---------------------------ADICIONE CÓDIGO AQUI-----------------------------------



# -----------------------JOGO-----------------------------
# ------------------COMECA AQUI---------------------------

nome = input('Qual e o seu nome?\nR= ')
print('\nOla', nome, ', Vamos comecar\n')

inicioJogo()
listaPerguntas = [pergunta1(), pergunta2(), pergunta3(), pergunta4()]

for perguntas in listaPerguntas:
    print(perguntas)

print('Voce conseguiu =', ponto, 'pontos !')
print('Obrigado por jogar', nome, '!!!!')

logJogo()

# ---------------------------------------------------------------
