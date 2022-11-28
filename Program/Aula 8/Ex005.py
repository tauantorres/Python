"""[Exercício 5] Escreva um programa que leia o
nome e preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar.
No final, mostre:
1)	Qual é o total gasto na compra;
2)	Quantos produtos custam mais de R$ 1000.
3)	Qual é o nome do produto mais barato."""

# EXERCICIO 5
soma = mais_que_mil = contador = 0
print("="*40)
print(f"{'LOJA SUPER BARATÃO':^40}")
print("="*40)
while True:
    nome_do_produto = str(input("Nome do Produto: "))
    preco = float(input("Preço: R$"))
    contador += 1
    soma += preco
    if contador == 1:
        menor_preco = preco
        nome_do_produto_mais_barato = nome_do_produto
    else:
        if preco < menor_preco:
            menor_preco = preco
            nome_do_produto_mais_barato = nome_do_produto
        if preco >= 1000:
            mais_que_mil += 1

    resposta = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    while resposta not in 'SN':
        print("RESPOSTA INVÁLIDA!")
        resposta = str(input("Quer continuar? [S/N]")).strip().upper()[0]

    if resposta == 'N':
        break
print(f"{' FIM DO PROGRAMA ':=^40}")
print(f"O total da compra foi R${soma:.2f}")
print(f"Temos {mais_que_mil} custando mais de R$1000,00")
print(f"O produto mais barato foi: {nome_do_produto_mais_barato.title()}. Valor = R${menor_preco}")
