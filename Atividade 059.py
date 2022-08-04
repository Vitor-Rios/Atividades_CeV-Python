# Crie um programa que leia dois valores e mostre um menu na tela
# [1] - Somar
# [2] - Multiplicar
# [3] - Maior
# [4] - Novos numeros
# [5] - Sair do programa

opc = 0

while opc != 5:
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o Segundo Valor: '))
    print('''Escolha uma opção:
    # [1] - Somar
    # [2] - Multiplicar
    # [3] - Maior
    # [4] - Novos numeros
    # [5] - Sair do programa''')
    opc = int(input('Opção: '))

    while opc != 4 and opc != 5:
        if opc == 1:
            soma = valor1 + valor2
            print(f'O Resultado da soma é {soma}')
            opc = int(input('Digite outra opção: '))
        if opc == 2:
            mult = valor1 * valor2
            print(f'O Resultado da Multiplicação é:{mult}')
            opc = int(input('Digite outra opção: '))
        if opc == 3:
            lista = [valor1, valor2]
            print(f'O Maior valor entre os dois digitados é {max(lista)}')
            opc = int(input('Digite outra opção: '))
        else:
            print('Opção inválida')
            opc = 4
