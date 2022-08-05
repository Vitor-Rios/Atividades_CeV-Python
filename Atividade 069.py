# Crie um programa que leia a idade e o sexo de varias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuario quer ou não continuar.
# No final mostre:
# A - Quantas pessoas tem mais de 18 anos.
# B - Quando homem foram cadastrados.
# C - Quantas mulheres tem menos de 20 anos
maioridade = qnthomem = mulhermenoridade = 0
while True:
    idade = int(input('Digite a idade: '))
    opc = ' '
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M] / [F]')).upper()
    while opc not in 'NY':
        opc = str(input('Deseja continuar? [Y] / [N]')).upper()
    if idade > 18:
        maioridade = maioridade + 1
    if sexo in 'Mm':
        qnthomem = qnthomem + 1
    if sexo in 'Ff' and idade < 20:
        mulhermenoridade = mulhermenoridade + 1
    if opc in 'Nn':
        break
print(f'''
# A - Quantas pessoas tem mais de 18 anos é {maioridade}
# B - Quando homem foram cadastrados {qnthomem}
# C - Quantas mulheres tem menos de 20 anos {mulhermenoridade}
''')


