# 1. Função sem retorno
def saudacao():
    print("Olá, seja bem-vindo!")

saudacao()

# 2. Função com parâmetros
def soma(a, b):
    return a + b

print(soma(3, 4))  # 7

# 3. Função com valor padrão
def saudacao_nome(nome="Usuário"):
    print(f"Olá, {nome}!")

saudacao_nome("Carlos")  # Olá, Carlos!

# 4. Função com múltiplos parâmetros
def media(*notas):
    return sum(notas) / len(notas)

print(media(7, 8, 9, 10))  # 8.5

# 5. Função que retorna múltiplos valores
def operacoes(a, b):
    return a + b, a - b, a * b, a / b

print(operacoes(10, 2))  # (12, 8, 20, 5.0)
