"""[Exercício 1] Escreva um programa que leia um
número real qualquer e mostre a sua porção inteira."""

import math
N = float(input("Digite um valor: "))
print("A parte inteira de  {} vale {}".format(N, math.trunc(N)))
