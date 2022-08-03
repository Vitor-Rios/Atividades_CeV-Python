# Faça um programa que leia o peso de cinco pessoas.
# No final mostre qual foi o maior e o menor peso lidos.

peso = float(input('Digite o Peso'))
maior = peso
menor = peso

for c in range(0,4):
    peso = float(input('Digite o Peso'))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print(f'Maior peso {maior}\n'
      f'Menor peso {menor}')



