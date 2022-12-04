"""[Exercício 4] Escreva um programa que gerencie o aproveitamento
de um jogador de futebol. O programa vai:
1) Ler o nome do jogador e quantas partidas ele jogou.
2) Depois vai ler a quantidade de gols feitos em cada partida.
3) No final, tudo isso será guardado em dicionário, incluindo o total de gols feitos durante o campeonato."""

# EXERCICIO 4

txt_1 = f'RESPOSTA INVÁLIDA'
txt_2 = f'Esse valor não é um número. Tente novamente.'
t = len(txt_2) + 4
# soma = 0

jogador = dict()
gols = list()

# ENTRADA - NOME
jogador['Nome'] = str(input("Nome do jogador: ")).strip().title()

# ENTRADA - QUANTIDADE DE PARTIDAS
partidas = input(f"Quantas partidas {jogador['Nome']} jogou? ").strip()

# QA - PARTIDA COMO INTEIRO
while not partidas.isnumeric():
    print(f"{'=' * t}\n\033[31m{txt_1:^{t}}\033[m\n{txt_2:^{t}}\n{'=' * t}")
    partidas = input(f"Quantas partidas {jogador['Nome']} jogou? ").strip()
partidas = int(partidas)

# ENTRADA - GOLS EM PARTIDAS
for i in range(0, partidas):
    auxiliar = input(f"   => Quantos gols na {i + 1}o partida? ").strip()

    # QA - VALOR COMO TIPO NÚMERICO
    while not auxiliar.isnumeric():
        print(f"{'=' * t}\n\033[31m{txt_1:^{t}}\033[m\n{txt_2:^{t}}\n{'=' * t}")
        auxiliar = input(f"Quantos gols na {i + 1}o partida? ").strip()
    auxiliar = int(auxiliar)
    # soma += auxiliar
    gols.append(auxiliar)

jogador['Gols'] = gols[:]
jogador['Total de gols'] = sum(gols)  # soma

# SAÍDA - MOSTRANDO O RESULTADO FINAL
print('=' * t)
print(jogador)
print('=' * t)
for chave, valor in jogador.items():
    print(f"O campo {chave} tem o valor {valor}.")
print('=' * t)

print(f"O jogador {jogador['Nome']} jogou {partidas} partidas.")

# for posicao in range(0, partidas):
#    print(f"   => Na partida {posicao + 1}, fez {jogador['Gols'][posicao]} gols.")

for posicao, gol in enumerate(jogador['Gols']):
    print(f"   => Na partida {posicao + 1}, fez {gol} gols.")

print(f"Foi um total de {jogador['Total de gols']} gols.")
print(f"{f'< FIM DO PROGRAMA >':=^{t}}")
