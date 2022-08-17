# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior numero no dado

import random
import time
import operator

ranking = []
bib = {'Jogador 1': random.randint(1, 6),
       'Jogador 2': random.randint(1, 6),
       'Jogador 3': random.randint(1, 6),
       'Jogador 4': random.randint(1, 6)}
for c, v in bib.items():
    print(f'O {c} tirou {v} no dado')
    time.sleep(1)
ranking = sorted(bib.items(), key=operator.itemgetter(1), reverse=True)
print('-=-' * 15)
for p, j in enumerate(ranking):
    print(f'{p + 1}o Lugar Ficou {j[0]} que tirou {j[1]} no dado')
    time.sleep(1)
