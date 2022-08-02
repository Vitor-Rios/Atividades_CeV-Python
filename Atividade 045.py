# Crie um programa que faça o computador jogar JoKenPô com você

import random
player = int(input('''Selecione
1 - Pedra
2 - Papel
3 - tesoura
'''))

listap = ['PEDRA', 'PAPEL', 'TESOURA']
lista = ['PEDRA', 'PAPEL', 'TESOURA']
random.shuffle(lista)

if player == 1 and lista[0] == 'PEDRA':
    print(f'Você escolheu {listap[0]} e o computador {lista[0]}')
    print('EMPATE')
elif player == 1 and lista[0] == 'PAPEL':
    print(f'Você escolheu {listap[0]} e o computador {lista[0]}')
    print('Computador Ganhou')
elif player == 1 and lista[0] == 'TESOURA':
    print(f'Você escolheu {listap[0]} e o computador {lista[0]}')
    print('Você ganhou')
elif player == 2 and lista[0] == 'PEDRA':
    print(f'Você escolheu {listap[1]} e o computador {lista[0]}')
    print('Você ganhou')
elif player == 2 and lista[0] == 'PAPEL':
    print(f'Você escolheu {listap[1]} e o computador {lista[0]}')
    print('EMPATE')
elif player == 2 and lista[0] == 'TESOURA':
    print(f'Você escolheu {listap[1]} e o computador {lista[0]}')
    print('Computador Ganhou')
elif player == 3 and lista[0] == 'PEDRA':
    print(f'Você escolheu {listap[2]} e o computador {lista[0]}')
    print('Computador Ganhou')
elif player == 3 and lista[0] == 'PAPEL':
    print(f'Você escolheu {listap[2]} e o computador {lista[0]}')
    print('Você ganhou')
elif player == 3 and lista[0] == 'TESOURA':
    print(f'Você escolheu {listap[2]} e o computador {lista[0]}')
    print('Empate')
else:
    print('Opção invalida')
