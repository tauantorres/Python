"""[Exercício 9] Escreva um programa que em que você jogue JoKenPo com o computador."""

import random
print("="*20)
print("""Faça a sua escolha:
[1] - PEDRA
[2] - PAPEL
[3] - TESOURA""")
print("="*20)
usuario = int(input("Sua escolha: "))
computador = random.randint(1, 3)
lista = ["PEDRA", "PAPEL", "TESOURA"]
print(f"A máquina escolheu {lista[computador - 1]}")
if usuario != 1 and usuario != 2 and usuario != 3:
    print("OPÇÃO INVÁLIDA!")
else:
    if usuario == 1:
        print("Você escolheu PEDRA")
        if computador == 2:
            print("PERDEU")
        elif computador == 3:
            print("VENCEU")
        else:
            print("EMPATE")
    elif usuario == 2:
        print("Você escolheu PAPEL")
        if computador == 2:
            print("EMPATE")
        elif computador == 3:
            print("PERDEU")
        else:
            print("VENCEU")
    elif usuario == 3:
        print("Você escolheu TESOURA")
        if computador == 2:
            print("VENCEU")
        elif computador == 3:
            print("EMPATE")
        else:
            print("PERDEU")
