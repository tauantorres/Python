"""[Exercício 4] Escreva um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros aleatoriamente.
Seu programa tem  que analisar todos os valores e dizer qual deles é o maior."""

# EXERCICIO 4
def linha(comprimento, opcao):
    d = comprimento

    if opcao == 1:
        print('=' * d)

    if opcao == 2:
        print(f"{'< RESULTADOS >':=^{d}}")


def invalido(saida):
    txt = 'RESPOSTA INVÁLIDA!'
    d = len(txt) * 4
    txt1 = 'Isso não é um número. Tente novamente.'
    txt2 = 'Isso não é uma letra. Tente novamente.'
    txt3 = 'Opção não existe. Tente novamente.'

    if saida == 1:  # ЭТО НЕ ЧИСЛА
        print(f"{'=' * d}\n\033[31m{txt:^{d}}\033[m\n{txt1:^{d}}\n{'=' * d}")
    if saida == 2:  # ЭТО НЕ БУКВА, УВАК
        print(f"{'=' * d}\n\033[31m{txt:^{d}}\033[m\n{txt2:^{d}}\n{'=' * d}")
    if saida == 3:  # ВЫБОР НЕ СУЩЕСТВУЕТ
        print(f"{'=' * d}\n\033[31m{txt:^{d}}\033[m\n{txt3:^{d}}\n{'=' * d}")


def maior(lista):
    linha(50, 2)
    print(f"Você digitou os valores: {lista}.")
    print(f"Ao total são {len(lista)} números.")
    print(f"O maior valor digitado foi {max(lista)}")
    linha(50, 1)


# MAIN FUNCTION
valores = list()

while True:

    auxiliar = input("Digite um número: ")
    while not auxiliar.isnumeric():
        invalido(1)
        auxiliar = input("Digite um número: ")

    auxiliar = int(auxiliar)
    valores.append(auxiliar)

    resposta = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]

    while resposta not in 'SN':
        invalido(3)
        resposta = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]

    if resposta == 'N':
        break

maior(valores)
