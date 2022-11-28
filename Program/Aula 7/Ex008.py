"""[Exercício 8] Escreva um programa que leia
vários números inteiros e só pare quando o
usuário digitar o valor 999. No final, mostre
quantos números foram digitados e qual foi a soma entre eles."""

# EXERCICIO 8
contador = soma = 0
terminar = False

while not terminar:

    numero = int(input("Digite um número [999 to exit]: "))

    if numero != 999:
        contador += 1
        soma += numero

    if numero == 999:
        terminar = True

print(f"Contador = {contador}")
print(f"Soma = {soma}")
