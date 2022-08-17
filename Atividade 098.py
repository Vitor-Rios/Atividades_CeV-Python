# Faça um programa que tenha um função chamada contador(),
# que receba três parâmetros: inicio, fim e passo e realize a contagem.
# Seu programa tem que realizar tres contagens atraves da função cirada:
# A - De 1 até 10, de 1 em 1
# B - De 10 até 0, de 2 em 2
# C - Uma contagem personalizada.

import time


def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p = abs(p)
    print(f'~~' * 20)
    print(f'Contando de {i} até {f} de {p} em {p}')
    if i > f:
        p = -p
        f -= 2
    for c in range(i, f + 1, p):
        print(c, end=' ')
        time.sleep(0.5)
    print()


contador(1, 10, 1)
contador(10, 0, 2)
print(f'~~' * 20)
print('Customize a contagem')
i = int(input('Digite o inicio: '))
f = int(input('Digite o Final: '))
p = int(input('Digite o Passo'))
contador(i, f, p)
