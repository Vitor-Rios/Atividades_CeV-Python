# Crie um programa que tenha uma função voto() que vai recever como parametro o ano de nascimento de uma pessoa,
# Retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições

import datetime


def voto(ano):
    hoje = datetime.date.today().year
    idade = hoje - ano
    if 18 <= idade <= 100:
        print(f'Com {idade}, O Voto é Obrigatório')
    elif idade < 16:
        print(f'Com {idade}, O Voto é Negado')
    else:
        print(f'Com {idade}, O Voto é Opcional')


voto(int(input('Em que ano você nasceu?: ')))
