"""[Exercício 11] Escreva um programa que leia o nome,
idade e sexo de 4 pessoas. No final do programa, mostre:
1)	A média de idade do grupo;
2)	Qual é o nome do homem mais velho;
3)	Quantas mulheres têm menos de 20 anos."""

# EXERCICIO 11
soma_idade = mulheres = mais_velho = 0
for i in range(1, 5):
    print("=" * 40)
    print(f"{f'{i}o REGISTRO':^40}")
    print("=" * 40)
    sexo = str(input("Qual o seu sexo[M/F]? ")).upper().strip()[0]
    if sexo == 'M':
        idade = int(input("Quantos anos você tem? "))
        soma_idade += idade
        nome = str(input("Qual o seu nome? ")).strip()
        if idade > mais_velho:
            mais_velho = idade
            nome_mais_velho = nome
    else:
        idade = int(input("Quantos anos você tem? "))
        soma_idade += idade
        if idade < 20:
            mulheres += 1
        nome = str(input("Qual o seu nome? ")).strip()
print("=" * 40)
print(f"{'ANALISANDO DADOS...':^40}")
print("=" * 40)
print(f"{nome_mais_velho} é o homem mais velho")
print(f"Existem {mulheres} mulheres com menos de 20 anos.")
print(f"A média das idade é {soma_idade/4:.2f}")


