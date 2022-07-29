# Fala um programa que leia tres numeros e moste qual é o maior e qual é o menor

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))

lista = [num1, num2, num3]

print(f'o Maior valor digitado foi: {max(lista)}')
print(f'o Menor valor digitado foi: {min(lista)}')
