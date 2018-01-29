import urllib.request
import urllib.parse
import re

url = 'https://pythonprogramming.net/introduction-to-python-programming/'

valores = {'s': 'basics',
           'submit': 'search'}

data = urllib.parse.urlencode(valores)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

# print(respData)

paragrafos = re.findall(r'<p>(.*?)</p>', str(respData))

for cada in paragrafos:
    print(cada)
