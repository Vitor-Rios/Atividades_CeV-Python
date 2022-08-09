# Crie um programa que vai ler varios numeros e colocar em uma lista.
# depois disso mostre:
# A - Quantos numeros foram digitados.
# B - A Lista de valores, ordenada de forma decrescente.
# C - se o valor 5 foi digitado e esta ou não na lista.

lista = []
qtd = 0
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    qtd = qtd + 1
    opc = ' '
    while opc not in 'YN':
        opc = input('Deseja adicionar outro valor? [Y] / [N]').upper().strip()
    if opc == 'N':
        break
lista.sort(reverse=True)
print(f'A Lista digitada possui {qtd} numeros \n'
      f'{lista}')
if 5 in lista:
    print(f'O numero 5 foi digitado: e esta na posição {lista.index(5)}')
else:
    print('O numero 5 não foi digitado.')
