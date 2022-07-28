# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
# EX: Ana Maria de Souza
# primeiro: Ana
# ultimo: Souza

nome = input('Digite seu nome Completo:')
nome = nome.split()

print(f'Seu primeiro nome é {nome[0]} e seu ultimo nome é {nome[-1]}')
