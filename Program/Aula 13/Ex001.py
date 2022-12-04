"""[Exercício 1] Escreva um programa que tenha uma função área(),
que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno."""


# EXERCICIO 1
def cabeca():
    txt = 'CONTROLE DE TERRENO'
    t = len(txt) + 6
    print('=' * t)
    print(f"{txt:^{t}}")
    print('=' * t)


def area(largura, comprimento):
    A = largura * comprimento
    print(f"A área do terreno será de A = {A:.2f} m².")


# MAIN FUNCTION
cabeca()
l = float(input("Largura (m): "))
c = float(input("Comprimento (m): "))
area(l, c)
