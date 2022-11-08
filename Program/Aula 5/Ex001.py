"""[Exercício 1] Escreva um programa que aprove
um empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário
do comprador e em quantos anos ele vai pagar. Calcule
o valor da prestação mensal, sabendo que ela não pode
exceder 30% do salário ou então o empréstimo será negado."""

valor_da_casa = float(input("Valor da casa: R$"))
salario = float(input("Salário: R$"))
tempo = int(input("Em quantos anos você pretende pagar? "))
prestacao_mensal = valor_da_casa/(tempo*12)
print(f"A prestação mensal será de R${prestacao_mensal:.2f}")
print(f"30% do seu salário é R${salario*0.3:.2f}")
if prestacao_mensal >= salario*0.3:
    print("Empréstimo NEGADO!")
else:
    print("Empréstimo ACEITO!")

