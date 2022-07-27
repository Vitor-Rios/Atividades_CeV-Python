# o Professor quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quartro alunos e mostre a ordem sortada.

import random

aluno1 = input('Digite o nome do aluno')
aluno2 = input('Digite o nome do aluno')
aluno3 = input('Digite o nome do aluno')
aluno4 = input('Digite o nome do aluno')

pessoas = [aluno4,aluno3,aluno2,aluno1]

random.shuffle(pessoas)

print (pessoas)
