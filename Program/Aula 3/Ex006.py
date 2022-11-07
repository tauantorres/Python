"""[Exercício 6] Escreva um programa que leia
o nome completo de uma pessoa e mostre o
primeiro e o último nome separadamente."""

nome = str(input("Nome completo: ")).strip()
print("Primeiro nome: {}".format(nome.split()[0]))
print("Último nome: {}".format(nome.split()[len(nome.split()) - 1]))
