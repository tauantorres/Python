# EXEMPLO 1
numero = soma = 0
while True:
    numero = int(input("Digite um número [999 to exit]: "))
    if numero == 999:
        break
    soma += numero
print(f"A soma vale {soma}.")
