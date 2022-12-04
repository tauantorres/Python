"""[Exercício 2] [DESAFIO] Escreva um programa onde 4 jogadores
joguem um dado e tenham resultados aleatórios. Guarde esses
resultados em um dicionário. No final, coloque esse dicionário
em ordem, sabendo que o vencedor tirou o maior número no dado."""

# EXERCICIO 2
from time import sleep
from random import randint
from operator import itemgetter
jogadores = {'Jogador 1': randint(1, 6),
             'Jogador 2': randint(1, 6),
             'Jogador 3': randint(1, 6),
             'Jogador 4': randint(1, 6)}

print(f"\n\033[33m{f'< JOGADAS >':=^40}\033[m")
for chave, valor in jogadores.items():
    print(f"O {chave} tirou {valor}!")
    sleep(0.5)

ranking = list()
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True) # 0 - Por em ordem por chave
                                                                     # 1 - Por em ordem por valor
print(f"\n\033[35m{f'< RANKING DOS JOGADORES >':=^40}\033[m")
for posicao, valor in enumerate(ranking):
    print(f"{posicao + 1}o Lugar : {valor[0]} com {valor[1]}")
    sleep(0.5)
