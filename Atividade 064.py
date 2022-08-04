# Crie um programa que leia varios numeros inteiros pelo teclado.
# O programa só vai parar quando o usuários digitar o valor 999
# que é a condição de parada. no Final mostre quantos numeros foram digitados.
# e Qual foi a soma entre eles.
# desconsiderando o flag (999)


num = int(input('Digite um numero inteiro: '))
totnum = 0
somnum = 0

while num != 999:

    totnum = totnum + 1
    somnum = somnum + num
    num = int(input('Digite outro numero: '))


print(f'O Total de numeros Digitados foi {totnum} e a soma de todos eles foi {somnum}')
