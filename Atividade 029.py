# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A Multa vai custar R$7,00 por cada KM acima do limite

km = float(input('Qual a velocidade do Carro?: '))


if km > 80:
    multa = 7.00 * (km - 80)
    print(f'Você execeu o limite de velocidade e deverá pagar uma multa de: R$ {multa:.2f}')

else:
    print('Boa Viagem')
