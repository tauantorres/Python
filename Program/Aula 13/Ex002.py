"""[Exercício 2] Escreva um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem com
tamanho adaptável aos tamanho do texto.Faça isso quantas vezes o usuário quiser."""


# EXERCICIO 2
def escreva(txt):
    t = len(txt) + 4
    print("=" * t)
    #print(f"{txt:^{t}}")
    print(txt.center(t))
    print("=" * t)


def invalida():
    txt = '< RESPOSTA INVÁLIDA >'
    t = len(txt) + 6
    print(f"\033[31m{txt:=^{t}}\033[m")


# MAIN FUNCTION
while True:
    msg = str(input("Digite seu texto: ")).strip()
    escreva(msg)

    resposta = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
    while resposta not in 'SN':
        invalida()
        resposta = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
    if resposta == 'N':
        break

print(f"{'< FIM DO PRORGAMA >':^25}")

