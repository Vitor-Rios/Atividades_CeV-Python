# Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e menor valores lidos.
# O programa deve perguntar se ele quer ou não continuar a digitar valores


maior = menor = soma = cont = 0
c = 'y'
while c in 'Yy':
    num = int(input('Digite um Valor: '))
    soma = soma + num
    cont = cont + 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    c = str(input('Deseja Digitar outro valor? [Y] / [N]: '))

med = soma / cont

print(f'''A soma dos numero digitados é: {soma}
A Média dos numero digitados é {med}
O Maior numero digitado foi {maior}
O Menor numero digitado foi {menor}''')
