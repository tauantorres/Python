"""[Exercício 1] Escreva um programa que leia
nome e média de um aluno, guardando também
a situação em um dicionário. No final, mostre
o conteúdo da estrutura na tela."""

# EXERCICIO 1
aluno = dict()
aluno['Nome'] = str(input("Nome do aluno(a): ")).title().strip()
aluno['Média'] = float(input(f"Média de {aluno['Nome']}: "))

print("-" * 30)
for chave, valor in aluno.items():
    print(f"{chave} é igual a {valor}.")

print("=" * 30)
print("Situação é igual a ", end='')
if aluno['Média'] >= 7.0:
    print(f"\033[34mAPROVADO\033[m")
elif 4 <= aluno['Média'] < 7:
    print(f"\033[33mRECUPERAÇÃO\033[m")
else:
    print(f"\033[31mREPROVADO\033[m")
print("=" * 30)
