"""[Exercício 2] Escreva um programa que leia um número
entre 0 e 9999 e mostre cada um dos dígitos separados
mostrando quantas unidades, dezenas, centenas e milhares há nesse número."""

# SOLUÇÃO COM STRINGS
n1 = int(input('Digite um número entre 0 e 9999: '))
n2 = str(int(10000 + n1))
print('Milhares: {}'.format(n2[1]))
print('Centenas: {}'.format(n2[2]))
print('Dezenas: {}'.format(n2[3]))
print('Unidades: {}'.format(n2[4]))

# SOLUÇÃO MATEMÁTICA
N = int(input("Digite um número inteiro entre 0 e 9999: "))
unidade = N%10
print("Unidade = {}".format(unidade))
dezena = (N//10)%10
print("Dezena = {}".format(dezena))
centena = (N//100)%10
print("Centezas = {}".format(centena))
milhar = (N//1000)%10
print("Milhar = {}".format(milhar))
