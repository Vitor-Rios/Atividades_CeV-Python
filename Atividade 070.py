# Crie um programa que leia o nome e o preço de varios produtos.
# O Programa deverá perguntar se o usuário vai continuar.
# No final mostre:
# A - Qual é o total gasto na compra
# B - quantos produtos custam mais de R$ 1000.
# C- Qual é o nome do produto mais barato

total = caro = barato = cont = 0
prodbarato = ''
while True:
    prod = str(input('Digite o nome do produto: '))
    val = int(input('Digite o Valor do Produto: R$ '))
    total = total + val
    cont = cont + 1
    if val > 1000:
        caro = caro + 1
    if cont == 1 or val < barato:
        barato = val
        prodbarato = prod
    opc = ' '
    while opc not in 'NS':
        opc = input('Deseja continuar? [S] / [N]:').upper().strip()
    if opc == 'N':
        break

print(f'''
Total gasto na compra R$: {total}
{caro} produtos custam mais de R$ 1000.
O nome do produto mais barato é {prodbarato} custando R$: {barato}
''')
