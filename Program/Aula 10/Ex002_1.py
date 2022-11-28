"""[Exercício 2] Escreva um programa que o usuário
escreverá vários valores numéricos e cadastre-os
em uma lista. Caso o número já exista lá dentro,
ele não será adicionado. No final, serão exibidos
todos os valores únicos digitados, e em ordem crescente.
1) Ler varios valores
2) Verificar se o numero ja existe
3) Nao adicionar caso ja exista
4) Mostrar a lista em ordem crescente"""

# EXERCICIO 2.2
valores = list()
while True:
    valor = int(input("Digite um valor: "))

    contador = 0
    for i in range(0, len(valores)):
        if valor == valores[i]:
            contador += 1
    if contador >= 1:
        print("Esse valor JÁ EXISTE na lista.")
    else:
        valores.append(valor)
        print("Valor adicionado com SUCESSO!")

    resposta = str(input("Deseja continuar [S/N]?")).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input("RESPOSTA INVÁLIDA. Deseja continuar [S/N]?")).upper().strip()[0]
    if resposta == 'N':
        break
valores.sort()
print(f"Lista = {valores}")


