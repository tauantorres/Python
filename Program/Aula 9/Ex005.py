"""[Exercício 5] Escreva um programa que
tenha uma tupla única com os nomes de
produtos e seus respectivos preços, na
sequência. No final, mostre uma listagem
de preços, organizando os dados em forma tabular."""

# EXERCICIO 5
produtos = ('Caderno', 12.50, 'Mochila', 55.00, 'Livro', 21.90)
print("-"*30)
print(f"\033[33m{f'TABELA DE PREÇOS':^30}\033[m")
print("-"*30)
for posicao_produto in range(0, len(produtos)):
    if posicao_produto % 2 == 0:
        print(f"{produtos[posicao_produto]:.<23}", end='')
    else:
        print(f"R${produtos[posicao_produto]:.2f}")
print("-"*30)
