"""[Exercício 6] Escreva um programa que leia os 3 lados
de um triângulo e diga se eles formam ou não um triângulo."""

l1 = float(input("L1 = "))
l2 = float(input("L2 = "))
l3 = float(input("L3 = "))

v1 = (l1 < l2 + l3)
v2 = (l2 < l1 + l3)
v3 = (l3 < l2 + l1)

if v1 and v2 and v3:
    print("GERA UM TRIÂNGULO")
else:
    print("NÃO GERA UM TRIÂNGULO")

