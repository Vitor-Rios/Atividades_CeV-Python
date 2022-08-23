# Crie um programa que tenha a função leiaint(),
# Que vai funcionar de forma semelhante a função input() do python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex:
# n = leiaint('Digite um n')

def leiaInt(txt):
    while True:
        n = str(input(txt))
        if n.isnumeric():
            return n
        else:
            print('Erro, Digite um numero valido')


n = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}')
