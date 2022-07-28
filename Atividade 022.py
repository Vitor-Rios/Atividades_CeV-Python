# 022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minusculas
# Quantas letras ao todo (sem considerar espaços)
# quantas letras tem o primeiro nome.

nome = input('Digite Seu nome: ')
dividido = nome.split()


print(f'O Nome com letras Maiusculas: {nome.upper()}')
print(f'O Nome com letras Minusculas: {nome.lower()}')
print(f'Quantidade de Letras sem considerar espaços: {len(nome.replace(" ",""))}')
print(f'o primeiro nome tem {len(dividido[0])} Letras')

