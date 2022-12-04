"""[Exercício 3] Escreva um programa que leia:
1) Nome, ano de nascimento e carteira de trabalho;
2) Cadastre-os (com idade) em um dicionário se por acaso a
   CTPS (Carteira de Trabalho e Previdência Social) for diferente de ZERO;
3) O dicionário receverá também o ano de contratação e o salário;
4) Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
   (Considere 35 anos de colaboração para se aposentar)"""

# EXERCICIO 3
import datetime
pessoa = dict()

txt = f'RESPOSTA INVÁLIDA'
t = len(txt) + 24

# ENTRADA -  DO NOME DO USUARIO
pessoa['Nome'] = str(input("Digite seu nome: ")).strip().title()

# ENTRADA - DO ANO DE NASCIMENTO
ano = input("Ano de nascimento: ").strip()

# QA - CTPS
while not ano.isnumeric() or len(ano) != 4:
    print(f"{'=' * t}\n\033[31m{txt:^{t}}\033[m\n{f'Formato do tipo: YYYY':^{t}}\n{'=' * t}")
    ano = input(f"Ano de nascimento: ").strip()
ano = int(ano)
pessoa['Idade'] = datetime.datetime.now().year - ano

# ENTRADA - CTPS
pessoa['Carteira de Trabalho'] = input("Carteira de Trabalho [0 não tem]:").strip()

# QA - CTPS
while not pessoa['Carteira de Trabalho'].isnumeric() or len(pessoa['Carteira de Trabalho']) != 8:
    print(f"{'=' * t}\n\033[31m{txt:^{t}}\033[m\n{f'A CTPS deve ter 8 dígitos.':^{t}}\n{'=' * t}")
    pessoa['Carteira de Trabalho'] = input("Carteira de Trabalho [0 não tem]:").strip()
pessoa['Carteira de Trabalho'] = int(pessoa['Carteira de Trabalho'])

if pessoa['Carteira de Trabalho'] == '0':

    print('=' * t)
    for chave, valor in pessoa.items():
        print(f"{chave:.<{len(txt) * 2}} {valor:<{len(txt) - 16}}")
    print(f"{f'< FIM DO PROGRAMA >':=^{t}}")

else:

    # ENTRADA - ANO DE CONTRATAÇAO
    pessoa['Ano de Contratação'] = input("Ano de contratação: ").strip()

    # QA - ANO DE CONTRATAÇÃO
    while not pessoa['Ano de Contratação'].isnumeric() or len(pessoa['Ano de Contratação']) != 4 or (int(pessoa['Ano de Contratação']) -ano) <= 16:

        if not pessoa['Ano de Contratação'].isnumeric():
            print(f"{'=' * t}\n\033[31m{txt:^{t}}\033[m\n{f'Esse valor não é um número. Tente novamente.':^{t}}\n{'=' * t}")
        elif len(pessoa['Ano de Contratação']) != 4:
            print(f"{'=' * t}\n\033[31m{txt:^{t}}\033[m\n{f'Formato do tipo: YYYY':^{t}}\n{'=' * t}")
        elif (int(pessoa['Ano de Contratação']) - ano) <= 16:
            print(f"{'=' * t}\n\033[31m{txt:^{t}}\033[m\n{f'É preciso ser maior de idade por lei.':^{t}}\n{'=' * t}")

        pessoa['Ano de Contratação'] = input("Ano de contratação: ").strip()
    pessoa['Ano de Contratação'] = int(pessoa['Ano de Contratação'])
    pessoa['Aposentadoria'] = (pessoa['Ano de Contratação'] - ano) + 35

    # ENTRADA - SALÁRIO
    pessoa['Salário'] = float(input("Salário: R$"))

    print('=' * t)
    for chave, valor in pessoa.items():
        print(f"{chave:.<{len(txt)*2}} {valor:<{len(txt)-16}}")
    print(f"{f'< FIM DO PROGRAMA >':=^{t}}")
