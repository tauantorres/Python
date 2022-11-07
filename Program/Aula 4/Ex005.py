"""[Exercício 5] Escreva um programa que
leia um ano qualquer e mostre se ele é BISSEXTO."""

import datetime

ano = int(input('Digite um ano (Coloque 0 para analizar o seu ano atual): '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano BISSEXTO!' .format(ano))
else:
    print('{} NÃO é um ano BISSEXTO!' .format(ano))
