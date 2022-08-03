# Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo

num = int(input('Digite o numero: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        total = total + 1

print(f'o Numero {num} é divisivel {total} vezes portanto')

if total == 2:
    print('Ele é primo')
else:
    print('Ele não é primo')
