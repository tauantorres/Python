"""[Exercício 10] Escreva um programa que leia
o peso de cinco pessoas. No final, mostre
qual foi o maior e menor peso lidos."""

# EXERCICIO 10.1
maior = menor = 0
for i in range(1, 6):
    if i == 1:
        menor = maior = float(input(f"Peso {i}o pessoa = "))
    else:
        peso = float(input(f"Peso {i}o pessoa = "))
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O maior peso digitado foi {maior:.2f}Kg")
print(f"O menor peso digitado foi {menor:.2f}Kg")

# EXERCICIO 10.2
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}o pessoa: '.format(p)))

    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido é {}'.format(maior))
print('O menor peso lido é {}'.format(menor))
