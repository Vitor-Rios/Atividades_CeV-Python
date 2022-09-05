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
