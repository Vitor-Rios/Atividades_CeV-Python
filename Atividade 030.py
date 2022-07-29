# Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar.

num = int(input('Digite um numero:'))
rest = num % 2

if rest == 1:
    print('o Numero digitado é ÍMPAR')

else:
    print('o Numero digitado é PAR')

