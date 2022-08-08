# Crie um programa que vai gerar 5 numeros aleatórios e colocar em um tupla.
# Depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estão na tupla.
import random
numeros = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))

print(f'Os numeros gerados foram: {numeros}')
print(f'O Maior valor gerado foi: {max(numeros)}')
print(f'O Maior valor gerado foi: {min(numeros)}')
