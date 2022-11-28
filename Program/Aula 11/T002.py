turma = [[0, 'Tauan Torres', 7.2, 9.8, 6.5],
        [1, 'Kristina Shirosh', 6, 6, 10],
        [2, 'Pedro Henrique', 8, 6, 6.9],
        [3, 'Anouk Zhirosh Torres', 5, 9, 7]]

mostrar = -1
txt = f'CADASTRO '
p = len(txt) * 4 + 10

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
