# Crie um programa que tenha uma função notas() que pode receber varias notas de alunos e vai
# retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
#
# Adicione tambem as docstrings da função.

def notas(*num, sit=False):
    """
    -> Função para analistar notas e mostrar situação
    :param num: Notas dos alunos
    :param sit: (Opcional) Mostra a situação
    :return: Retorna Biblioteca com as informações e Resultados
    """
    d = {'Quantidade': len(num), 'Maior': max(num), 'Menor': min(num), 'Média': sum(num) / len(num)}
    if sit:
        if d['Média'] >= 7:
            d['Situação'] = 'BOA'
            return d
        elif 6 <= d['Média'] < 7:
            d['Situação'] = 'Médio'
            return d
        elif d['Média'] < 6:
            d['Situação'] = 'Ruim'
            return d
    else:
        return d


resp = notas(6, 8, 6, 8, 10, sit=True)
print(resp)
help(notas)
