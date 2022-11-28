"""[Exercício 3] Escreva um programa que crie
uma matriz de dimensão 3X3 e preencha com
valores lidos pelo teclado. No final, mostre
a matriz na tela com a formatação correta."""

# EXERCICIO 3
matrix = [[], [], []]
for i in range(0, 3):
    for j in range(0, 3):
        matrix[i].append(int(input(f"matriz[{i}][{j}] = ")))
print("="*10)
print(f"{f'MATRIZ':^10}")
print("="*10)
for i in range(0, 3):
    for j in range(0, 3):
        print(f" {matrix[i][j]}", end=' ')
    print("")
