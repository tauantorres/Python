# EXEMPLO 1
print("\033[31m{:=^50}\033[m" .format(' EXEMPLO 1 '))

teste = list()
teste.append('Tauan')
teste.append(27)
print(f"Sua lista de teste = {teste}")

galera = list()
galera.append(teste)
teste[0] = 'Kristina'
teste[1] = 26
galera.append(teste)
print(f"Sua lista galera = {galera}]\n")

# EXEMPLO 2
print("\033[31m{:=^50}\033[m" .format(' EXEMPLO 2 '))

teste2 = list()
teste2.append('Tauan')
teste2.append(27)
print(f"Sua lista de teste = {teste2}")

galera2 = list()
galera2.append(teste2[:])
teste2[0] = 'Kristina'
teste2[1] = 26
galera2.append(teste2[:])
print(f"Sua lista galera = {galera2}\n")

# EXEMPLO 3
print("\033[31m{:=^50}\033[m" .format(' EXEMPLO 3 '))

galera3 = [['Tauan', 27], ['Kristina', 26], ['Alba', 58]]
print("Imprimindo cada termo:")
print(f"galera3[0][0] = {galera3[0][0]}")
print(f"galera3[0][1] = {galera3[0][1]}")
print(f"galera3[1][0] = {galera3[1][0]}")
print(f"galera3[1][1] = {galera3[1][1]}")
print(f"galera3[2][0] = {galera3[2][0]}")
print(f"galera3[2][1] = {galera3[2][1]}")
print("\nImprimindo cada lista dentro da lista principal:")
print(f"galera3[0] = {galera3[0]}")
print(f"galera3[1] = {galera3[1]}")
print(f"galera3[2] = {galera3[2]}")

# EXEMPLO 4
print("\033[31m{:=^50}\033[m" .format(' EXEMPLO 4 '))

print("Usando 'for' para imprimir as listas dentro da lista:")
for pessoa in galera3:
    print(pessoa)
print('')

# EXEMPLO 5
print("\033[31m{:=^50}\033[m" .format(' EXEMPLO 5 '))

print("Usando 'for' para imprimir só os nomes: ")
for pessoa in galera3:
    print(pessoa[0])

print('')

print("Usando 'for' para imprimir só as idades: ")
for pessoa in galera3:
    print(pessoa[1])

print('')

print("Usando 'for' para imprimir o nome e a idade: ")
for pessoa in galera3:
    print(f"{pessoa[0]} tem {pessoa[1]} anos de idade.")

print('')

# EXEMPLO 6
print("\033[31m{:=^50}\033[m" .format(' EXEMPLO 6 '))

pessoas = list()
dados = list()
total_maior = total_menor = 0

for i in range(0, 3):
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Idade: ")))
    pessoas.append(dados[:])
    dados.clear()

for i in pessoas:
    if i[1] >= 21:
        print(f"{i[0]} é maior de idade.")
        total_maior += 1
    else:
        print(f"{i[0]} é menor de idade.")
        total_menor += 1

print(f"Temos {total_maior} maiores e {total_menor} menores de idade.")
