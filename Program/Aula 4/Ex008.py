"""[Exercício 8] Escreva um programa que leia o
comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo."""

L1 = int(input("L1 = "))
L2 = int(input("L2 = "))
L3 = int(input("L3 = "))

V1 = (L1 < L2 + L3)
V2 = (L2 < L1 + L3)
V3 = (L3 < L1 + L2)

if V1 and V2 and V3:
    print("GERA UM TRIANGULO!")
else:
    print("NÃO GERA UM TRIÂNGULO!")
