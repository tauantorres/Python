"""[Exercício 1] Escreva um programa que
leia o nome e peso de várias s,
guardando tudo em uma lista. No final, mostre:
1)	Quantas pessoas foram cadastradas;
2)	Uma listagem com as pessoas mais pesadas;
3)	Uma listagem com as pessoas mais leve."""

# EXERCICIO 1
pessoas = list()
auxiliar = list()
while True:
    print("=" * 20)
    print(f"\033[33m{f'CADASTRO {len(pessoas) + 1}':^20}\033[m")
    print("=" * 20)
    auxiliar.append(str(input("Nome: ")))
    auxiliar.append(int(input("Peso: ")))

    if len(pessoas) == 0:
        maior_peso = menor_peso = auxiliar[1]

    else:
        if auxiliar[1] > maior_peso:
            maior_peso = auxiliar[1]

        if auxiliar[1] < menor_peso:
            menor_peso = auxiliar[1]

    pessoas.append(auxiliar[:])
    auxiliar.clear()

    resposta = str(input("Deseja continuar[S/N]? ")).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input(f"{f'='*20}\n\033[031m{f'RESPOSTA INVÁLIDA!':^20}\033[m\n{f'='*20}\nDeseja continuar[S/N]? ")).upper().strip()[0]
    if resposta == 'N':
        break
print("=" * 20)
print(f"Ao todo, {len(pessoas)} pessoas foram cadastradas.")

print(f"O \033[031mMAIOR\033[m peso digita foi {maior_peso}Kg. Peso de ", end='')
for pessoa in pessoas:
    if pessoa[1] == maior_peso:
        print(f"[{pessoa[0]}]", end=' ')

print(f"\nO \033[034mMENOR\033[m peso digita foi {menor_peso}Kg. Peso de ", end='')
for pessoa in pessoas:
    if pessoa[1] == menor_peso:
        print(f"[{pessoa[0]}]", end=' ')
