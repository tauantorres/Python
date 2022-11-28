"""[Exercício 4] Escreva um programa que leia
um número do usuário e retorne a tábuada desse número."""

# EXERCICIO 4
f = 15
n = int(input("Digite um número:"))
print("="*f)
print(f"{f'TABUADA DO {n}':^{f}}")
print("="*f)

for i in range(1, 11):
    print(f"{i} X {n} = {i*n}")
print("="*f)
