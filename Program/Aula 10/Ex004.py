"""[Exercício 4] Escreva um programa que
vai ler vários valores numéricos e colocar
eles em uma lista. No final, mostre:
1)	Quantos números foram digitados;
2)	A lista de valores digitados, ordenada de forma crescente;
3)	Se o valor 5 foi digitado e está ou não na lista."""

# EXERCICIO 4.1
numeros = list()
while True:
    numeros.append(int(input("Digite um valor: ")))

    resposta = str(input("Deseja continuar [S/N]:")).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input("\033[031mRESPOSTA INVÁLIDA!\033[m \nDeseja continuar [S/N]:")).upper().strip()[0]
    if resposta == 'N':
        break

numeros.sort(reverse=True)
print(f"Você digitou {len(numeros)} números.")
print(f"A lista que você digitou em ordem decrescente é {numeros}")
if 5 in numeros:
    print("O valor 5 faz parte da lista.")
else:
    print("O valor 5 \033[031mnão\033[m faz parte da lista.")
