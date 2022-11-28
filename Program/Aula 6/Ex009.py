"""[Exercício 9] Escreva um programa que leia
o ano de nascimento de sete pessoas. No final,
mostre quantas delas ainda não atingiram a
maioridade e quantas já são maiores."""

# EXERCICIO 9
import datetime
maior_de_idade = menor_de_idade = 0
for i in range(1, 8):
    ano_nascimento = int(input(f"{i}) Quantos anos você tem? "))
    idade = datetime.date.today().year - ano_nascimento
    if idade >= 18:
        maior_de_idade += 1
    else:
        menor_de_idade += 1
print(f"{menor_de_idade} ainda são menor de idade.")
print(f"{maior_de_idade} são maior de idade.")

