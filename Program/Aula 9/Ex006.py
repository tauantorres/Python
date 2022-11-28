"""[Exercício 6] Escreva um programa que tenha uma tupla
com várias palavras (não usar acentos). Depois disso,
você deve mostrar, para cada palavra, quais são as suas vogais."""

# EXERCICIO 6
palavras = ('Amigos', 'tAUAN', 'uNiVeRsIdAdE')
for palavra in palavras:
    print(f"\nNa palavra {palavra.upper()} temos ", end='')
    for i in range(0, len(palavra)):
        if palavra[i:i+1].lower() in 'aeiou':
            print(palavra[i:i+1].lower(), end=' ')



