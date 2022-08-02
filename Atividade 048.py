# Faça um programa que calcule a soma entre todos os numeros
# impares que são multiplos de tres e que se encontram no intervalo de 1 ate 500

soma = 0
for c in range(0, 500):
    if c % 2 == 1 and c % 3 == 0:
        soma = soma + c

print(soma)
