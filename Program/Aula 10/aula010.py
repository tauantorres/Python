print('{:=^30}' .format(' EXEMPLO 1 '))

# EXEMPLO 1

numero_1 = (2, 5, 9, 1)
#numero_1[2] = 3
print('Tupla =', numero_1)

# ALTERANDO VALORES
numero_2: list[int] = [2, 5, 9, 1]
print('Lista =', numero_2)
numero_2[2] = 3
print('Lista alterada =', numero_2)

# ADICIONANDO VALORES
numero_2.append(7)
print('Adicionando valor 7 ao numero_2 =', numero_2)

# COLOCANDO EM ORDEM DIRETA
numero_2.sort()
print('Colocando em ordem direta =', numero_2)

# COLOCANDO EM ORDEM REVERSA
numero_2.sort(reverse=True)
print('Colocando em ordem reversa =', numero_2)

# TAMANHO DA LISTA
print('A lista tem tamanho =', len(numero_2))

# INSERIR VALORES  NA LISTA
numero_2.insert(2, 0) # .insert("QUAL POSICAO", "VALOR A SER ADICIONADO")
print('Inserindo o valor "0" na posicao "2"=', numero_2)

# REMOVER ELEMENTOS
numero_2.pop() # ELIMINA O ULTIMO VALOR
print('Eliminando o ultimo valor =', numero_2)
numero_2.pop(2) # ELIMINA O VALOR NA POSICAO "2"
print('Elimando o valor na posicao "2" =', numero_2)

# EXEMPLO 2
print('\n{:=^30}' .format(' EXEMPLO 2 '))

numero_3 = [7, 5, 3, 2, 1]
print('numero_3 =', numero_3)
numero_3.insert(2, 2)
print('Inserindo o valor "2" na posicap "2" =', numero_3)
numero_3.remove(2)
print('Removendo o valor "2" =', numero_3) # ELIMINA A PRIMEIRA OCORRENCIA DO VALOR DESEJADO

if 4 in numero_3:
    numero_3.remove(4)
else:
    print('Não achei o número 4.')

if 5 in numero_3:
    numero_3.remove(5)
    print('Lista com o valor "5" removido =', numero_3)
else:
    print('Não achei o número 5.')

# EXEMPLO 3
print('\n{:=^30}' .format(' EXEMPLO 3 '))

# PODEMOS COMECAR UMA LISTA DE DUAS MANEIRAS:
# valores = []
# valores = list()

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print('Valores =', valores)

"""del(valores)
print('Deletando a Valores =', valores)"""

"""for i in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print("Cheguei ao final da lista!")"""

# EXEMPLO 4
print('\n{:=^30}' .format(' EXEMPLO 4 '))

# LIGANDO DUAS LISTAS
a = [2, 3, 4, 7]
print(f'Lista A = {a}')
b = a
b[2] = 8
print(f'Lista A = {a}')
print(f'Lista B = {b}')
print('\n')

# COPIANDO DUAS LISTAS
c = [2, 3, 4, 7]
d = c[:]
d[2] = 8
print(f'Lista C = {c}')
print(f'Lista D = {d}')
