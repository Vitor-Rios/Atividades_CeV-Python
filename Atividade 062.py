# Melhore o desafio 061, perguntando para o usuario se ele quer mostrar mais alguns termos.
# O Programa encerra quando ele disser que quer mostrar 0 termos.

opc = 1
while opc != 0:

    termo = int(input('Digite o Primeiro Termo: '))
    raz = int(input('Digite a Razão'))
    cont = 1

    while cont <= 10:
        print(termo, end=' ')
        termo = raz + termo
        cont = cont + 1

    opc = int(input('\nQuer mostrar mais algum termo?, Caso queira finalizar é só pressionar "0": '))
