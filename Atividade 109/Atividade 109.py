# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parametro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108

import moeda

num = float(input('Digite um numero '))
dec = float(input('Deseja Aumentar e Diminuir quantos %? '))

print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num,True)}')
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num,True)}')
print(f'Aumentando {dec} % do numero {moeda.moeda(num)} é {moeda.aumentar(num,dec,True)}')
print(f'Diminuindo {dec} % do numero {moeda.moeda(num)} é {moeda.diminuir(num,dec,True)}')
