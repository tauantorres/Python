"""[Exercício 1] Crie um módulo chamado moeda.py que:
1) Tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
2) Faça também um programa que importe esses módulos e use algumas dessas funções."""

# EXERCÍCIO 1
import moeda

valor = float(input("Digite o preço: R$"))
moeda.linha(40)
moeda.aumentar(valor, 10)
moeda.diminuir(valor, 13)
moeda.dobro(valor)
moeda.metade(valor)
moeda.linha(40, '< FIM DO PROGRAMA >', True)
