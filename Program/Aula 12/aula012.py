"""# EXEMPLO 1
dados = {'Nome': 'Tauan', 'Idade': 27}
print(dados)
print(dados['Nome'])
print(dados['Idade'])

# EXEMPLO 2
dados = {'Nome': 'Tauan', 'Idade': 27}
print(dados)
print(dados['Nome'])
print(dados['Idade'])
dados['Sexo'] = 'M'
print(dados)

# EXEMPLO 3
dados = {'Nome': 'Tauan', 'Idade': 27}
print(dados)
dados['Sexo'] = 'M'
print(dados)
del dados['Idade']
print(dados)

# EXEMPLO 4
livro = {'Titulo': 'A revolução dos bichos',
         'Ano': 1945,
         'Autor': 'George Orwell'}
print(livro)
print(livro.values())
print(livro.keys())
print(livro.items())

# EXEMPLO 5
livro = {'Titulo': 'A revolução dos bichos', 'Ano': 1945, 'Autor': 'George Orwell'}
for key, value in livro.items():
    print(f"A chave é {key} e o valor é {value}.")

# EXEMPLO 6
livraria = [{'Titulo': 'A revolução dos bichos', 'Ano': 1945, 'Autor': 'George Orwell'},
            {'Titulo': 'Harry Potter e a Pedra Filosofal', 'Ano': 1999, 'Autor': 'J. K. Rowling'},
            {'Titulo': 'Totem e Tabu', 'Ano': 1913, 'Autor': 'Sigmund Freud'}]
print(livraria[0]['Titulo'])
print(livraria[0]['Ano'])
print(livraria[0]['Autor'])
print("=" * 20)
print(livraria[1]['Titulo'])
print(livraria[1]['Ano'])
print(livraria[1]['Autor'])
print("=" * 20)
print(livraria[2]['Titulo'])
print(livraria[2]['Ano'])
print(livraria[2]['Autor'])
print("=" * 20)

# EXEMPLO 7.1
dados = {'Nome': 'Tauan', 'Idade': 27, 'Sexo': 'M'}
for key in dados.keys():
    print(key)

# EXEMPLO 7.2
dados = {'Nome': 'Tauan', 'Idade': 27, 'Sexo': 'M'}
for value in dados.values():
    print(value)

# EXEMPLO 7.3
dados = {'Nome': 'Tauan', 'Idade': 27, 'Sexo': 'M'}
for key, value in dados.items():
    print(f"{key} = {value}")

# EXEMPLO 8
dados = {'Nome': 'Tauan', 'Idade': 27, 'Sexo': 'M'}
dados['Nome'] = 'Pedro'
for key, value in dados.items():
    print(f"{key} = {value}")

# EXEMPLO 9
dados = {'Nome': 'Tauan', 'Idade': 27, 'Sexo': 'M'}
dados['Peso'] = 81.3
for key, value in dados.items():
    print(f"{key} = {value}")

# EXEMPLO 10
brasil = []
estado_1 = {'UF': 'Rio Grande do Sul', 'Sigla': 'RS'}
estado_2 = {'UF': 'Santa Catarina', 'Sigla': 'SC'}
brasil.append(estado_1)
brasil.append(estado_2)
print(estado_1)
print(estado_2)
print(brasil)
print(brasil[0])
print(brasil[0]['UF'])
print(brasil[0]['Sigla'])
print(brasil[1])
print(brasil[1]['UF'])
print(brasil[1]['Sigla'])

# EXEMPLO 11
brasil = list()
estado = dict()

for contador in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa [UF]: '))
    estado['Sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy()) # estado[:]
print(brasil)


# EXEMPLO 12
brasil = list()
estado = dict()

for contador in range(0, 2):
    estado['UF'] = str(input('Unidade Federativa [UF]: '))
    estado['Sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy()) # estado[:]

for estado in brasil:
    for key, value in estado.items():
        print(f"O campoe'{key}' tem valor de '{value}'.")
"""

# EXEMPLO 13
brasil = list()
estado = dict()

for contador in range(0, 2):
    estado['UF'] = str(input('Unidade Federativa [UF]: '))
    estado['Sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy()) # estado[:]

for estado in brasil:
    for value in estado.values():
        print(f"{value}", end=' ')
    print()
