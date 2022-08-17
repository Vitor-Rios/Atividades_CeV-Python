# Crie um programa que leia o nome, sexo e idade de varias pessoas, Guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista.
# No final, mostre:
# A - Quantas pessoas foram cadastradas
# B - A Média de idade do grupo
# C - Uma lista com todas as mulheres
# D - Uma lista com todas as pessoas com idade acima da média

pessoas = {}
temp = []
soma = cont = mul = 0
while True:
    nome = input('Digite o nome: ')
    pessoas['nome'] = nome
    sexo = input('Digite o Sexo [M][F]: ').upper()
    pessoas['sexo'] = sexo
    idade = int(input('Digite a Idade: '))
    pessoas['idade'] = idade
    soma = soma + idade
    temp.append(pessoas.copy())
    opc = ' '
    while opc not in 'YN':
        opc = input('Deseja adicionar outra pessoa?: ').upper().strip()
    if opc == 'N':
        break
med = soma / len(temp)
print(temp)
print(f'A - Foram cadastrados {len(temp)} pessoas')
print(f'B - A média de idade é {med}')
print('C - A lista com todas as mulheres: ', end='')
for c in temp:
    if c['sexo'] == 'F':
        print(c['nome'], end=' ')
print()
print('D - A Lista com idade maior que a média: ', end='')
for c in temp:
    if c['idade'] >= med:
        print(c['nome'], end=' ')
