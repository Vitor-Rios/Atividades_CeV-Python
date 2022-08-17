# Faça um programa que tenha um lista chamada numeros e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 numeros e vai coloca-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior

import random
import time


def sorteia(list):
    print('Sorteando os numeros: ')
    for c in range(0, 5):
        num = random.randint(0, 10)
        print(num, end=' ')
        lista.append(num)
        time.sleep(0.5)
    print()


def somaPar(list):
    s = 0
    for c in lista:
        if c % 2 == 0:
            s = s + c
    print(f'Somando os valores Pares da Lista {lista}: Temos:{s}')


lista = []
sorteia(lista)
somaPar(lista)
