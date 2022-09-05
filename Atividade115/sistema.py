from Atividade115.lib.interface import *
from Atividade115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])

    if resposta == 1:
        # Opção de ler Arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de novo cadastro
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do Sistema.')
        break
    else:
        print('Opção Inválida')
    sleep(2)

