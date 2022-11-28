"""[Exercício 2] Escreva um programa que uma tupla com
uma “lista de tops”. (Ex: Campeonato Brasileiro de Futebol,
ou os países que mais ricos do mundo e etc). Depois mostre:
1)	A penas os 5 primeiros colocados;
2)	Os últimos 4 colocados;
3)	Imprimir eles na tela com todos em ordem alfabética;
4)	Em que país estará um dos itens a sua escolha."""

# EXERCICIO 2
pessoas = ('Tauan', 'Kristina', 'Pedro', 'Kevin', 'Alba', 'Rogério')
print(f"Lista = {pessoas}")
print(f"Os três primeiros da lista: {pessoas[:3]}")
print(f"Os três últimos da lista: {pessoas[-3:]}")
print(f"Os nomes em ordem alfabética: {sorted(pessoas)}")
print(f"A posição de {pessoas[pessoas.index('Kristina')]} é {pessoas.index('Kristina') + 1}°.")

