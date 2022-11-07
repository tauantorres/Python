"""[Exercício 1] Escreva um programa que leia
o nome completo de uma pessoa e mostre:
1)	O nome com todas as letras maiúsculas;
2)	O nome com todas as letras minúsculas;
3)	Quantas letras ao todo (sem considerar os espaços);
4)	Quantas letras tem o primeiro nome."""

nome = str(input("Qual o seu nome completo? ")).strip()
print("Nome em letras maiúsculas: {}".format(nome.upper()))
print("Nome em letras minúsculas: {}".format(nome.lower()))
print("Total de letras no nome: {}".format(len(''.join(nome.split()))))
print("Total de letras no nome: {}".format(len(nome) - nome.count(" "))) # SUGESTÃO DE RESPOSTA
print("O primeiro nome tem {} letras".format(len(nome.split()[0])))
print("O primeiro nome tem {} letras".format(nome.find(" "))) # SUGESTÃO DE RESPOSTA ALTERNATIVA
