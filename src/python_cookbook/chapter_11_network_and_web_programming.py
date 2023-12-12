from chapter_0 import prn_tem

prn_tem('11.1. Interacting with HTTP Services As a Client')
from urllib import request, parse
url = 'http://httpbin.org/get'
param = {
    'name1': 'value1',
    'name2': 'value2'
}
querysting = parse.urlencode(param)
with request.urlopen(url+'?'+querysting) as u:
    resp: bytes = u.read()
    from pprint import pprint
    print(resp.decode('UTF-8'))

from urllib import request, parse
url = 'http://httpbin.org/post'
param = {
    'name1': 'value1',
    'name2': 'value3'
}
querysting = parse.urlencode(param)
resp = request.urlopen(url, querysting.encode('ascii'))
mes = resp.read()

print(mes.decode('utf-8'))

from urllib import request, parse

headers = {
    'User-agent': 'none/ofyourbudiness',
    'Spam': 'Eggs'
}
req = request.Request(url, querysting.encode('ascii'), headers=headers)
resp = request.urlopen(req)
mes = resp.read()
mes_str = mes.decode('utf-8')
print(mes_str)

import requests
url = 'http://httpbin.org/post'
param = {
    'name1': 'value1',
    'name2': 'value2',
}

headers = {
    'User-agent': 'none/ofyourbusiness',
    'Spam': 'Eggs'
}

resp: requests.Response = requests.post(url, data=param, headers=headers)
text = resp.text
print(text)
print(resp.content)
print(resp.json())
import requests
resp: requests.Response = requests.head('https://python.org/')
print(resp.status_code)
# # print(resp.headers['last-modified'])
# print(resp.headers['content-type'])
# resp.headers['content-lenhth']
for header, content in resp.headers.items():
    print(f'{header}: {content}')

import requests

resp: requests.Response = requests.get('https://pypi.python.org/pypi?:action=login', auth=('user', 'password'))
print(resp.text)
for hed, val in resp.headers.items():
    print(f'{hed}: {val}')
hedp = resp.headers['Permissions-Policy']
for inem in hedp.split(','):
    print(inem)

import requests
url = 'http://httpbin.org/post'
# file = {'file': ('f')}
prn_tem('11.2. Creating a TCP Server')
from socketserver import BaseRequestHandler, TCPServer
class EchoHandler(BaseRequestHandler):
    def handle(self):
        print(f'Got connection j')
