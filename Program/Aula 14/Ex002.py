def linha(tamanho):
    print('=' * tamanho)


def fatorial(n, show=False):
    produto = 1
    linha(40)

    if show == False:
        for i in range(n, 0, -1):
            produto *= i
        print(f"{n}! = {produto}")

    else:
        print(f"{n}! = ", end=' ')
        for i in range(n, 0, -1):
            produto *= i
            print(f"{i}", end=' x ') if i != 1 else print(f"{i}", end=' ')
        print(f"= {produto}")
    linha(40)


def verificadorInteiro(caminho):
    if caminho == 1:

        numero = input("Você gostaria de ver o fatorial de qual número? ")
        while not numero.isnumeric():
            numero = input("Erro: Resposta inválida.\nVocê gostaria de ver o fatorial de qual número? ")
        numero = int(numero)

        return numero

    if caminho == 2:
        escolha = input(" => Opção:")
        while not escolha.isnumeric():
            print("Erro: Resposta Inválida! Isso não é um número. Tente novamente!")
            escolha = input(" => Opção:")
        escolha = int(escolha)

        return escolha

    if caminho == 3:
        print("Erro: Resposta Inválida! Digite 1 ou 2, por favor.")
        escolha = verificadorInteiro(2)

        return escolha


def opcao():
    linha(40)
    print("Escolha uma opção:")
    print("[1] - Mostrar a multiplicação;")
    print("[2] - Mostrar apenas o resultado.")
    linha(40)

    escolha = verificadorInteiro(2)
    while escolha not in range(1, 3):
        escolha = verificadorInteiro(3)
    return escolha


def VerdadeiroOuFalso(escolha):
    return True if escolha == 1 else False


# MAIN FUNCTION:
numero = verificadorInteiro(1)
escolha = opcao()
opcao = VerdadeiroOuFalso(escolha)
fatorial(numero, opcao)
