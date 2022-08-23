# Faça um pgorama que tenha um função chamada ficha(),
# Que receba dois parametros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome, gols='0'):
    if nome == '':
        if gols == '':
            print(f'O jogador <Desconhecido> marcou 0 Gols.')
        else:
            print(f'O jogador <Desconhecido> marcou {gols} Gols.')
    elif nome != '':
        if gols == '':
            print(f'O Jogador {nome} marcou 0 Gols.')
        else:
            print(f'O Jogador {nome}, marcou {gols} Gols.')


nome = str(input('Digite o nome do Jogador: ')).strip()
gols = str(input('Digite o numero de gols: ')).strip()
ficha(nome, gols)
