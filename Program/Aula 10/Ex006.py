"""[Exercício 6] [DESAFIO] Escreva um programa que o usuário
digite uma expressão matemática qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está
com os parênteses abertos e fechados na ordem correta."""


# EXERCICIO 6
parenteses = list()
expressao = str(input("Digite a expressão: ")).upper().strip().split()
expressao = ''.join(expressao)
for simbolo in expressao:
    if simbolo == '(':
        parenteses.append(simbolo)
    elif simbolo == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break
if len(parenteses) == 0:
    print("Sua expressão está \033[034mCORRETA\033[m!")
else:
    print("Sua expressão está \033[031mERRADA\033[m!")

