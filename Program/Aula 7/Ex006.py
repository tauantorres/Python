"""[Exercício 7] Escreva um programa que
leia um número n inteiro e mostre na
tela os n primeiros números da Sequência
de Fibonacci da seguinte forma mostrada a seguir.
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8"""

# EXERCICIO 7
p1 = 0
p2 = 1
n = int(input("Quantos termos você deseja mostrar? "))
contador = 2
print(f'{p1}', end=' \033[031m->\033[m ')
print(f'{p2}', end=' \033[031m->\033[m ')
while contador != n:
    p3 = p1 + p2

    if contador < (n - 1):
        print(f'{p3}', end=' \033[031m->\033[m ')
    else:
        print(f'{p3}', end=' ')

    p1 = p2
    p2 = p3
    contador += 1



