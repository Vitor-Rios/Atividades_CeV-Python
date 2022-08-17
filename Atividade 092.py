# Crie umn programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em
# um dicionário, se por acaso a CTPS for diferente de ZERO,
# O docionário receberá tambem o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quando anos a pessoa vai se aposentar
# Considerar 35 anos de trabalho

import datetime
ano = datetime.date.today().year
pessoa = {'nome': str(input('Digite o Nome: ')),
          'idade': ano - int(input('Digite o Ano de nascimento: ')),
          'CTPS': int(input('Digite o No da CTPS [0 se não tiver]: '))}
if pessoa['CTPS'] != 0:
    pessoa['contratacao'] = int(input('Digite o ano de contratação: '))
    pessoa['salario'] = float(input('Digite o Salário: '))
    pessoa['aposentadoria'] = pessoa['contratacao'] + 35 + pessoa['idade'] - ano
print('-=-' * 15)
for c, v in pessoa.items():
    print(f'O Campo {c} tem o valor {v}')
