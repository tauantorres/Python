"""[Exercício 4] Escreva um programa que
pergunte a distância de uma viagem em Km.
Calcule e peça o preço da passagem, cobrando
R$ 0,50 por Km para viagens de até 200Km e
R$ 0,45 para viagens mais longas."""

S = float(input("Qual foi a distância percorrida [Km]? "))
if S <= 200:
    preco = S * 0.5
    print("Valor da passagem R${:.2f}".format(preco))
else:
    preco = S * 0.45
    print("Valor da passagem R${:.2f}".format(preco))
#preco = S*0.5 if S <= 200 else S*0.45
