"""[Exercício 4] Escreva um programa que leia
duas notas do aluno, calcule a sua média e diga:
1)	Média abaixo de 5: REPROVADO
2)	Entre 5 e 6.9: RECUPERAÇÃO
3)	Acima de 7: APROVADO"""

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2)/2
print(f"Sua média foi {m:.2f}")
if m >= 7 :
    print("APROVADO")
elif 5 <= m < 7:
    print("RECUPEÇÃO")
else:
    print("REPROVADO")

