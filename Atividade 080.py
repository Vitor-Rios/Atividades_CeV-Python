# Crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os em uma lista,
# ja na posição correta de inserção (sem usar o sort()).
# No final mostre a lista ordenada na tela.

lista = []
for c in range(0, 5):
    num = int(input('Digite um numero: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos = pos + 1

print(lista)
