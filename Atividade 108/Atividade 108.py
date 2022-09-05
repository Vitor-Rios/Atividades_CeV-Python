# Adapte o desafio 107, criando uma função adicional chamada moeda(),
# que consiga mostrar os valores como um valor monetário formatado.

import moeda

num = float(input('Digite um numero '))
dec = float(input('Deseja Aumentar e Diminuir quantos %? '))

print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'Aumentando {dec} % do numero {moeda.moeda(num)} é {moeda.moeda(moeda.aumentar(num,dec))}')
print(f'Diminuindo {dec} % do numero {moeda.moeda(num)} é {moeda.moeda(moeda.diminuir(num,dec))}')
