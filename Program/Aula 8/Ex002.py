"""[Exercício 2] Escreva um programa que
mostre a tabuada de vários números, um
de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido
quando o número solicitado for negativo."""

# EXERCICIO 2
while True:
    numero = int(input("Qual tabuada você deseja ver? "))

    if numero == 0:
        break
    else:
        print("="*30)
        print(f"{f'TABUADA DO {numero}':^30}")
        print("="*30)
        for i in range(1, 11):
            print(f"{i} x {numero} = {i * numero}")
        print("=" * 30)
print("=" * 30)
print(f"{f'ORIGADO PELA SUA PARTICIPAÇÃO':^30}")
print("=" * 30)


