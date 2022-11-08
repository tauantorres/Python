"""[Exercício 3] Escreva um programa que leia dois números
inteiros e compare-os, mostrando na tela a mensagem:
1)	“O primeiro valor é maior”
2)	“O segundo valor é maior”
3)	“Não existe valor maior, ambos são iguais”"""

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
maior = n1 > n2 and n1 or n2
menor = n1 < n2 and n1 or n2
if maior == menor:
    print("Não existe valor maior, ambos são iguais")
else:
    print(n1 > n2 and "O primeiro valor é maior" or "O segundo valor é maior")

