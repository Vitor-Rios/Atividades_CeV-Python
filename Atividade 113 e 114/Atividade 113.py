# Reescreva a função leiaint() que fizemos no desafio 104,
# incluindo agora a possibilidade dda digitação de um numero de tipo inválido.
# Aproveite e crie tambem uma função leiaFloat() com a mesma funcionabilidade.

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31m ERRO, Digite um número inteiro válido. \033[m')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida.')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31m ERRO, Digite um número real válido. \033[m')
        except KeyboardInterrupt:
            print('Entrada de dados interrompida.')
            return 0
        else:
            return n


n1 = leiaInt('Digite um valor inteiro: ')
n2 = leiaFloat('Digite um valor real: ')
print(f' O Valor inteiro digitado foi {n1} e o real foi {n2}')
