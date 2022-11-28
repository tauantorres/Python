"""[Exercício 8] Escreva um programa que leia
uma frase qualquer e diga se ela é um PALÍNDROMO,
desconsiderando os espaços e a acentuação."""

# EXERCICIO 8.2
frase = str(input("Digite um frase: ")).strip().upper()
juntos = ''.join(frase.split())
inverso = juntos[::-1]

if juntos == inverso:
    print("\033[34mPALINDROMO\033[m")
else:
    print("\033[31mNÃO\033[m É UM \033[34mPALINDROMO\033[m")





