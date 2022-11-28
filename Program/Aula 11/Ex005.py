"""[Exercício 5] Escreva um programa que ajude um jogador
da MEGA SENA a criar palpites. O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta."""

# EXERCICIO 5
import random
import time

auxiliar = list()
jogos = list()
txt = 'JOGO DA MEGA SENA'
tamanho = (len(txt) + 16)
print(f"{f'=' * tamanho}\n\033[034m{txt:^{tamanho}}\033[m\n{f'=' * tamanho}")
palpites = int(input("Quantos jogos você quer? "))
txt_2 = f'< SORTEANDO {palpites} JOGOS >'
print(f"{txt_2:=^{tamanho}}")
for k in range(0, palpites):
    for i in range(0, 6):
        auxiliar.append(random.randint(1, 60))
    jogos.append(auxiliar[:])
    auxiliar.clear()
for j in range(0, len(jogos)):
    time.sleep(1)
    jogos[j].sort()
    print(f"Jogo {j + 1} : {jogos[j]}")
print(f"{f'< BOA SORTE >':=^{tamanho}}")
