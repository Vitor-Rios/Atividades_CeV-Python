# faça um programa que leia a largura e a altura de uma parede em metros
# calcule sua area e a quantidade de tinta necessaria para pinta-la
# sabendo que cada litro de tinta pinta uma area de 2M²

altura = float(input('Digite a Altura da Parede em Metros "m": '))
largura = float(input('Digite a Largura da Parede em Metros "m": '))

area = altura * largura
tinta = area / 2

print(f'O Valor Total é de {area} M² \n'
      f'A quantidade de Tinta necessária é de {tinta} L')
