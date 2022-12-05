"""[Exercício 2] Adapte o código do exercício 1,
criando uma função adicional chamada moeda()
que consiga mostrar os valores com um valor monetário formatado."""

# EXERCÍCIO 2
import moeda

valor = float(input("Digite o preço: R$"))
moeda.resumo(valor)