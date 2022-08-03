# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo. Desconsiderando os espaços.
# EX: APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA

frase = str(input('Digite a frase: ')).strip().upper()
lista = frase.split()
junto = ''.join(lista)
inverso = junto[::-1]

if junto == inverso:
    print(f' Temos um palindromo, você digitou {junto} e ao contrário é {inverso}')
else:
    print(f'Não temos um palindromo, você digitou {junto} e ao contrario é {inverso}')



