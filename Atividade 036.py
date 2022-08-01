# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
# O Programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o empréstimo sera negado.

casa = float(input('Qual o Valor da casa? '))
salario = float(input('Qual o Valor do salário? '))
tempo = float(input('Vai pagar em quantos anos? ')) * 12
prest = casa / tempo

if prest <= (salario * 30 / 100):
    print(f'O Valor da prestação será {prest}')
else:
    print('O valor da prestação ultrapassa 30% do salário')




