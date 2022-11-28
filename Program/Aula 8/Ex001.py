"""[Exercício 1] Escreva um programa que leia
vários números inteiros e só pare quando o
usuário digitar o valor 999. No final, mostre
quantos números foram digitados e qual foi a
soma entre eles."""

# EXERCICIO 1
numero = contador = soma = 0

while True:
    numero = int(input("Digite um número [999 to Exit]: "))
    if numero == 999:
        break
    else:
        soma += numero
        contador+= 1
print(f"Soma = {soma}")
print(f"Contador = {contador}")



