"""[Exercício 5] Escreva um programa que:
 1) Tenha UMA lista chamada números;
 2) Tenha DUAS funções chamadas sorteia() e somaPar().
 3) A primeira função vaisortear 5 números e vai colocá-los dentro da lista;
 4) A segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior."""


# EXERCICIO 5
def sorteia(lista):
    print("Sorteando os valores: ", end='')
    for i in range(0, 5):
        sleep(0.5)
        valor = randint(1, 100)
        if valor % 2 == 0:
            print(f"\033[34m{valor}\033[m", end=' ')
        else:
            print(f"\033[31m{valor}\033[m", end=' ')
        lista.append(valor)
    sleep(0.5)
    print(" \033[35mPRONTO!\033[m")


def somaPar(lista):
    soma = 0
    sleep(0.5)
    for elemento in lista:
        if elemento % 2 == 0:
            soma += elemento
    print(f'A soma dos valores pares de {lista} é {soma}.')


from random import randint
from time import sleep

numeros = list()
sorteia(numeros)
somaPar(numeros)

