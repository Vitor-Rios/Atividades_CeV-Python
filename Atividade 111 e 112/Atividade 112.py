# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
# mas com uma validação de dados para aceitar apenas valores que sejam monetários


from utilidadesCeV import moeda, dado

num = dado.leiaDinheiro('Digite o Valor: ')
dec = float(input('Deseja Aumentar e Diminuir quantos %? '))

moeda.resumo(num, dec)
