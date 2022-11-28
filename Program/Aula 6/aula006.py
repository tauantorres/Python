"""# EXEMPLO 1
for c in range(1, 6): # range(incio , fim) -> [inicio, fim)
    print('{}) Hello, world!' .format(c))
print('FIM!\n')

# EXEMPLO 2
for c in range(1, 10, 2):
    print('{}) Hello, world!' .format(c))
print('FIM!\n')


# EXEMPLO 3
for c in range(10 , 0, -1): # range(inicio, fim, passo)
    print('{}) Hello, world!' .format(c))
print('FIM!\n')

# EXEMPLO 4
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    print('{}) Hello, world!' .format(c))
print('FIM!\n')

# EXEMPLO 5
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

for c in range(inicio, fim + 1, passo):
    print('{}) Hello, world!' .format(c))
print('FIM!\n')"""

# EXEMPLO 6
soma = 0
for c in range(0, 4):
    n = int(input('Digite um número:'))
    soma = soma + n # s += n
print('FIM!')
print('A soma é igual a {}' .format(soma))

