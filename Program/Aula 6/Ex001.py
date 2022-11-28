"""[Exercício 1] Escreva um programa que faça
a contagem regressiva de 10 até 0 com uma
pausa de 1 segundo entre eles."""

# EXERCICIO 1
import time

for i in range(10, -1, -1):
    print(i)
    time.sleep(1)
print("---FIM---")


