# EXERCICIO 2.2
lista = [[], [], []]
while True:
    auxiliar = int(input("Digite um valor: "))

    if auxiliar % 2 == 0:
        lista[0].append(auxiliar)
        lista[1].append(auxiliar)
    else:
        lista[0].append(auxiliar)
        lista[2].append(auxiliar)

    resposta = str(input("Deseja continuar[S/N]? ")).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input(f"{f'='*20}\n\033[031m{f'RESPOSTA INVÁLIDA!':^20}\033[m\n{f'='*20}\nDeseja continuar[S/N]? ")).upper().strip()[0]
    if resposta == 'N':
        break

print(f"Lista = {lista}")
lista[1].sort(reverse=True)
lista[2].sort(reverse=True)
print(f"Pares = {lista[1]}")
print(f"Impares = {lista[2]}")
