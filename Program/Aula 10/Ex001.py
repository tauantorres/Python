"""[Exercício 1] [DESAFIO] Escreva um programa que leia 5 valores
e guarde-os dentro de uma lista. No final, mostre qual foi o maior
e o menor valor digitado e as suas respectivas posições na lista."""

# EXERCICIO 1
numeros = list()
maiores = list()
menores = list()
for i in range(0, 5):
    numeros.append(int(input(f"Digite o {i + 1}o valor: ")))
    if i == 0:
        maior = numeros[i]
        menor = numeros[i]
    else:
        if numeros[i] > maior:
            maior = numeros[i]
        if numeros[i] < menor:
            menor = numeros[i]
for posicao, numero in enumerate(numeros):
    if numero == maior:
        maiores.append(posicao)
    if numero == menor:
        menores.append(posicao)

print(f"Você digitou os valores {numeros}.")

print(f"O maior valor digitado foi {maior} nas posições ", end='')
for i in range(0, len(maiores)):
    print(f"{maiores[i]}", end='...')

print(f"\nO menor valor digitado foi {menor} nas posições ", end='')
for i in range(0, len(menores)):
    print(f"{menores[i]}", end='...')
