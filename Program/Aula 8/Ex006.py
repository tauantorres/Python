"""[Exercício 6] Escreva um programa que simule o funcionamento
de um caixa eletrônico. O usuário informa o quanto deverá ser
sacado (inteiro) e o programa retornará quantas cédulas de cada
valor serão entregues. Considere que só há cédulas de 50, 20, 10 e 1."""

# EXERCICIO 6
print("-"*35)
print(f"{f' BANCO CENTRAL ':^35}")
print("-"*35)
total = valor = int(input("Valor à ser sacado: R$"))
cedulas = 50
total_cedulas = 0
while True:
    if total >= cedulas:
        total -= cedulas
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f"Total de {total_cedulas} cédulas de R${cedulas}")
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        total_cedulas = 0
        if total == 0:
            break
print(f"{f' FIM ':-^35}")
