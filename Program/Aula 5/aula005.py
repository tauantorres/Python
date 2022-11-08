"""# ESTRUTURAS CONDICIONAIS 2

if <condição_1>:
    Bloco_1
elif <condição_2>:
    Bloco_2
elif <condição_n>:
    Bloco_n
else:
    <Bloco_(n+1)>

# EXEMPLO 1
nome = str(input('Qual o seu nome? ')).strip()

if nome == 'Tauan':
    print('Que nome bonito, {}!' .format(nome))
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil, {}!' .format(nome))
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!' .format(nome))"""

import datetime
print(f"A DATA de hoje é: {datetime.date.today()}")
print(f"DIA = {datetime.date.today().day}")
print(f"MÊS = {datetime.date.today().month}")
print(f"ANO = {datetime.date.today().year}")


