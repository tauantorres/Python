"""# EXEMPLO 1
lista = ('Tauan', 'Kristina', 'Kevin', 'Pedro')
print(lista)
print(lista[2])

# EXEMPLO 2
lista = ('Tauan', 'Kristina', 'Kevin', 'Pedro')
print(lista)
print(lista[0:2])

# EXEMPLO 3
lista = ('Tauan', 'Kristina', 'Kevin', 'Pedro')
print(lista)
print(lista[1:])

# EXEMPLO 4
lista = ('Tauan', 'Kristina', 'Kevin', 'Pedro')
print(lista)
print(lista[-1])

# EXEMPLO 5
lista = ('Tauan', 'Kristina', 'Kevin', 'Pedro')
print(lista)
print(len(lista))

# EXEMPLO 6
lista = ('Tauan', 'Kristina', 'Kevin', 'Pedro')
print(lista)
for pessoa in lista:
    print(pessoa)

# EXEMPLO 7
lista = ('Tauan', 'Kristina', 'Kevin', 'Pedro')
print(lista)
for contador in range(0, len(lista)):
    print(lista[contador])

# EXEMPLO 8
lista = ('Tauan', 'Kristina', 'Kevin', 'Pedro')
print(lista)
for posicao, pessoa in enumerate(lista):
    print(f"{pessoa} está na posição {posicao} da tupla!")

# EXEMPLO 9
lista_nomes = ('Tauan', 'Kristina', 'Kevin', 'Pedro')
print(lista_nomes)
print(sorted(lista_nomes))

lista_numeros = (7, 22, 4, 12, 7, 29)
print(lista_numeros)
print(sorted(lista_numeros))

# EXEMPLO 10
a = (1, 2, 3)
b = (4, 5, 6)
c_1 = a + b
c_2 = b + a
print(c_1)
print(c_2)

# EXEMPLO 11
numeros = (7, 22, 4, 12, 7, 29)
print(numeros)
print(numeros.count(7))

letras = ('A', 'B', 'C', 'A', 'D', 'A')
print(letras)
print(letras.count('A'))

# EXEMPLO 12
numeros = (7, 22, 4, 12, 7, 29)
print(numeros)
print(numeros.index(12))

letras = ('A', 'B', 'C', 'A', 'D', 'A')
print(letras)
print(letras.index('C'))
print(letras.index('A'))
print(letras.index('A', 1))

# EXEMPLO 13
info = ('Tauan', 80.0, 'M', 27, 'Porto Alegre')
print(info)

# EXEMPLO 14
pessoa = ('Tauan', 80.0, 'M', 27, 'Porto Alegre')
print(pessoa)
del(pessoa)
print(pessoa)

# EXEMPLO 15
a = (0, 1, 2)
b = (0, 3, 4)
print(a < b)"""

# EXEMPLO 16
produtos = ('Caderno', 12.50, 'Mochila', 55.00, 'Livro', 21.90)

print("\033[033mTESTE 1\033[m")
for posicao in range(0, len((produtos))):
    print(posicao, end=' ')

print("\n\033[033mTESTE 2\033[m")
for produto in produtos:
    print(produto, end=' ')

print("\n\033[033mTESTE 3\033[m")
for posicao, produto in enumerate(produtos):
    print(f' Produto:{produto}. Posição:{posicao}')


