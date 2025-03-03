# 1. Criando uma tupla
numeros = (1, 2, 3, 4, 5)

# 2. Acessando elementos
print(numeros[2])  # 3

# 3. Desempacotamento de tupla
a, b, c, d, e = numeros
print(a, b, c, d, e)  # 1 2 3 4 5

# 4. Verificando se um valor está na tupla
print(3 in numeros)  # True

# 5. Concatenando tuplas
outra_tupla = (6, 7, 8)
nova_tupla = numeros + outra_tupla
print(nova_tupla)  # (1, 2, 3, 4, 5, 6, 7, 8)
