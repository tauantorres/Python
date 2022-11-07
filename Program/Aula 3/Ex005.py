"""[Exercício 5] Escreva um programa que leia um frase e mostre:
1)	Quantas vezes aparece a letra “A”;
2)	Em que posição ela aparece pela primeira vez;
3)	Em que posição aparece pela última vez."""

frase = str(input("Digite uma frase: ")).strip()
print("Existe {} 'A's na frase '{}'".format(frase.upper().count("A"), frase))
print("O primeiro 'A' aparece na posição {}".format(1 + frase.upper().find("A")))
posicao_ultimo_A = len(frase) - frase[len(frase) - 1::-1].upper().find("A") - 1
print("A posição do último 'A' é {} em uma contagem partindo do 1.".format(posicao_ultimo_A + 1))
print("A posição do último 'A' é {} em uma contagem partindo do 1.".format(frase.upper().rfind("A") + 1)) # SOLUÇÃO ALTERNATIVA
