# Escreva um programa que leia um numero n inteiro qualquer
# e mostre na tela os n primeros elementos de uma sequencia de fibonacci.


num = int(input('Quantos termos quer mostrar?: '))
t1 = 0
t2 = 1
repet = 3

print(f'{t1} {t2}', end=' ')

while repet <= num:
    t3 = t1 + t2
    print(f'{t3}', end=' ')
    t1 = t2
    t2 = t3
    repet = repet + 1

print('Fim')

