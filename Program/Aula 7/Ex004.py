"""[Exercício 4] Escreva um programa que leia
um número e calcule seu fatorial mostra da
tela como exemplo a seguir. 5! = 5x4x3x2x1 = 120"""

# EXERCICIO 4
numero = int(input("Digite um número inteiro: "))
while numero <= 0:
    print('NÃO EXISTE FATORIAL DE NÚMERO NEGATIVO OU ZERO!')
    numero = int(input("Digite um número inteiro: "))
produto = 1
print(f"{numero}! = ", end='')
while numero != 0:
    if numero != 1:
        print(f"{numero}", end=' x ')
    else:
        print(f"{numero}", end=' ')
    produto *= numero
    numero -= 1
print(f'= {produto}')
