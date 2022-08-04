# Faça um programa que leia um numero e mostre o seu fatorial

num = int(input('Digite o numero: '))
print(f'Calculando {num}! = ', end=' ')
f = 1
for num in range(num, 0, -1):
    print(f'{num}', end=' ')
    print(f'x' if num > 1 else '=', end=' ')
    f = f * num

print(f)
