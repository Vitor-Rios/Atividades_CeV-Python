# Crie uma tupla com os 20 primeiros colocados da tabela do Campeonato brasileiro de Futebol, na Ordem de colocação.
# Depois mostre:
# A - Apenas os 5 primeiros colocados.
# B - Os ultimos 4 colocados da tabela
# C - Uma lista com os times em ordem Alfabética
# D - Em que posição da tabela está o time da Chapecoense.

times = ('Corinthians', 'Palmeiras', 'São Paulo', 'Atlético-MG', 'Botafogo','Santos','Fluminense','Coritiba','América-MG','Avaí',
         "Internacional", 'Athletico-PR', 'Bragantino', 'Flamengo', 'Goiás', 'Cuiabá', 'Atlético-GO', 'Juventude', 'Ceará' , 'Fortaleza')

print(times[:5])
print(times[-4:])
print(sorted(times))
print(times.index('Juventude'))
