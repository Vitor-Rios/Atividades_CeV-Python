# Refaça o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
# Equilátero: todos os lados iguais
# Isóceles: dois lados iguais
# Escaleno: todos os lados diferentes


a = int(input('Digite o valor da primeira reta: '))
b = int(input('Digite o valor da Segunda reta: '))
c = int(input('Digite o valor da terceira reta:'))

if (a + b) > c and (a + c) > b and (c + b) > a:
    print('É possivel fazer um triângulo')

    if a == b == c:
        print('é um triangulo equilátero.')
    elif a != b != c != a:
        print('é um triangulo Escaleno')
    else:
        print('é um triangulo Isóceles')

else:
    print('Não é possivel formar um triangulo')
