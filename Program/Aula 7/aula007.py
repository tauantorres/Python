# EXEMPLO 1
c = 1
while c <= 10:
    print(c)
    c += 1
print("--FIM--")

# EXEMPLO 2
resposta = 'S'
while resposta == 'S':
    valor = int(input("Digite um valor: "))
    resposta = str(input('Quer continuar? [S/N] ')).upper().split()[0]
print('FIM!')

# EXEMPLO 3
par = impar = 0
resposta = 'S'
while resposta == 'S':
    n = int(input('Digite um valor: '))

    if n % 2 == 0:
        par += 1
    else:
        impar += 1
    resposta = str(input("Você deseja continuar [S/N]? ")).upper().split()[0]
    while resposta not in 'SN':
        print("RESPOSTA INVÁLIDA!")
        resposta = str(input("Você deseja continuar [S/N]? ")).upper().split()[0]

print('Você digitou {} valor pares e {} valores ímpares.' .format(par, impar))
