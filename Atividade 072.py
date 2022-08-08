# Crie um programa que tenha um Tupla totalmente preenchida com uma contagem por extensão.
# De 0 até 20.
# Seu programa deverá ler um numero pelo teclado (ente 0 e 20) e mostra-lo por extenso

cont = ('ZERO', 'UM', 'DOIS', 'TRES', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE',
        'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')

num = ''
while num not in (0,20):
    num = int(input('Informe um numero entre 0 a 20: '))

print(f'VOCÊ DIGITOU O NUMERO: {cont[num]}')





