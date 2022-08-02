# Desenvolva uma lógica que leia o peso e altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# acima de 40: Obesidade Mórbida

altura = float(input('Digite sua Altura: '))
peso = float(input('Digite seu Peso: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print(f'IMC de {imc} Abaixo do peso')
elif 18.5 <= imc < 25:
    print(f'IMC de {imc} é Ideal')
elif 25 <= imc < 30:
    print(f'IMC de {imc} é Sobrepeso')
elif 30 <= imc < 40:
    print(f'IMC de {imc} é Obesidade')
else:
    print(f'IMC de {imc} é Obesidade Mórbida')
