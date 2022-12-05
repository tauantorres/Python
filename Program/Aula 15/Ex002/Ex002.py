"""[Exercício 2] Adapte o código do exercício 1,
criando uma função adicional chamada moeda()
que consiga mostrar os valores com um valor monetário formatado."""

# EXERCÍCIO 2
import moeda

valor = float(input("Digite o preço: R$"))
moeda.linha(40)
moeda.aumentar(valor, 10)
moeda.diminuir(valor, 13)
moeda.dobro(valor)
moeda.metade(valor)
moeda.linha(40, '< FIM DO PROGRAMA >', True)