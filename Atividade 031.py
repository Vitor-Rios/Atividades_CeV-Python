# Desenvolva um programa que pergunte a distancia de uma viagen em KM,
# Calcule o preço da pasasgem, cobrando R$ 0,50 por KM para viagens de até 200KM e R$0,45 para viagens mais longas.

km = float(input('Digite a Distancia da Viajem: '))

if km <= 200:
    valor = km * 0.50
    print(f'O Valor total da viajem é de: R$ {valor:.2f}')

else:
    valor = km * 0.45
    print(f'O Valor da viajem é de: R$ {valor:.2f}')
    