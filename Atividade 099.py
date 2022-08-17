# Faça um programa que tenha um função chamada maior(),
# que receba vários parametros com valores inteiros.
# Seu programa tem que analistar todos os valores e dizer qual deles é o maior

def maior(* valores):
    if len(valores)>0:
        print(f'foram informados os seguintes valores {valores}, ao todo foram {len(valores)} valores')
        print(f'o Maior valor informado foi {max(valores)}')
    else:
        print(f'não foi informado valor')


maior(6,8,7,8,10)
maior(0,1,3,50)
maior()
maior(1)