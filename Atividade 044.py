# Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de
# pagamento: A vista dinheiro e cheque: 10% de desconto A vista no cartão: 5% de desconto Em até 2x no cartão: Preço
# normal 3x ou mais no cartão: 20% de juros

valor = float(input('Digite o valor do produto R$ '))
print("""
-===========================-
Digite como vai ser pago:
1 - A Vista no Dinheiro ou Cheque
2 - A Vista no Cartão
3 - Em até 2x no Cartão
4 - Em 3x ou mais no cartão
-===========================-
""")
opc = int(input('Opção: '))

if opc == 1:
    print(f'O Valor a ser pago com 10% de desconto é R$ {valor - (valor * 10 / 100)}')
elif opc == 2:
    print(f'O Valor a ser pago a Vista no cartão com 5% de desconto é R$ {valor - (valor * 5 / 100)}')
elif opc == 3:
    print(f'O Valo a ser pago em 2x no cartão é R$ {valor}, em 2x de {valor / 2}')
elif opc == 4:
    pcl = int(input('Vai parcelar em quantas vezes?'))
    valor2 = valor + (valor * 20/100)
    print(f'O valor a ser pago é de {valor2}, em {pcl} de {valor2 / pcl}')
else:
    print('Opção invalida')
