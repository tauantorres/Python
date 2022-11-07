"""[Exercício 3] Escreva um programa que
leia o nome de uma cidade e informe se
ela começa com a palavra “Santo”."""

cidade = str(input("Qual o nome da cidade? ")).strip()
print("A cidade começa com 'Santo'? {}".format("SANTO" in cidade.upper().split()[0]))
print("A cidade começa com 'Santo'? {}".format(cidade[:5].upper() == "SANTO")) # SUGESTÃO DE RESPOSTA
