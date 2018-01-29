#RE - REGULAR EXPRESSIONS

'''
IDENTIFICADORES

\d - qualquer numero
\D - qualquer coisa menos um numero
\s - espaço
\S - qualquer coisa menos um espaço
\w - qualquer caractere
\W - qualquer coisa menos um caractere
.  - qualquer coisa menos uma nova linha
\b - the whitespace around words
\. - um ponto

MODIFICADORES

{1,3} estamos esperando de 1-3
+ match se tiver 1 ou mais repeticao
? match se tiver 0 ou 1 repeticao
* match se tiver 1 ou mais repeticao
$ match o final de uma string
^ match no comeco de uma string
| match either or \d(1-3 | \d(2-4)
[] range ou 'varianca' #[A-Z] [1-5a-qA-Z]
{x} esperando quantidade 'x'

WHITE SPACE CHARACTERS

\n - linha nova
\s - espaço
\t - tab
\e - escape
\f - form feed
\r - return

NÃO ESQUEÇA

. + * ? [ ] $ ^ ( ) { } | \ - se precisar usar esses é necessário dar escape nelas 


'''

import re

strExemplo = '''
Jessica tem 15 anos, e Daniel tem 27 anos.
Eduardo tem 97 anos, e seu avo, Oscar tem 102.
'''

idades = re.findall(r'\d{1,3}',strExemplo)
nomes = re.findall(r'[A-Z][a-z]*',strExemplo)

print(idades)
print(nomes)

idadeDict = {}

x = 0

for cadaNome in nomes:
	idadeDict[cadaNome] = idades[x]
	x+=1

print(idadeDict)