# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

nome = input('Digite o nome da cidade: ')
separado = nome.capitalize().split()

print('Santo' in separado[0])

