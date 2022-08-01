# Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversão:
# 1 para binario
# 2 para octal
# 3 para hexadecimal

num = int(input('Digite um valor: '))
print('''-=--=--=--=--=--=--=--=--=--=--=--=-
Digite qual tipo de conversão deseja:
    1 - Binário
    2 - Octal'
    3 - Hexadecimal:
-=--=--=--=--=--=--=--=--=--=--=--=''')
valor = int(input())

if valor == 1:
    print(f'o Valor {num} convertido para binário é {bin(num)[2:]}')

elif valor == 2:
    print(f'o Valor {num} Convertido para Octal é {oct(num)[2:]}')

elif valor == 3:
    print(f'O valor {num} Convertido para Hexadecimal é {hex(num)[2:]}')
else:
    print('Nenhuma opção Válida selecionada.')