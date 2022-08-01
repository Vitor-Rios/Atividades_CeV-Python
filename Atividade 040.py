# Crie um programa que leia duas notas de um aluno e calcule sua media,
# mostrando uma mensagem no final, de acordo com a media atingida:
# Média abaixo de 5.0 REPROVADO
# Média entre 5.0 e 6.9 RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a Segunda nota: '))

if (nota1 + nota2) / 2 < 5.0:
    print(f'Nota {(nota1 + nota2) / 2} Reprovado')

elif 5 <= (nota1 + nota2) / 2 < 6.9:
    print(f'{(nota1 + nota2) / 2}Recuperação')

else:
    print(f'Nota {(nota1 + nota2) / 2} APROVADO')
