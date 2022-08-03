# Crie um programa que leia o ano de nascimento de sete pessoas,
# no final mostre quantas pessoas ainda não atingiram a maioridade e quantas ja são maiores.

maior = 0
menor = 0

for c in range(0, 7):
    idade = int(input('Digite a Idade: '))
    if idade >= 22:
        maior = maior + 1
    elif idade < 22:
        menor = menor + 1

print(f'Maior idade {maior}\n'
      f'Menor Idade {menor}')
