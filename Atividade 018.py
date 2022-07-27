# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

import math

entrada = float(input('Digite o valor do angulo: '))
valor = math.radians(entrada)
sen = math.sin(valor)
cos = math.cos(valor)
tan = math.tan(valor)

print (f'O Valor de Seno do Angulo de {entrada} é {sen:.2f} \n'
       f'O Valor de Cosseno do Angulo de {entrada} é {cos:.2f} \n'
       f'O Valor da Tangente do Angulo de {entrada} é {tan:.2f}')



