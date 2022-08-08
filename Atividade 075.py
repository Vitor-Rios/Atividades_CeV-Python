# Desenvolva um programa que leia Quatro valores pelo teclado e guarde-os em uma tupla. no final mostre:
# A - Quantas vezes apareceu o valor 9
# B - Em que posição foi digitado o primeiro valor 3
# C - Quais foram os numero pares

numeros = (int(input('Digite um numero: ')),
           int(input('Digite mais um numero: ')),
           int(input('Digite outro: ')),
           int(input('Digite só mais um: ')))

print(f'O numero 9 foi digitado: {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O numero 3 apareceu pela primeira vez na posição: {numeros.index(3)+1}')
else:
    print('Não tem numero 3 na Tupla.')
print(f'Os numero pares digitados foram: ',end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
