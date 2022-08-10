# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteudo da estrutura na tela.

disc = {'nome': str(input('Digite o Nome: ')), 'media': float(input('Digite a média: '))}

print(f'O nome informado foi {disc["nome"]} A média é: {disc["media"]}')
if disc["media"] >= 6:
    print('APROVADO')
else:
    print('REPROVADO')