# Aprimore o desafio anterior, mostrando no final:
# A - A soma de todos so valores pares digitados.
# B - A soma dos valres da terceira coluna
# C - O maior valor da segunda linha

lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somat = soma = 0

for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c] = int(input(f'Digite o valor [{l, c}]:'))
        if lista[l][c] % 2 == 0:
            soma = soma+lista[l][c]
for l in range(0,3):
    for c in range(0,3):
        print(f'[{lista[l][c]:^5}]', end='')
    print()
somat = lista[0][2] + lista[1][2] + lista[2][2]

print(f'A soma dos valores pares é: {soma}')
print(f'A soma dos valores da terceira coluna é: {somat}')
print(f'O Maior valor da segunda linha é: {max(lista[1])}')



