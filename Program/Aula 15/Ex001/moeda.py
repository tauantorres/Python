def linha(tamanho, txt='', sit=False):
    if sit == False:
        print('=' * tamanho)
    else:
        print(f"{txt:=^{tamanho}}")


def aumentar(valor, porcento):
    return print(f" => Aumentado 10%, temos R${(1 + porcento / 100) * valor:.2f}.")


def diminuir(valor, porcento):
    return print(f" => Com o desconto de 13%, temos R${(1 - porcento / 100) * valor:.2f}.")


def dobro(valor):
    return print(f" => O dobro do valor vale R${2 * valor:.2f}.")


def metade(valor):
    return print(f" => A metade do valor vale R${valor / 2:.2f}.")
