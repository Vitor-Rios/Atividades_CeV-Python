# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 termos da progressão usando a estrutura while.

termo = int(input('Digite o Primeiro Termo: '))
razão = int(input('Digite a Razão'))
cont = 1

while cont <= 10:
    print(termo, end=' ')
    termo = razão + termo
    cont = cont + 1
