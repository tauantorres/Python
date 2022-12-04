auxiliar = input(f"Digite seu peso: ")
while auxiliar.isnumeric() != True:
    print("RESPOSTA INVALIDA")
    auxiliar = input("Digite um numero: ")
auxiliar = int(auxiliar)
print(type(auxiliar))