"""[Exercício 3] Escreva um programa que vai
gerar cinco números aleatórios e colocar
dentro em uma tupla. Depois disso, mostre a
listagem de números gerados e também indique
o menor e o maior valor que estão na tupla."""

# EXERCICIO 3
import random
tupla = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10),
         random.randint(1, 10), random.randint(1, 10))
print(tupla)
for i in range(0, 5):
    if i == 0:
        maior = menor = tupla[0]
    else:
        if tupla[i] > maior:
            maior = tupla[i]
        if tupla[i] < menor:
            menor = tupla[i]
print(f"O maior valor é {maior}")
print(f"O menor valor é {menor}")
