# EXERCICIO 2.2
valores = list()
while True:
    valor = int(input("Digite um valor: "))

    if valor not in valores:
        valores.append(valor)
        print("Valor adicionado com SUCESSO!")
    else:
        print("Esse valor JÁ EXISTE na lista.")

    resposta = str(input("Deseja continuar [S/N]?")).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input("RESPOSTA INVÁLIDA. Deseja continuar [S/N]?")).upper().strip()[0]
    if resposta == 'N':
        break
valores.sort()
print(f"Lista = {valores}")