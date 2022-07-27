# Crie um programa que leia um numero real qualquer pelo teclado e mostre sua porção inteira
# (exemplo Digite: 6.127 / Mostre:6) biblioteca math

import math

x = float(input('Digite um valor real (Ex: 12,45): '))
resultado = math.trunc(x)

print (f'O numero inteiro digitado foi: {resultado}')
