# Faça um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista, no final mostre:
# A - Quantas pessoas foram cadastradas
# B - Uma listagem com as pessoas mais pesadas.
# C - Uma listagem com as pessoas mais leves.

lista = []
dado = []
while True:
    dado.append(input('Digite o nome: '))
    dado.append(int(input('Digite o Peso: ')))
    lista.append(dado[:])
    dado.clear()
    opc = ' '
    while opc not in 'YN':
        opc = input('Deseja adicionar mais pessoas? [Y]/[N]:').upper().strip()
    if opc == 'N':
        break
print(f'Foram cadastradas um total de {len(lista)} Pessoas.')
print('O nome das pessoas com mais de 100Kg é:', end=' ')
for c in range(len(lista)):
    if lista[c][1] >= 100:
        print(f'[{lista[c][0]}]', end=' ')
print(f'\nO nome das pessoas com menos de 70Kg é:', end=' ')
for c in range(len(lista)):
    if lista[c][1] < 70:
        print(f'[{lista[c][0]}]', end=' ')

