#Crie um programa que gerencia o aproveitamento de um jogador de futebol.
#O programa vai ler o Nome do jogador e quantas partidas ele jogou.
#Depois vai ler a quantidade de gols feito em cada partida.
#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

apro = {}
gols = []
apro['nome'] = str(input('Digite o Nome do Jogador: '))
part = int(input(f'Quantas Partidas o jogador {apro["nome"]} Jogou?'))
for c in range(0,part):
    gols.append(int(input(f'Quantos gols na Partida {c+1}?')))
apro['gols'] = gols[:]
apro['total'] = sum(gols)
print('-=-'*15)
for c,v in apro.items():
    print(f'O campo {c} tem o valor {v}')
print('-=-'*15)
print(f'O jogador {apro["nome"]} Jogou {part} partidas')
for c in enumerate(gols):
    print(f'Na partida {c[0]+1}, fez {c[1]} gols')

