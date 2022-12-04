"""# EXEMPLO 1
def linha():
    print("=" * 30)

linha()
print(f"{'SENAC':^30}")
linha()


# EXEMPLO 2
def head(msg):
    print("=" * 30)
    print(f"{msg:^30}")
    print("=" * 30)


# main function:
head('SENAC')


# EXEMPLO 3
def soma(n1, n2):
    s = n1 + n2
    print(f"{n1} + {n2} = {s}")


# main function:
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
soma(n1, n2)


# EXEMPLO 4
def lin():
    print('=' * 30)


def mult(n1, n2):
    lin()
    print(f"N1 = {n1} e N2 = {n2}")
    print(f"2 X {n1} = {2 * n1}")
    print(f"2 X {n2} = {2 * n2}")
    lin()


# main function:
x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))
mult(n1=x, n2 =y)
mult(n1=y, n2=x)


# EXEMPLO 5
def contador(* parametro):
    print(parametro)


# MAIN FUNCTION
contador(1, 2, 3, 4)
contador(0, 1, 0, 1, 0, 1)
contador(2, 0)


# EXEMPLO 6
def contador(* parametro):
    for valor in parametro:
        print(f"{valor}", end=' ')
    print('- FIM!')


# MAIN FUNCTION
contador(1, 2, 3, 4)
contador(0, 1, 0, 1, 0, 1)
contador(2, 0)


# EXEMPLO 7
def contador(* parametro):
    tamanho = len(parametro)
    print(f"Recebi os valores {parametro} e são ao todo {tamanho} números.")


# MAIN FUNCTION
contador(1, 2, 3, 4)
contador(0, 1, 0, 1, 0, 1)
contador(2, 0)


# EXEMPLO 8
def dobro(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1


# MAIN FUNCTION
valores = [1, 2, 3, 4, 5, 6]
dobro(valores)
print(valores)


# EXEMPLO 9
def triplo(lista):
    for i in range(0, len(lista)):
        lista[i] *= 3


# MAIN FUNCTION
valores = [1, 2, 3, 4, 5, 6]
triplo(valores)
print(valores)"""


# EXEMPLO 10
def soma(* valores):
    s = 0
    for numero in valores:
        s += numero
    print(f"Somando os valores {valores} temos {s}.")


# MAIN FUNCTION
soma(1, 2)
soma(3, 4, 5)

