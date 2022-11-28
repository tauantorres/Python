"""[Exercício 2] Escreva um programa que o computador vai “pensar”
em um número inteiro entre 0 e 10. Só que agora o jogador vai
tentar adivinhar até acertar o número, mostrando no final quantos
palpites foram necessários para vencer.

# EXERCICIO 2.1
import random
contador = 1
computador = random.randint(0, 10)
jogador = int(input("Diginte um número entre 0 e 10: "))
while jogador != computador:
    while jogador not in range(0, 11):
        print('PALPITE INVÁLIDO!')
        jogador = int(input("Diginte um número entre 0 e 10: "))
        contador += 1
    if jogador == computador:
        break
    if jogador < computador:
        print('Mais... Tente mais uma vez.')
    else:
        print('Menos... Tente mais uma vez.')
    jogador = int(input("Diginte um número entre 0 e 10: "))
    contador += 1
print(f'Você VENCEU! Computador pensou em {computador} e você em {jogador}')
print(f'Número de jogadas = {contador}')"""

# EXERCICIO 2.2
import random
computador = random.randint(0, 10)
acertou = False
contador = 0
while not acertou:
    jogador = int(input('Digite um valor: '))
    contador += 1

    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {contador} tentativas')




