# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
# Para salários acima de R$1.250,00 calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Digite o Valor do salário: '))

if salario > 1250.00:
    print(f'O Valor do salário com aumento é de {salario + ((salario * 10) /100)}')
else:
    print(f'O Valor do salário com aumento é de {salario + ((salario * 15) / 100)}')


