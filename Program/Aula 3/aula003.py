frase = "Mega adrenalina mode on"

# FATIAMENTO
print(frase[9:14]) # [inicio : fim]
print(frase[:14]) # [ 0 : fim]
print(frase[9:21:2]) #[inicio : fim : pulando de]
print(frase[15:]) #[inicio : ate o final]
print(frase[9::3]) #[inicio : ate o final : pulando de]

# ANALISE
len(frase) # tamanha ta string
print(len(frase))
print(frase.count('o')) #conta quantas vezes aparece o caracter 'o'
print(frase.upper().count('o')) #Maisculas e depois procura 'o'
print(frase.count('o', 0, 13)) #quantos 'o' entre [0, 13)
print(frase.find('deo')) # em que momemnto comecou o 'deo'
print('Curso' in frase) #"Encontramos 'Curso' em 'frase'? True or False

# TRANSFORMACAO
print(frase.replace('Phyton', "Android")) #Substitui uma palavra por outra
print(frase.upper()) #Escreve tudo em letra maiuscula
print(frase.lower()) #Tudo em minusculo
print(frase.capitalize())
print(frase.title())
nova_frase = '   Aprenda Phyton  '
print(nova_frase)
print(nova_frase.strip()) #Remove os espacos inuteis em ambos os lados
print(nova_frase.rstrip()) #Remove os espacos inuteis pela esquerda
print(nova_frase.lstrip()) #Remove os espacos inuteis pela direita

# DIVISAO
lista = frase.split()
print(lista)

# JUNCAO
print('-'.join(lista))
print(lista[2][3]) # o segundo elemente da lista e o 3 letra desse elemento (lembrando que inicia no 0)


print('')
print("""Álvaro de Campos\n
Todas as cartas de amor são\n
Todas as cartas de amor são
Ridículas.

Não seriam cartas de amor se não fossem
Ridículas.
Também escrevi em meu tempo cartas de amor,
Como as outras,
Ridículas.

As cartas de amor, se há amor,
Têm de ser
Ridículas.

Mas, afinal,
Só as criaturas que nunca escreveram
Cartas de amor
É que são
Ridículas.

Quem me dera no tempo em que escrevia
Sem dar por isso
Cartas de amor
Ridículas.

A verdade é que hoje
As minhas memórias
Dessas cartas de amor
É que são
Ridículas.

(Todas as palavras esdrúxulas,
Como os sentimentos esdrúxulos,
São naturalmente
Ridículas).""")



