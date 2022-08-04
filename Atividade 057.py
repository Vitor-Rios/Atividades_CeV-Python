# Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores "M" ou "F".
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite o Sexo M/F:'))

while sexo not in 'MmFf':
    sexo = str(input('Informação incorreta, Digite novamente o sexo'))

print('opção válida')
