# Crie um programa onde o usuário digite uma expressão qualquer que use parenteses.
# Seu aplicativo deverá analisar se a expressão passada esta com os os parenteses abertos e fechados na ordem correta

n = input('Digite a expressão numerica: ')
a = n.count('(')
b = n.count(')')

if a != b:
    print('A Expressão está incorreta.')
else:
    print('A Expressão é valida:')

