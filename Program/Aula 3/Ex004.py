"""[Exercício 4] Escreva um programa que
leia o nome completo de uma pessoa e
diga se ela tem “Silva” no nome."""

nome = str(input("Nome completo: ")).strip()
print("O nome tem 'Silva' dentro dele? {}".format("SILVA" in nome.upper()))
