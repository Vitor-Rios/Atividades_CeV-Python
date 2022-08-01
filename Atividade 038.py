# Escreva um programa que leia dois numero inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O Segundo valor é maior
# Não existe valor maior, os dois são iguais.

val1 = int(input('Digite o primeiro valor: '))
val2 = int(input('Digite o segundo valor: '))

if val1 > val2:
    print(f'o Primeiro valor {val1} é maior que {val2}')

elif val2 > val1:
    print(f'O Segundo valor {val2} é maior que {val1}')

else:
    print('Os Valores são iguais')

