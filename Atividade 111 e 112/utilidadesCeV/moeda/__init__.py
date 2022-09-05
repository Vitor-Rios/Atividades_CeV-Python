def aumentar(num=0, quantidade=0, formatado=False):
    r = num + ((num * quantidade) / 100)
    if formatado:
        return moeda(r)
    else:
        return r


def diminuir(num=0, quantidade=0, formatado=False):
    r = num - ((num * quantidade) / 100)
    if formatado:
        return moeda(r)
    else:
        return r


def dobro(num=0, formatado=False):
    r = num * 2
    if formatado:
        return moeda(r)
    else:
        return r


def metade(num=0, formatado=False):
    r = num / 2
    if formatado:
        return moeda(r)
    else:
        return r


def moeda(num=0):
    return f'R$ {num:.2f}'.replace('.', ',')


def resumo(num=0, quantidade=0):
    print('~' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('~' * 30)
    print(f'{"Preço Analisado:":<16} {moeda(num):>13}')
    print(f'{"Dobro do preço:":<16} {dobro(num,True):>13}')
    print(f'{"Metade do preço:":<16} {metade(num,True):>13}')
    print(f'{quantidade:.0f}{" % de Aumento:":<16} {aumentar(num, quantidade,True):>11}')
    print(f'{quantidade:.0f}{" % de Redução:":<16} {diminuir(num,quantidade,True):>11}')
    print('~'*30)
