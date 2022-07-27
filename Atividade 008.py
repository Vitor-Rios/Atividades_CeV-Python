# Escreva um programa que leia um valor em metros e o exiba convertido em centrimetro e milimetros

met = float( input( 'Digite o valor em Metros:'))
cent = met*100
mil = met*1000

print(f'O Valor digitado foi: {met}m \n'
      f'Em centímetros é: {cent} cm \n'
      f'Em milímetros é: {mil}mm')

