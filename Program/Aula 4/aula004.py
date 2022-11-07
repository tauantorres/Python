"""# CONDIÇÕES SIMPLES
if <boolean>:
    Bloco True
else:
    Bloco False"""

# EXEMPLO 1
idade = int(input("Quantos anos você tem? "))

if idade < 18:
    print("MENOR DE IDADE.")
else:
    print("MAIOR DE IDADE")

# EXEMPLO 2
idade = int(input("Quantos anos você tem? "))
print("MENOR DE IDADE" if idade < 18 else "MAIOR DE IDADE")

# EXEMPLO 3
nome = str(input("Qual o seu nome? ")).strip()
if nome.upper()[0] == "A":
    print("Nome iniciados com a letra 'A' são muito bonitos!")
print("Bom dia, {}!". format(nome))

# EXEMPLO 4
nome = str(input("Qual o seu nome? ")).strip()
if nome.upper()[0] == "A":
    print("Nome iniciados com a letra 'A' são muito bonitos!")
else:
    print("Seu nome é bem normal!")
print("Bom dia, {}!". format(nome))

# EXEMPLO 5
N1 = float(input("Informe a primeira nota: "))
N2 = float(input("Informe a segunda nota: "))
M = (N1 + N2)/2
print("Sua nota final é {}".format(M))
if M >= 7 :
    print("APROVADO")
else:
    print("REPROVADO")

# EXEMPLO 6
N1 = float(input("Informe a primeira nota: "))
N2 = float(input("Informe a segunda nota: "))
M = (N1 + N2)/2
print("Sua nota final é {}".format(M))
print("APROVADO" if M >= 7 else "REPROVADO")

