"""[Exercício 6] Escreva um programa que leia
três números e mostre qual é o maior e qual é o menor."""

maior = menor = 0
N1 = int(input("Primeiro número: "))
maior = menor = N1

N2 = int(input("Segundo número: "))
if N2 >= maior:
    maior = N2
if N2 <= menor:
    menor = N2

N3 = int(input("Terceiro número: "))
if N3 >= maior:
    maior = N3
if N3 <= menor:
    menor = N3

print("Maior número {}".format(maior))
print("Menor número {}".format(menor))

