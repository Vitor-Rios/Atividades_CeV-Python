# Desenvolva um programa que leia o nome, idade, sexo de 4 pessoas. No final do programa, mostre:
# A Media de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres tem menos de 20 anos.

somaidade = 0
medidade = 0
nomevelho = ''
idadevelho = 0
totmulher = 0

for c in range(1, 5):
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo M / F: '))
    somaidade = idade + somaidade
    if c == 1 and sexo in 'Mm':
        idadevelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > idadevelho:
        idadevelho = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher = totmulher + 1

medidade = somaidade / 4
print(f'A média de idade do grupo é: {medidade}\n'
      f'O nome do homem mais velho é {nomevelho} e a idade dele é {idadevelho}\n'
      f'{totmulher} Mulheres Tem menos de 20 anos')
