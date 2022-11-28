"""[Exercício 4] Escreva um programa que melhore o exercício 3, mostrando no final:
1)	A soma de todos os valores pares digitados;
2)	A soma dos valores da terceira coluna;
3)	O maior valor da segunda linha."""

# EXERCICIO 4
matrix = [[], [], []]
pares = terceira_linha = 0
for i in range(0, 3):
    for j in range(0, 3):
        matrix[i].append(int(input(f"matriz[{i}][{j}] = ")))

print("="*10)
print(f"{f'MATRIZ':^10}")
print("="*10)
for i in range(0, 3):
    for j in range(0, 3):
        print(f" {matrix[i][j]}", end=' ')
        if matrix[i][j] % 2 == 0:
            pares += matrix[i][j]
        if i == 2:
            terceira_linha += matrix[i][j]
        if i == 1:
            if j == 0:
                maior = matrix[i][j]
            else:
                if matrix[i][j] > maior:
                    maior = matrix[i][j]

    print("")
print("="*10)
print(f"A soma de todos os valores pares = {pares}")
print(f"A soma da terceira linha = {terceira_linha}")
print(f"O maior valor da segunda linha = {maior}")
