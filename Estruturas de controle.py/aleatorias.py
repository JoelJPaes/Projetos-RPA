## Testando valores considerados True ou False em if
# if 0:
#     print("Verdadeiro")
# else:
#     print("Falso")  # Será executado porque 0 é considerado False.

# if "Python":
#     print("Verdadeiro")  # Será executado porque a string não está vazia.
# if []:
#     print("Verdadeiro")
# else:
#     print("Falso")  # Será executado porque lista vazia é False.

# # Verificação simples de maioridade usando if  
# idade = int(input("Digite sua idade: "))  
# if idade >= 18:  
#     print("Você é maior de idade.")  # Executado  
# else:  
#     print("Você é menor de idade.")  # Executado  

# # Tratamento de erro com try-except para entrada inválida  
# try:  
#     idade = int(input("Digite sua idade: "))  
#     if idade >= 18:  
#         print("Você é maior de idade.")  
#     else:
#         print("Você é menor de idade.")  
# except ValueError:  
#     print("Por favor, digite um número válido.")  

# Loop while para perguntar idade até o usuário encerrar  
# while True:  
#     entrada = input("Digite sua idade ou 'encerrar' para sair: ")  
#     if entrada.lower() == "encerrar":  
#         print("Encerrando o programa.")  
#         break  # Sai do loop
#     try:  
#         idade = int(entrada)  
#         if idade >= 18:  
#             print("Você é maior de idade.")  
#         else:  
#             print("Você é menor de idade.")  
#     except ValueError:  
#         print("Por favor, digite um número válido ou 'encerrar' para sair.")  

# # Percorre a lista e verifica se cada idade é maior ou menor de idade
# idades = [12, 18, 25, 17, 30]
# for idade in idades:
#     if idade >= 18:
#         print(f"Idade {idade}: Maior de idade.")
#     else:
#         print(f"Idade {idade}: Menor de idade.")

# Definindo Funções com `def`
# def saudacao(nome):
#     print(f"Olá, {nome}! Bem-vindo ao Python.")

# saudacao("João")  
# saudacao("Maria")  
