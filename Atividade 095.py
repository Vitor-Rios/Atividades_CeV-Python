# Aprimore o Desafio 093 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

apro = {}
gols = []
time = []

while True:
    apro.clear()
    gols.clear()
    nome = str(input('Digite o Nome do Jogador: '))
    apro['nome'] = nome
    part = int(input(f'Quantas Partidas o jogador {apro["nome"]} Jogou?'))
    apro['partidas'] = part
    if part != 0:
        for c in range(0, part):
            gols.append(int(input(f'Quantos gols na Partida {c + 1}?')))
        apro['gols'] = gols[:]
        apro['total'] = sum(gols)
    time.append(apro.copy())

    opc = ' '
    while opc not in 'YN':
        opc = input('Deseja adicionar outro jogador?: ').upper().strip()
    if opc == 'N':
        break
print('-=-' * 20)
print(f'{"COD":<4} {"NOME":<15}{"PARTIDAS":<15}{"GOLS":<8}{"TOTAL":<8}')
for k, v in enumerate(time):
    print(f'{k:<4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    print('-=-' * 20)
    busca = int(input('Digite o Cod do jogador que quer visualizar (999 encerra): '))
    if busca == 999:
        break
    if busca > len(time):
        print('-=-' * 20)
        print(f' ERRO , não existe o jogador com o Código {busca}')
    else:
        print('-=-' * 20)
        print(f'Levantamento do Jogador {time[busca]["nome"]}')
        for c in enumerate(time[busca]["gols"]):
            print(f'Na partida {c[0] + 1}, fez {c[1]} gols')
