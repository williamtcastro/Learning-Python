#coding: utf-8
#URLLIB

import urllib.request
import urllib.parse

'''

# x = urllib.request.urlopen('https://www.google.com') /requisitar pagina do google

# print(x.read()) # ler requisição

url = 'https://pythonprogramming.net/search'
valores = {'q':'basic'}

data = urllib.parse.urlencode(valores)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print (respData)

'''
'''
ESSE NÃO FUNCIONARA POIS O USER AGENTE ESTA COMO PYTHON 

try: 
	x = urllib.request.urlopen('https:www.google.com/search?q=test')
	print(x.read())

except Exception as e:
	print(str(e))

'''

# USER AGENT ESTÁ DEFINIDO COMO MOZILA SENDO ASSIM PODEREMOS ENGANAR O FILTRO

try:
	url = 'https://www.google.com/search?q=test'
	headers = {}
	headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
	req = urllib.request.Request(url, headers=headers)
	resp = urllib.request.urlopen(req)
	respData = resp.read()

	print(respData)

	saveFile = open('teste.txt','w')
	saveFile.write(str(respData))
	saveFile.close()


except Exception as e:
	print(str(e))