# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo.
# Calcule e mostre a hipotenusa.

from math import hypot

x = float(input('Digite o Cateto Maior: '))
y = float(input('Digite o Cateto Menor: '))

z = hypot(x,y)

print (f'{z:.2f}')
