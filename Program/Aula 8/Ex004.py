"""[Exercício 4] Escreva um programa que leia
a idade e o sexo de várias pessoas. A cada
pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre:
1)	Quantas pessoas tem mais de 18 anos;
2)	Quantos homens foram cadastrados;
3)	Quantas mulheres tem menos de 20 anos."""

# EXERCICIO 4
contador = pessoas_maioridade = homens_cadastrados = mulheres_menores_de_vinte = 0
while True:
    print("="*30)
    sexo = str(input("Qual o seu sexo [M/F]:")).strip().upper()[0]
    while sexo not  in 'MF':
        print("RESPOSTA INVÁLIDA!")
        sexo = str(input("Qual o seu sexo [M/F]:")).strip().upper()[0]

    idade = int(input("Quantos anos você tem? "))

    if idade >= 18:
        pessoas_maioridade += 1
    if sexo == 'M':
        homens_cadastrados += 1
    if sexo == 'F' and idade < 20:
        mulheres_menores_de_vinte += 1

    resposta = str(input("Você deseja continuar [S/N]? ")).strip().upper()[0]
    while resposta not in 'SN':
        print("RESPOSTA INVÁLIDA!")
        resposta = str(input("Você deseja continuar [S/N]? ")).strip().upper()[0]
    if resposta == 'N':
        break
print("="*30)
print(f"Pessoas com mais de 18 = {pessoas_maioridade}")
print(f"Homens cadastrados = {homens_cadastrados}")
print(f"Mulheres com menos de 20 = {mulheres_menores_de_vinte}")
