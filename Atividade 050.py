# desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for impar, desconsidere-o

num = 0

for c in range(0, 6):
    val = int(input('Digite o Valor inteiro: '))
    if val % 2 == 0:
        num = num + val

print(num)
