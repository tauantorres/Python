"""[Exercício 5] Escreva um programa que leia
o primeiro termo e a razão de uma PA, mostrando
os 10 primeiros termos da PA"""

# EXERCICIO 6
termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
inicio = 0
fim = 10
terminar = False

while not terminar:
    while inicio != fim:
        if inicio < (fim - 1):
            print(f"{termo}", end=' -> ')
        else:
            print(f"{termo}", end=' -> PAUSE')
        termo += razao
        inicio += 1

    mais = int(input("\nMais quantos termos? "))
    if mais == 0:
        terminar = True
    else:
        fim = fim + mais

print(f"\n{' FIM ':=^42}")
print(f"Progressão finalizada mostrando {fim} termos.")
print("="*42)
