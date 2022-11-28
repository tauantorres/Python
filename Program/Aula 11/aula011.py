"""# RELEMBRANDO
dados = list()
dados.append('Tauan')
dados.append(27)
print(dados[0])
print(dados[1])

# EXEMPLO 1
dados = ['Tauan', 27]
pessoas = list()
pessoas.append(dados[:])
print(pessoas[0])

# EXEMPLO 2
pessoas = [['Tauan', 27], ['Pedro', 22], ['Kevin', 24]]
print(pessoas)
print(pessoas[0])
print(pessoas[1])
print(pessoas[2])

# EXEMPLO 3
pessoas = [['Tauan', 27], ['Pedro', 22], ['Kevin', 24]]
# NOMES
print(pessoas[0][0])
print(pessoas[1][0])
print(pessoas[2][0])
# IDADES
print(pessoas[0][1])
print(pessoas[1][1])
print(pessoas[2][1])
# SUBLISTA
print(pessoas[0])
print(pessoas[1])
print(pessoas[2])

# EXEMPLO 4
pessoa = list()
pessoa.append('Tauan')
pessoa.append(27)

grupo = list()
grupo.append(pessoa)
print(grupo)

pessoa[0] = 'Kristina'
pessoa[1] = 26
grupo.append(pessoa)
print(grupo)

# EXEMPLO 5
pessoa = list()
pessoa.append('Tauan')
pessoa.append(27)

grupo = list()
grupo.append(pessoa[:])
print(grupo)

pessoa[0] = 'Kristina'
pessoa[1] = 26
grupo.append(pessoa[:])
print(grupo)

# EXEMPLO 6
grupo = [['Kristina', 27], ['Anuk', 13], ['Tauan', 31], ['Kevin', 24]]
for pessoa in grupo:
    print(pessoa)
print("--FIM--")

# EXEMPLO 7
grupo = [['Kristina', 27], ['Anuk', 13], ['Tauan', 31], ['Kevin', 24]]
for pessoa in grupo:
    # NOME
    print(pessoa[0])
print("--FIM--")

# EXEMPLO 8
grupo = [['Kristina', 27], ['Anuk', 13], ['Tauan', 31], ['Kevin', 24]]
for pessoa in grupo:
    # IDADE
    print(pessoa[1])
print("--FIM--")

# EXEMPLO 9
grupo = [['Kristina', 27], ['Anuk', 13], ['Tauan', 31], ['Kevin', 24]]
for pessoa in grupo:
    print(f"{pessoa[0]} tem {pessoa[1]} anos de idade.")

# EXEMPLO 10
pessoas = list()
dado = list()
for i in range(0, 3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    pessoas.append(dado[:])
    dado.clear()
print(pessoas)

# EXEMPLO 11
pessoas = list()
dado = list()
for i in range(0, 3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    pessoas.append(dado[:])
    print("="*30)
    print("\033[31mANTES\033[m:")
    print(pessoas)
    print(dado)
    dado.clear()
    print("=" * 30)
    print("\033[34mDEPOIS\033[m:")
    print(pessoas)
    print(dado)
    print("=" * 30)
print(pessoas)"""

# EXEMPLO 12

grupo = list()
pessoailiar = list()
maior_idade = menor_idade = 0
quantidade = int(input("Quantas pessoas você quer registrar? "))
for i in range(0, quantidade):
    pessoailiar.append(str(input("Nome: ")))
    pessoailiar.append(int(input("Idade: ")))
    grupo.append(pessoailiar[:])
    pessoailiar.clear()

for pessoa in grupo:
    if pessoa[1] >= 18:
        print(f"{pessoa[0]} é \033[34mMAIOR\033[m de idade.")
        maior_idade += 1
    else:
        print(f"{pessoa[0]} é \033[31mMENOR\033[m de idade.")
        menor_idade += 1
print(f"Temos {menor_idade} menores de idade e {maior_idade} maiores de idade registrados.")

