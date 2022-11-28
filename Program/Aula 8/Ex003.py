"""[Exercício 3] Escreva um programa que
jogue par ou impar com o computador.
O jogo só será interrompido quando o
jogador PERDER, mostrando o total de
vitórias consecutivas que ele conquistou
no final do jogo."""

# EXERCICIO 3
import random
contador = 0
while True:
    print("="*30)
    print(f"{f'PAR OU IMPAR':^30}")
    print("="*30)
    print("[1] - PAR")
    print("[2] - IMPAR")
    jogador_escolha = int(input("Qual a sua escolha? "))

    while jogador_escolha != 1 and jogador_escolha != 2:
        print("OPÇÃO INVÁLIDA!")
        jogador_escolha = int(input("Qual a sua escolha? "))

    jogador_numero = int(input("Digite uma valor: "))
    computador = random.randint(1, 100)
    soma = jogador_numero + computador
    print(f"Numero do jogador = {jogador_numero}")
    print(f"Numero do computador = {computador}")
    print(f"Soma = {soma}")
    if jogador_escolha == 1 and soma % 2 == 0:
        print("Você VENCEU!")
        contador += 1
    else:
        print("Você PERDEU!")
        break
print("="*30)
print(f"{f'GAME OVER':^30}")
print("="*30)
print(f"Você tem {contador} vitórias consecutivas.")


