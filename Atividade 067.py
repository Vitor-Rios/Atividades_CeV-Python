# Faça um programa que mostre a tabuada de varios numeros, um de cada vez, Para cada valor digitado pelo usuário.
# O Programa sera interrompido quando o numero solicitado for negativo.

while True:
    num = int(input('Digite o numero para saber a Tabuada, ou Digite um numero negativo para sair: '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num}x{c} = {c * num}')
