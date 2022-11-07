"""[Exercício 3] Escreva um programa que leia um ângulo qualquer e
mostre na tela o valor do seno, cosseno e tangente desse ângulo."""

import math
angulo = float(input("Angulo = "))
radianos = math.radians(angulo)

seno = math.sin(radianos)
print("Sin({}) = {:.2f}".format(angulo, seno))
cosseno = math.cos(radianos)
print("Cos({}) = {:.2f}".format(angulo, cosseno))
tangente = math.tan(radianos)
print("Tg({}) = {:.2f}".format(angulo, tangente))
