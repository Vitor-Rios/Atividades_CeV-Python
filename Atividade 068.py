# Faça um programa que jogue par ou impar com o computador.
# O jogo só sera iterrompido quando o jogador perder.
# Mostrando o total de vitorias consecutivas que ele conquistou no final do jogo

import random
pont = 0
while True:
    jogador = int(input('Escolha um Numero: '))
    opc = ' '
    computador = random.randint(0, 10)
    final = (computador + jogador) % 2
    while opc not in 'PI':
        opc = str(input('Escolha Par [P] ou Ímpar [I]')).upper().strip()
    if opc == 'P':
        if final == 0:
            print(f'Você escolheu {jogador} e o computador {computador}')
            print('O Resultado foi Par, Você Ganhou')
            pont = pont + 1
        else:
            print(f'Você escolheu {jogador} e o computador {computador}')
            print(f'O Resultado foi Impar, Voce Perdeu, e ganhou {pont} seguidas')
            break
    if opc == 'I':
        if final ==1:
            print(f'Você escolheu {jogador} e o computador {computador}')
            print('O Resultado foi Ímpar, Você Ganhou')
            pont = pont + 1
        else:
            print(f'Você escolheu {jogador} e o computador {computador}')
            print(f'O Resultado foi Par, Você Perdeu, e ganhou {pont} seguidas')
            break




