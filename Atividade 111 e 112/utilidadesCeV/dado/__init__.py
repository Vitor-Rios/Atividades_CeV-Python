def leiaDinheiro(dado):
    while True:
        valor = input(dado).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'Valor {valor} é um preço invalido ')
        else:
            return float(valor)

