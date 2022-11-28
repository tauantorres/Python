"""[Exercício 1] Escreva um programa que leia o
sexo de uma pessoa, mas só aceite ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente
até ter um valor correto."""

# EXERCICIO 1
sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper()[0]
while sexo not in 'MF':
    print('RESPOSTA INVÁLIDA!')
    sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper()[0]
print('--FIM--')