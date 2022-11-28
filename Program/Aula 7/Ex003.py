"""[Exercício 3] Escreva um programa que lerá
dois valores do usuário e mostre um menu na
tela dando as opções:
[1] – somar,
[2] – multiplicar,
[3] – maior,
[4] – novos números,
[5] – sair do programa.
Seu programa deverá realizar a operação solicitada em cada caso."""

# EXERCICIO 3
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
fim = False
while not fim:
    print('='*20)
    print(f"{'MENU':^20}")
    print('='*20)
    print('[1] - Somar;')
    print('[2] - Multiplicar;')
    print('[3] - Maior;')
    print('[4] - Novos números;')
    print('[5] - Sair.')
    print('='*20)
    opcao = int(input('Qual é a sua opção? '))
    while opcao not in range(1, 6):
        print('OPÇÃO INVÁLIDA!')
        opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        print(f"{' SOMA ':=^20}")
        soma = n1 + n2
        print(f"{f'{n1} + {n2} = {soma}':^20}")
    elif opcao == 2:
        print(f"{' MULTIPLICAR ':=^20}")
        produto = n1 * n2
        print(f"{f'{n1} X {n2} = {produto}':^20}")
    elif opcao == 3:
        print(f"{' MAIOR ':=^20}")
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior valor digita foi {maior}.')
    elif opcao == 4:
        print(f"{' RELEITURA ':=^20}")
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print(f"{' SAIR ':=^20}")
        fim = True
        print('PROGRAMA ENCERRADO')
print('--FIM--')
