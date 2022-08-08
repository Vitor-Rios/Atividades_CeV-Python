# Crie um programa que tenha uma tupla com varias palavras (Não usar acentos).
# Depois disso, você deve mostrar, para cada, quais são suas vogais.

lista = ('Agua', 'Conector', 'Abastecimento', 'Amaciante')

for p in lista:
    print(f'\n Na palavra {p} temos as vogais: ', end='')
    for vogal in p:
        if vogal.lower() in 'aeiou':
            print(vogal, end=' ')
