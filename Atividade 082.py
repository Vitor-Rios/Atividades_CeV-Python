# Crie um programa que vai ler varios numero e colocar em uma lista. Depois disso, crie duas listas extras que vão
# conter apenas os valores pares e os valores impares digitados, respectivamente. Ao final, mostre o conteúdo das
# tres listas geradas.

lista = []
par = []
impar = []

while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    opc = ' '
    while opc not in 'YN':
        opc = input('Deseja adicionar outro valor? [Y]/[N]: ').upper().strip()
    if opc == 'N':
        break
pos = 0
while pos < len(lista):
    if lista[pos] % 2 == 1:
        impar.append(lista[pos])
        pos += 1
    else:
        par.append(lista[pos])
        pos += 1
print(f' Valores da lista {lista}\n'
      f'Pares {par}\n'
      f'impar {impar}')
