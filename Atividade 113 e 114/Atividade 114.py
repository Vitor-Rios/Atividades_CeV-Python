# Crie um programa em python que teste se o site Pudim esta acessivel pelo computador do usuário.

import urllib.error
import urllib.request


try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site não esta acessível.')
else:
    print('Consegui acessar o site com sucesso.')

