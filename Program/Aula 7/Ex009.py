"""[Exercício 9] Escreva um programa que leia vários números.
No final, mostre a média entre todos os valores e qual foi
o maior e o menor valores lido. O programa deve perguntar
ao usuário se ele quer ou não continuar a digitar valores."""

# EXERCICIO 9
contador = soma = maior = menor = 0
terminar = False

while not terminar:

    numero = int(input("Digite um número [999 to exit]: "))

    if numero != 999:
        if contador == 0:
            maior = menor = numero
        else:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero
        contador += 1
        soma += numero

    if numero == 999:
        terminar = True

print(f"Contador = {contador}")
print(f"Soma = {soma}")
print(f"Média = {float(soma/contador):.2f}")
print(f"Maior = {maior}")
print(f"Menor = {menor}")




