"""[Exercício 1] Escreva um programa que
o computador pensará em um número entre 0 e 5.
Em seguida, o usuário deverá adivinhar esse valor.
Caso o usuário acerte, retorne “VENCEU”, caso perca, retorne “PERDEU”."""

import random
import time
print("="*20)
print("{:^20}".format("ADIVINHACAO"))
print("="*20)

jogador = int(input("Em que número eu pensei [entre 0 e 5]? "))
maquina = random.randint(0, 5)

print("PROCESSANDO...")
time.sleep(1)
print("Eu pensei em {}".format(maquina))
if jogador == maquina:
    print("ACERTOU")
else:
    print("PERDEU")
