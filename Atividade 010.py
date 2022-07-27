# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# E mostre quando dolares ela pode comprar (considera US$ 1,00 = R$3,27)

din = float(input('Digite o valor que possui em R$: '))
dol = din/3.27

print(f'Com esse valor "R$ {din}" você consegue "US${dol:.2f}"')
