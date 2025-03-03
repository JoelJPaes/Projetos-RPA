# criando uma lista com range
quadrados = [x**2 for x in range(5)]
print(quadrados)  # [0, 1, 4, 9, 16]

#         Filtrando elementos (apenas pares)
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]

#Convertendo strings para maiúsculas
nomes = ["ana", "joão", "maria"]
nomes_maiusculos = [nome.upper() for nome in nomes]
print(nomes_maiusculos)  # ['ANA', 'JOÃO', 'MARIA']

# Criando uma lista de tuplas
pares = [(x, x**2) for x in range(5)]
print(pares)  # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]

#Compreensão de listas com `if-else`
resultado = ["par" if x % 2 == 0 else "ímpar" for x in range(6)]
print(resultado)  # ['par', 'ímpar', 'par', 'ímpar', 'par', 'ímpar']
