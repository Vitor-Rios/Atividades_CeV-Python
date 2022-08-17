# Faça um programa que tenha um função chamada area(),
# que receba as dimensões de um terreno retangular (largura e comprimento)
# e mostre a area do terreno.

def area(l, c):
    a = l * c
    print(f'A área de {l} x {c} é {a}m²')


l = float(input('Digite a Largura (m): '))
c = float(input('Digite o Comprimento (m): '))

area(l, c)
