# Cria um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade().
# Faça tambem um programa que importe esse módulo e use algumas dessas funções

import moeda

num = float(input('Digite um numero '))
dec = float(input('Deseja Aumentar e Diminuir quantos %? '))

print(f'O dobro de {num} é {moeda.dobro(num)}')
print(f'A metade de {num} é {moeda.metade(num)}')
print(f'Aumentando {dec} do numero {num} é {moeda.aumentar(num,dec)}')
print(f'Diminuindo {dec} do numero {num} é {moeda.diminuir(num,dec)}')