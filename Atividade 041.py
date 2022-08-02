# A confederação nacional de natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: mirim
# até 14 anos: infantil
# até 19 anos: junior
# até 20 anos: Sênior
# acima: Master

from datetime import date

idade = int(input('Digite o Ano de nascimento: '))
data = date.today()
comp = data.year - idade

if comp <= 9:
    print(comp)
    print('Mirim')
elif 10 <= comp <= 14:
    print(comp)
    print('Infantil')
elif 14 < comp <= 19:
    print(comp)
    print('Junior')
elif comp == 20:
    print(comp)
    print('Sênior')
else:
    print(comp)
    print('Master')
