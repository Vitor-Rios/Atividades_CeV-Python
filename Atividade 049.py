# refaça o desafio 9, mostrando a tabuada de um numero que o usuário escolher, só que agora utilizando o lçao for.

n = int(input('Digite um numero inteiro: '))

for c in range(0, 10 + 1):
    print(f'{n}x{c} = {n * c}')
