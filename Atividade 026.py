# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a ultima vez.

texto = input('Digite uma Frase').strip()

print(f'A letra "a" aparece {texto.upper().count("A")} vezes \n'
      f'A primeira vez que ela aparece é na posição {texto.upper().find("A") + 1}\n'
      f'A ultima vez que ela aparece é na posição {texto.upper().rfind("A") +1}')

