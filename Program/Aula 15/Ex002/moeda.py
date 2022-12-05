def linha(tamanho, txt='', sit=False):
    if sit == False:
        print('=' * tamanho)
    else:
        print(f"{txt:=^{tamanho}}")


def aumentar(valor = 0, porcento = 1):
    return print(f" => Aumentado 10%, temos {moeda((1 + porcento / 100) * valor)}.")


def diminuir(valor = 0, porcento = 1):
    return print(f" => Com o desconto de 13%, temos {moeda((1 - porcento / 100) * valor)}.")


def dobro(valor = 0):
    return print(f" => O dobro de {moeda(valor)} vale {moeda(2 * valor)}.")


def metade(valor = 0):
    return print(f" => A metade de {moeda(valor)} vale {moeda(valor / 2)}.")


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

