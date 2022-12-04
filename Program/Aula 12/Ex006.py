"""[Exercício 6] [DESAFIO] Escreva um programa que
aprimore o exercício 4 para que funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador."""

# EXERCICIO 6

txt_1 = f'RESPOSTA INVÁLIDA'
txt_2 = f'Esse valor não é um número. Tente novamente.'
t = len(txt_2) + 4

time = list()
jogador = dict()
gols = list()

while True:
    jogador.clear()
    gols.clear()
    jogador['Nome'] = str(input("Nome do jogador: ")).strip().title()
    partidas = input(f"Quantas partidas {jogador['Nome']} jogou? ").strip()

    while not partidas.isnumeric():
        print(f"{'=' * t}\n\033[31m{txt_1:^{t}}\033[m\n{txt_2:^{t}}\n{'=' * t}")
        partidas = input(f"Quantas partidas {jogador['Nome']} jogou? ").strip()
    partidas = int(partidas)

    for i in range(0, partidas):
        auxiliar = input(f"   => Quantos gols na {i + 1}o partida? ").strip()

        while not auxiliar.isnumeric():
            print(f"{'=' * t}\n\033[31m{txt_1:^{t}}\033[m\n{txt_2:^{t}}\n{'=' * t}")
            auxiliar = input(f"Quantos gols na {i + 1}o partida? ").strip()
        auxiliar = int(auxiliar)
        gols.append(auxiliar)

    jogador['Gols'] = gols[:]
    jogador['Total de gols'] = sum(gols)
    time.append(jogador.copy())

    resposta = str(input("Deseja continuar[S/N]? ")).strip().upper()[0]
    while resposta not in 'SN':
        print(f"{'=' * t}\n\033[31m{txt_1:^{t}}\033[m\n{'=' * t}")
        resposta = str(input("Deseja continuar[S/N]? ")).strip().upper()[0]
    if resposta == 'N':
        break

print('=' * t)
print("Cód. ", end='')
for key in jogador.keys():
    print(f"{key:<15}", end='')
print()
print('=' * t)
for chave, valor in enumerate(time):
    print(f"{chave:<4} ", end='')
    for i in valor.values():
        print(f"{str(i):<15}", end='')
    print()
print('=' * t)

while True:
    busca = input("Selecione o jogador pelo código [999 to Exit]: ").strip()
    while not busca.isnumeric():
        print(f"{'=' * t}\n\033[31m{txt_1:^{t}}\033[m\n{txt_2:^{t}}\n{'=' * t}")
        busca = input("Selecione o jogador pelo código [999 to Exit]: ").strip()
    busca = int(busca)
    if busca == 999:
        break

    if busca >= len(time):
        print(f"{'=' * t}\n\033[31mNÃO\033[m existe jogador com o código de número {busca}.\n{'=' * t}")
    else:
        print(f"{'=' * t}\nLEVANTAMENTO DO JOGADOR: {time[busca]['Nome']}")
        for indice, gol in enumerate(time[busca]['Gols']):
            print(f"  => No jogo {indice + 1} fez {gol} gols.")
    print('=' * t)

print(f"{'< VOLTE SEMPRE >':-^{t}}")
