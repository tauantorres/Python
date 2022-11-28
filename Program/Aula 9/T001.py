produtos = ('Caderno', 12.50, 'Mochila', 55.00, 'Livro', 21.90)

for posicao in range(0, len((produtos))):
    if i % 2 == 0:
        print(produtos[posicao], end=' - ')
    else:
        print(produtos[posicao])
