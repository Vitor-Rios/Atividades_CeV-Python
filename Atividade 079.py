# Crie um programa onde o usuário possa digitar varios valores numericos e cadastre-os em uma lista.
# Caso o numero ja exista lá dentro, ele não sera adicionado.
# No final, serão exibidos todos os valores unicos digitados, em ordem crescente.

numeros = []

while True:
    opc = ' '

    num = int(input('Digite um numero: '))

    if num not in numeros:
        numeros.append(num)
    else:
        print('Esse numero ja estava cadastrado, então não foi adicionado.')

    while opc not in 'YN':
        opc = input('Deseja continuar? [Y] / [N]').upper()

    if opc == 'N':
        break

numeros.sort()
print(numeros)
