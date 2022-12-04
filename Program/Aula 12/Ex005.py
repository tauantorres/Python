"""[Exercício 5] Escreva um programa que leia:
    1) Nome, sexo e idade de várias pessoas;
    2) Guarde os dados de cada pessoa em um dicionário;
    3) Guarde todos os dicionários em uma lista.
No final, mostre:
    1)	Quantas pessoas foram cadastradas;
    2)	A média de idade do grupo;
    3)	Uma lista com todas as mulheres;
    4)	Uma lista coom todas as pessoas com idade acima da média."""

# EXERCICIO 5
txt_1 = f'RESPOSTA INVÁLIDA'
t = len(txt_1) + 8
txt_2 = f"{'=' * t}\n\033[31m{txt_1:^{t}}\033[m\n{'=' * t}"

pessoa = dict()
grupo = list()

idade = 0

while True:

    pessoa['Nome'] = str(input("Nome: ")).strip().title()

    pessoa['Sexo'] = str(input("Sexo [M/F]: ")).strip().upper()[0]
    while pessoa['Sexo'] not in 'MF':
        pessoa['Sexo'] = str(input(f"{txt_2}\nSexo [M/F]: ")).strip().upper()[0]

    auxiliar = input("Idade: ").strip()
    while not auxiliar.isnumeric():
        auxiliar = input(f"{txt_2}\nIdade: ").strip()
    auxiliar = int(auxiliar)
    idade += auxiliar
    pessoa['Idade'] = auxiliar

    grupo.append(pessoa.copy())

    # ENTRADA - CONTINUE?
    resposta = str(input("Quer continuar [S/N]? ")).upper().strip()[0]

    # QA - CONTINUE?
    while resposta not in 'SN':
        resposta = str(input(f"{txt_2}\nQuer continuar [S/N]? ")).upper().strip()[0]
    if resposta == 'N':
        break

# ENCERRAMENTO
media = idade/len(grupo)

print('=' * 50)
print(f"- O grupo tem {len(grupo)} pessoas.")
print(f"- A média da idade é {media:.2f}.")

print("- As mulheres cadastradas foram: ", end=' ')
for i in range(0, len(grupo)):
    if grupo[i]['Sexo'] in 'F':
        print(f"{grupo[i]['Nome']}", end=' ')

print(f"\n- A lista das pessoas que estão acima da média:")
"""for i in range(0, len(grupo)):
    if grupo[i]['Idade'] > media:
        print(f"   => Nome = {grupo[i]['Nome']}; Sexo = {grupo[i]['Sexo']}; Idade = {grupo[i]['Idade']}")
"""
for pessoa in grupo:
    if pessoa['Idade'] > media:
        for chave, valor in pessoa.items():
            print(f"   => {chave} = {valor}; ", end='')
        print()

print(f"{f'< FIM DO PROGRAMA >':=^50}")



