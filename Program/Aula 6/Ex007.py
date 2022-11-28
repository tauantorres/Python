"""[Exercício 7] Escreva um programa que leia
um número inteiro e diga se ele é primo ou não."""

"""# EXERCICIO 7.1
n = int(input("Digite um valor: "))
contador = 0
for i in range(1, n + 1):
    if n % i == 0:
        contador += 1

if contador == 2:
    print("PRIMO")
else:
    print("NAO É PRIMO")"""

# EXERCICIO 7.2
n = int(input("Digite um valor: "))
contador = 0
for i in range(1, n + 1):
    if n % i == 0:
        print("\033[33m", end='')
        contador += 1
    else:
        print('\033[31m', end='')
    print(f'{i}', end=' ')
print('\033[m')
if contador == 2:
    print("\033[34mPRIMO\033[m")
else:
    print("\033[31mNAO\033[m É \033[34mPRIMO\033[m")
