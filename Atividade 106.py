# Faça um mini programa que utilize o interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra "FIM", o programa se encerrará.


def duvida(txt):
    help(txt)


comando = ''
while True:
    comando = str(input('Digite o comando ou biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        duvida(comando)
