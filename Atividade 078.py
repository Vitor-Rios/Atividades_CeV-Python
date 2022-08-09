# Faça um programa que leia 5 valores numericos e guarde-os em uma lista
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
for c in range(0, 5):
    lista.append(input('Digite o Valor: '))

print(lista)
print(f'O Maior valor digitado foi {max(lista)} e foi digitado na posição {lista.index(max(lista))}\n'
      f'O Menor valor digitado foi {min(lista)} e foi digitado na posição {lista.index(min(lista))}')
