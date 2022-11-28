"""[Exercício 6] [DESAFIO] Escreva um programa que leia nome
e duas notas de vários alunos e guarde tudo em uma lista
composta. No final, mostre um boletim contendo a média de
cada um e permita que o usuário possa mostrar as notas de
cada aluno individualmente."""

# EXERCICIO 6

turma = list()
aluno = list()
contador = 0
mostrar = -1
txt = f'CADASTRO '
p = len(txt) * 4 + 10
while True:
    print(f"{'=' * p}\n\033[34m{f'CADASTRO {contador + 1}':^{p}}\033[m\n{'=' * p}")
    aluno.append(contador)
    aluno.append(str(input("Nome: ")).strip().title())
    aluno.append(float(input("Nota 1: ")))
    aluno.append(float(input("Nota 2: ")))
    aluno.append((aluno[2] + aluno[3]) / 2)
    turma.append(aluno[:])
    aluno.clear()
    contador += 1

    resposta = str(input("Deseja continuar[S/N]? ")).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input(f"{f'=' * p}\n\033[031m{f'RESPOSTA INVÁLIDA!':^{p}}\033[m\n{f'=' * p}\nDeseja continuar[S/N]? ")).upper().strip()[0]
    if resposta == 'N':
        break

print(f"{f'=' * p}\n{f'No.':^8}{f'NOME':^30}{f'MÉDIA':<40}\n{f'=' * p}")
for aluno in turma:
    print(f"{f'[{aluno[0]}] ':<8}", end='')
    print(f"{f'{aluno[1]} ':^30}", end='')
    if aluno[4] < 7:
        print(f"\033[031m{f'{aluno[4]:.2f}':<50}\033[m")
    else:
        print(f"\033[034m{f'{aluno[4]:.2f}':<50}\033[m")
print("=" * p)

while True:
    if mostrar == 999:
        break
    mostrar = int(input("Deseja mostrar qual aluno [999 to Exit]? "))
    if mostrar == 999:
        break
    while mostrar not in range(0, len(turma)):
        mostrar = int(input(f"{f'=' * p}\n\033[031m{f'RESPOSTA INVÁLIDA!':^{p}}\033[m\n{f'=' * p}\nDeseja mostrar qual aluno [999 to Exit]? "))
        if mostrar == 999:
            break

    if mostrar < len(turma):
        print("=" * p)
        print(f"Aluno(a): \033[033m{turma[mostrar][1]}\033[m.")
        if turma[mostrar][2] < 7:
            print(f"1o Notas = [\033[031m{turma[mostrar][2]:.2f}\033[m]")
        else:
            print(f"1o Notas = [\033[034m{turma[mostrar][2]:.2f}\033[m]")

        if turma[mostrar][3] < 7:
            print(f"2o Notas = [\033[031m{turma[mostrar][3]:.2f}\033[m]")
        else:
            print(f"2o Notas = [\033[034m{turma[mostrar][3]:.2f}\033[m]")
        print("=" * p)

print(f"{f'=' * p}\n{f'< VOLTE SEMPRE >':^{p}}\n{f'=' * p}")

"""print(f"{f'=' * p}\n{f'No.':^8}{f'NOME':^30}{f'MÉDIA':<40}\n{f'=' * p}")
for aluno in turma:
    print(f"{f'[{aluno[0]}] ':^8}{aluno[1]:^30}{aluno[4]:<40}")
print("=" * p)

while True:
    if mostrar == 999:
        break
    mostrar = int(input("Deseja mostrar qual aluno [999 to Exit]? "))
    if mostrar == 999:
        break
    while mostrar not in range(0, len(turma)):
        mostrar = int(input(f"{f'=' * p}\n\033[031m{f'RESPOSTA INVÁLIDA!':^{p}}\033[m\n{f'=' * p}\nDeseja mostrar qual aluno [999 to Exit]? "))
        if mostrar == 999:
            break

    if mostrar < len(turma):
        print(f"Aluno(a): {turma[mostrar][1]}. Notas: [{turma[mostrar][2]}] [{turma[mostrar][3]}]")
        print("=" * p)

print(f"{f'=' * p}\n{f'< VOLTE SEMPRE >':^{p}}\n{f'=' * p}")
"""