# Crie um programa onde o usuário possa digitar sete valores numericos
# e cadastre-os em uma lista unica que mantenha separados os valores pares e impares.
# No final, mostre os valores pares e impares em ordem crescente

lista = [[], []]

for c in range(0, 7):
    num = int(input(f'Digite o {c + 1} valor: '))
    if num % 2 == 1:
        lista[1].append(num)
    else:
        lista[0].append(num)
lista[0].sort()
lista[1].sort()
print(f'Os numero Pares digitados foram: {lista[0]}')
print(f'Os numero impares digitados foram: {lista[1]}')

