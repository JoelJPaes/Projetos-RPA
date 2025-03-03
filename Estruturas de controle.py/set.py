#conjuntos\set

# 1. Criando um conjunto
numeros = {1, 2, 3, 4, 4, 5}
print(numeros)  # {1, 2, 3, 4, 5}  (sem repetição)

# 2. Adicionando elementos
numeros.add(6)
print(numeros)  # {1, 2, 3, 4, 5, 6}

# 3. Removendo elementos
numeros.remove(3)
print(numeros)  # {1, 2, 4, 5, 6}

# 4. Operações com conjuntos (união)
pares = {2, 4, 6, 8}
print(numeros | pares)  # União {1, 2, 4, 5, 6, 8}

# 5. Operações com conjuntos (interseção)
print(numeros & pares)  # Interseção {2, 4, 6}
