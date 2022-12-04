"""[Exercício 3] Escreva um programa que tenha uma função
chamada contador(), que receba três parâmetros: início,
fim e passo e realize a contagem. Seu programa tem que
realizar três contagens através da função:
1)	De 1 até 10, de 1 em 1;
2)	De 10 até 0, de 2 em 2;
3)	Uma contagem personalizada."""

# EXERCICIO 3
import time
p = 30


def linha():
    print('=' * p)


def subindo():
    linha()
    print("Contando de 0 até 10:")
    for i in range(0, 11):
        print(i, end=' ')
        time.sleep(0.5)
    print("FIM!")


def descendo():
    linha()
    print("Contando de 10 até 0:")
    for i in range(10, -1, -2):
        print(i, end=' ')
        time.sleep(0.5)
    print("FIM!")


def personalizada():
    valores = dict()

    linha()
    valores['Inicio'] = int(input("INICIO: "))
    valores['Fim'] = int(input("FIM: "))
    valores['Passo'] = int(input("PASSO: "))

    while (valores['Inicio'] < valores['Fim'] and valores['Passo'] < 0) or (
            valores['Inicio'] > valores['Fim'] and valores['Passo'] > 0) or (
            valores['Passo'] == 0) or (valores['Fim'] == valores['Inicio']):
        linha()
        print("Operação impossível de se realizar!")
        linha()
        valores['Inicio'] = int(input("INICIO: "))
        valores['Fim'] = int(input("FIM: "))
        valores['Passo'] = int(input("PASSO: "))

    print(f"Contagem de {valores['Inicio']} até {valores['Fim']} de {valores['Passo']} em {valores['Passo']}.")
    for i in range(valores['Inicio'], valores['Fim'], valores['Passo']):
        print(i, end=' ')
    print("FIM!")


# MAIN FUNCTION
time.sleep(0.5)
subindo()
time.sleep(0.5)
descendo()
time.sleep(0.5)
personalizada()
