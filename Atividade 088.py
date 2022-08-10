# Faça um programa que ajude um jogador da Mega Sena a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta
import random

lista = []
qtd = int(input('Quantos jogos serão gerados?: '))

for c in range(0, qtd):
    l = 0
    while l < 6:
        num = random.randint(1, 60)
        if num not in lista:
            lista.append(num)
            l += 1
    print(lista)
    lista.clear()
