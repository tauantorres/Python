"""[Exercício 6] Escreva um programa que
leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão."""

# EXERCICIO 6
a1 = int(input("Primeiro termo: "))
salto = int(input("Salto da PA: "))
for i in range(a1, a1 + 9*salto + 1, salto):
    print(i)

