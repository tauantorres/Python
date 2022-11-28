"""[Exercício 2] Escreva um programa onde o
usuário possa digitas sete valores numéricos
e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final,
mostre os valores pares e ímpares em ordem crescente."""

# EXERCICIO 2.1
lista = list()
numeros = list()
pares = list()
impares = list()

while True:
    auxiliar = int(input("Digite um valor: "))
    numeros.append(auxiliar)
    if auxiliar % 2 == 0:
        pares.append(auxiliar)
    else:
        impares.append(auxiliar)

    resposta = str(input("Deseja continuar[S/N]? ")).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input(f"{f'='*20}\n\033[031m{f'RESPOSTA INVÁLIDA!':^20}\033[m\n{f'='*20}\nDeseja continuar[S/N]? ")).upper().strip()[0]
    if resposta == 'N':
        break
lista.append(numeros[:])
lista.append(pares[:])
lista.append(impares[:])
pares.sort(reverse=True)
impares.sort(reverse=True)
print(f"Lista = {lista}")
print(f"Numeros = {numeros}")
print(f"Pares = {pares}")
print(f"Impares = {impares}")
