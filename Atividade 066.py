# Crie um programa que leia varios numeros inteiros pelo teclado.
# O programa só vai parar quando digitar o valor 999, Que é a condição de parada
# No final mostre quantos numeros foram digitados e qual foi a soma entre eles

soma = qnt = 0
while True:
    num = int(input('Digite um valor'))
    if num == 999:
        break
    qnt += 1
    soma = soma + num
print(f'A Quantidade de numero digitados foi {qnt}\n'
      f'E a Soma deles foi {soma}')
