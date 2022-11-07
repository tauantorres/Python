"""[Exercício 2] Escreva um programa que leia os dois catetos
de um triângulo retângulo e retorne o comprimento da hipotenusa."""

import math
C1 = float(input("Cateto oposto = "))
C2 = float(input("Cateto adjacente = "))
H = math.hypot(C1, C2)
#H = math.sqrt(pow(C1, 2) + pow(C2, 2))
print("Hipotenusa = {}".format(H))
