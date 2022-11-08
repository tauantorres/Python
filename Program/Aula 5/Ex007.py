"""[Exercício 7] Refaça o exercício 6, mas acrescentando se o
triângulo, caso seja formado, é: EQUILÁTERO, ISÓCELES ou ESCALENO."""

l1 = float(input("L1 = "))
l2 = float(input("L2 = "))
l3 = float(input("L3 = "))

v1 = (l1 < l2 + l3)
v2 = (l2 < l1 + l3)
v3 = (l3 < l2 + l1)

if v1 and v2 and v3:
    print("GERA UM TRIÂNGULO")
    if l1 == l2 == l3:
        print("EQUILÁTERO")
    elif l1 != l2 != l3 != l1:
        print("ESCALENO")
    else:
        print("ISÓCELES")
else:
    print("NÃO GERA UM TRIÂNGULO")

