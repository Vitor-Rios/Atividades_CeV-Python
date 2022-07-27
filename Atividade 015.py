# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 po dia e R$0.15 por KM rodado


km = float(input('Qual a KM percorrida?: '))
dias = float(input('Quantos dias o carro foi alugado?: '))

total = (km * 0.15) + (dias * 60)

print(f'O Total a ser pago será R$: {total:.2f}')
