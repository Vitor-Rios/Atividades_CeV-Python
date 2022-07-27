# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que leia o nome deles e escreva o nome do escolhido.
import random

aluno1 = input('Digite o nome do aluno: ')
aluno2 = input('Digite o nome do aluno: ')
aluno3 = input('Digite o nome do aluno: ')
aluno4 = input('Digite o nome do aluno: ')

pessoas = [aluno1,aluno2,aluno3,aluno4]

resultado = random.choice(pessoas)

print (f'O ALuno escolhido foi: {resultado}')
