txt_1 = f'RESPOSTA INVÁLIDA'
t = len(txt_1) + 8
txt_2 = f"{'=' * t}\n\033[31m{txt_1:^{t}}\033[m\n{'=' * t}"

while True:

    resposta = input("Quer continuar [S/N]? ")

    while resposta.upper().strip()[0] not in 'SN' or not resposta.isalpha():
        if resposta.upper().strip()[0] not in 'SN':
            print("TESTE 1")
        elif not resposta.strip().isalpha():
            print("TESTE 2")

        resposta = input(f"{txt_2}\nQuer continuar [S/N]? ")

    resposta = str(resposta.upper().strip()[0])
    if resposta == 'N':
        break

print(f"{f'< FIM DO PROGRAMA >':-^30}")