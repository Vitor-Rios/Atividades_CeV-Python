# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se ja é hora de se alistar
# Se ja passou do tempo do alistamento.
# Seu programa tambem deverá mostrar o tempo que falta ou o que passou do prazo

from datetime import date

ano = int(input('Digite o ano de seu nascimento'))
atual = date.today().year - ano

if atual < 18 :
    print(f'Ainda falta {18 - (atual)} anos para se alistar')

elif atual == 18:
    print('Se Fudeu, Esta na hora de se Alistar')

else:
    print(f'Ja passou {atual - 18} anos de se alistar')



