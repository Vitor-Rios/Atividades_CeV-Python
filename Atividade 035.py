# Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo

a = int(input('Digite o valor da primeira reta: '))
b = int(input('Digite o valor da Segunda reta: '))
c = int(input('Digite o valor da terceira reta:'))

if (a + b) > c and (a+c) > b and (c+b) > a :
    print('É possivel fazer um triângulo')

else:
    print('Não é possivel formar um triangulo')

