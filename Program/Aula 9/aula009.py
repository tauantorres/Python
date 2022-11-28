"""lanches = () [] {}
() - Tupla
[] - Lista
{} - Dicionario
"""
print('=' * 30)
print('\033[34m{:^30}\033[m' .format('AULA DE TUPLAS'))
print('=' * 30)

# DECLARANDO A TUPLA
print('=' * 30)
print('\033[31m{:^30}\033[m' .format('EXEMPLO 1'))
print('=' * 30)

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') # TUPLA SÃO IMUTÁVEIS!!!!!!!!!!
# lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'

print('DECLARANDO A TUPLA:')
print("lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')")
print('\n')

# IMPRIMINDO A TUPLA
print('=' * 30)
print('\033[31m{:^30}\033[m' .format('EXEMPLO 2'))
print('=' * 30)

print('IMPRIMINDO A TUPLA: ')
#print(lanche)
print("print(lanche) = {}" .format(lanche))
print('\n')

# IMPRIMIR ELEMENTOS SEPARADAMENTE NA ORDEM DIRETA
print('=' * 30)
print('\033[31m{:^30}\033[m' .format('EXEMPLO 3'))
print('=' * 30)

print('IMPRIMIR ELEMENTOS SEPARADAMENTE NA ORDEM DIRETA:')
print('lanche[0] = {}' .format(lanche[0]))
print('lanche[1] = {}' .format(lanche[1]))
print('lanche[2] = {}' .format(lanche[2]))
print('lanche[3] = {}' .format(lanche[3]))
print('\n')

# IMPRIMIR ELEMENTOS SEPARADAMENTE NA ORDEM INVERSA
print('=' * 30)
print('\033[31m{:^30}\033[m' .format('EXEMPLO 4'))
print('=' * 30)

print('IMPRIMIR ELEMENTOS SEPARADAMENTE NA ORDEM INVERSA:')
print('lanche[-4] = {}' .format(lanche[-4]))
print('lanche[-3] = {}' .format(lanche[-3]))
print('lanche[-2] = {}' .format(lanche[-2]))
print('lanche[-1] = {}' .format(lanche[-1]))
print('\n')

# IMPRIMIR ELEMENTOS PULANDO ALGUNS
print('=' * 30)
print('\033[31m{:^30}\033[m' .format('EXEMPLO 5'))
print('=' * 30)

print('IMPRIMIR ELEMENTOS PULANDO ALGUNS: ')
print('lanches[1:3] = {}' .format(lanche[1:3])) # LEMBRANDO: O último elemento durante um fatiamento é sempre ignorado
print('lanches[2:] = {}' .format(lanche[2:]))
print('lanches[:2] = {}' .format(lanche[:2]))
print('lanches[-2:] = {}' .format(lanche[-2:]))
print('\n')

# USANDO FOR COM TUPLAS
print('=' * 30)
print('\033[31m{:^30}\033[m' .format('EXEMPLO 6'))
print('=' * 30)

print('USANDO FOR COM TUPLAS: ')
for comida in lanche:
    print(f'Eu vou comer {comida}!')
print('Comi pra caramba!')

# TAMANHO DA TUPLA
print('=' * 30)
print('\033[31m{:^30}\033[m' .format('EXEMPLO 7'))
print('=' * 30)

print('TAMANHO DA TUPLA: ')
#print(lanche)
print(f"print(lanche) = {lanche}")
#print(len(lanche))
print(f"print(len(lanche)) = {len(lanche)}")
print('\n')

# OUTRAS FORMAS DE USAR FOR COM TUPLAS
print('=' * 30)
print('\033[31m{:^30}\033[m' .format('EXEMPLO 8'))
print('=' * 30)

print('OUTRAS FORMAS DE USAR FOR COM TUPLAS: ')
for contador in range(0 , len(lanche)):
    print("contador = {}" .format(contador))
print('\n')

# MAIS OUTRA FORMA DE USAR FOR COM TUPLA
print('=' * 30)
print('\033[31m{:^30}\033[m' .format('EXEMPLO 9'))
print('=' * 30)

print('OUTRAS FORMAS DE USAR FOR COM TUPLAS: ')
for contador in range(0 , len(lanche)):
    print("lanche = {}" .format(lanche[contador]))
print('\n')

# VISTO EM AULA
print('=' * 30)
print('\033[31m{:^30}\033[m' .format('EXEMPLO 10'))
print('=' * 30)
print('VISTO EM AULA:')

for contador in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[contador]} na posição {contador}')
print('\n')

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('\n')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('\n')

# COLOCAR EM ORDEM
print('=' * 30)
print('\033[31m{:^30}\033[m' .format('EXEMPLO 11'))
print('=' * 30)
print('COLOCAR EM ORDEM:')

#print(sorted(lanche))
print(f'print(sorted(lanche)) = {sorted(lanche)}')
print('\n')

# TUPLAS COM NUMEROS
print('=' * 30)
print('\033[31m{:^30}\033[m' .format('EXEMPLO 12'))
print('=' * 30)
print('TUPLAS COM NUMEROS:')

a = (2, 5, 4)
b = (5, 8, 1, 2)
print(f'a = {a}')
print(f'b = {b}')

c = a + b
print(f'c = a + b = {c}')

c = b + a
print(f'c = b + a = {c}')

#print(len(c))
print(f'print(len(c)) = {len(c)}')

#print(c.count(5))
print(f'print(c.count(5)) = {c.count(5)}') # CONTA QUANTAS VEZES ENCONTRA-SE "5" NA TUPLA

#print(c.index(8))
print(f'print(c.index(8)) = {c.index(8)}') # RETORNA A POSICAO DO NUMERO NA TUPLA

#print(c.index(2))
print(f'print(c.index(2)) = {c.index(2)}') # A PRIMEIRA VEZ QUE ELE VE O "2"

#print(c.index(2, 4))
print(f'print(c.index(2, 4)) = {c.index(2, 4)}') # c.index("VALOR BUSCADO", "PONTO DE PARTIDA")
print('\n')

# VARIAVEIS DENTRO DA TUPLA
print('=' * 30)
print('\033[31m{:^30}\033[m' .format('EXEMPLO 13'))
print('=' * 30)
print('VARIAVEIS DENTRO DA TUPLA')

pessoa = ('Kristina', 26, 'F', 60.0) # NOME, IDADE, SEXO, PESO
print(f'pessoa = {pessoa}')
del(pessoa)
print('del(pessoa)')
print("pessoa = NameError: name 'pessoa' is not defined")
