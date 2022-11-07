
# input() -  Função de entrada de Dados
nome = input("Qual o seu nome? ")
idade = input("Quantos ano você tem? ")
peso = input("Qual o seu peso? ")

# print() - Função de saída de Dados
print(nome, idade, peso)
print("{}, você pesa {} e sua idade é de {} anos." .format(nome, peso, idade))

# type() - Função para verificação de dados
N1 = int(input("Primeiro número: "))
N2 = int(input("Segundo número: "))
print(type(N1), type(N2))
print("A soma vale {}" .format(N1+N2))

# .isSOMETHING() - Função que verifica qual tipo primitivo do que foi escrito
n = input("Digite algo: ")
print(n.isnumeric())

# Cabeçalho
nome = input("Qual o seu nome? ")
print("=" * 20)
print(" Bem-vindo, {}!" .format(nome))
print("=" * 20)

# Formatação da impressão

nome = str(input("Qual o seu nome? "))
print("Prazer em te conhecer, {:20}".format(nome))
print("Prazer em te conhecer, {:>20}".format(nome))
print("Prazer em te conhecer, {:<20}".format(nome))
print("Prazer em te conhecer, {:^20}".format(nome))
print("Prazer em te conhecer, {:=^20}".format(nome))

N1 = int(input("Primeiro numero: "))
N2 = int(input("Segundo numero: "))
print("A soma vale {:.2f}".format(N1 / N2))

# Subcomando end=''
print("Como continuar ", end='')
print("em outra linha!")






