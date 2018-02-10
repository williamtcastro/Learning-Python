import urllib.parse
import urllib.request
import re



altcoin = input('\nDigite sua ALTCOIN (BITCOIN/IOTA/LITECOIN): ')
moeda = input('Digite sua Moeda (USD/ BRL): ')

url = 'https://www.coingecko.com/pt/gr%C3%A1ficos_de_pre%C3%A7os/{}/{}'.format(altcoin,moeda)
print(url)
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req)
respData = resp.read()

geral = re.findall(r'<body>(.*?)</body>',str(respData))
div1 = re.findall(r'<div id="wrapper">(.*?)</div>',str(geral))

print(geral)
print(div1)

nome = re.findall(r'<div = class="coin-value">(.*?)</div>',str(div3))
valor = re.findall(r'<span class="currency-exchangable">(.*?)</span>',str(div3))
porcentagem = re.findall(r'<div class="stat-percent-lg text-green">(.*?)<i class="fa fa-level-up">', str(div3))



