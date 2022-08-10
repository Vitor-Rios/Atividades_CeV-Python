# Crie um programa que leia o nome e duas notas de varios alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente

lista = []
while True:
    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a Primeira nota: '))
    nota2 = float(input('Digite a Segunda nota: '))
    med = (nota1 + nota2) / 2
    lista.append([nome,[nota1,nota2],med])
    opc = input('Deseja adicionar outro Aluno? [Y]/[N]:').upper().strip()
    if opc == 'N':
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for n,a in enumerate(lista):
    print(f'{n:<4}{a[0]:<10}{a[2]:>8}')
while True:
    cod = int(input('Deseja ver a nota de qual aluno? (999 Interrompe): '))
    if cod == 999:
        break
    if cod <= len(lista):
        print(f'As notas Aluno {lista[cod][0]} foram: {lista[cod][1]}')

