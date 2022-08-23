# Crie um programa que tenha uma função fatorial() que receba dois parametros:
# O primeiro que indique o numero a calcular e o outro chamado show,
# que sera um valor lógico (Opcional) indicando se será mostrado ou não na tela o processo de calculo do fatorial


def fatorial(num, show=False):
    """
    -> Calcula Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (Opcional), Mostrar ou não a conta
    :return: Valor do Fatorial de n.
    """
    tot = 1
    for c in range(num, 0, -1):
        tot *= c
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return tot


print(fatorial(5, True))
help(fatorial)

