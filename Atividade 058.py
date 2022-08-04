# Melhore o jogo do desafio 028 onde o computador vai "Pensar" em um numero entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessarios para vencer.

import random

num = int(input('Digite um Numero entre 0 e 10: '))
cont = 1
lista = random.randint(0, 10)

while num != lista:
    print('VOCÊ PERDEU')
    num = int(input('Tente Outro numero: '))
    cont = cont + 1


print('VOCÊ GANHOU')
print(f'Seu numero escolhido foi {num} e o sorteado pelo Computador foi {lista} \n'
      f'E Precisou de {cont} tentativas para acertar')
