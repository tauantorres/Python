"""# EXEMPLO 1
try:
    numerador = int(input("Numerador: "))
    denominador = int(input("Denominador: "))
    resposta = numerador/denominador
except Exception as erro:
    print(f"O problema encontrado foi: {erro.__class__}")
else:
    print(f"O resultado é {resposta:.2f}")
finally:
    print(f"{'< FIM DO PROGRAMA >':=^40}")"""

import urllib
import urllib.request

try:
    site = urllib.request.urlopen("https://www.google.com/")
except urllib.error.URLError:
    print("O Google \033[31mNÃO\033[m esta acessível no momento.")
else:
    print("O Google está acessível!")
