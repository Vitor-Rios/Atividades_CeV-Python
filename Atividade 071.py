# Crie um programa que simule o funcionamento de um caixa eletronico.
# No inicio, pergunte ao usuário qual sera o valor a ser sacado (numero inteiro)
# O programa vai informar quantas cedulas de cada valor serão entregues.
# OBS - considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1

saque = int(input('Qual o Valor a ser sacado?: R$ '))
total = saque
ced = 50
qtdced = 0
while True:
    if total >= ced:
        total = total - ced
        qtdced = qtdced + 1
    else:
        print(f'Vai receber {qtdced} de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        qtdced = 0
        if total == 0:
            break






