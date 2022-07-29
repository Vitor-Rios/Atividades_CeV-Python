# faça um programa que leia um ano e mostre se ele é bissexto
# 1 Se o ano for uniformemente divisível por 4, vá para a etapa 2. Caso contrário, vá para a etapa 5.
# 2 Se o ano for uniformemente divisível por 100, vá para a etapa 3. Caso contrário, vá para a etapa 4.
# 3 Se o ano for uniformemente divisível por 400, vá para a etapa 4. Caso contrário, vá para a etapa 5.
# 4 O ano é bissexto (tem 366 dias).
# 5 O ano não é um ano bissexto (tem 365 dias).

ano = int(input('Digite o ano: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print(f'Ano {ano} é Bissexto')

else:
    print(f'Ano {ano} não é Bixessto')
