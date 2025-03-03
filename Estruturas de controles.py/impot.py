# 1. Importando módulo inteiro
import math
print(math.sqrt(25))  # 5.0

# 2. Importando função específica
from random import randint
print(randint(1, 10))  # Número aleatório entre 1 e 10

# 3. Criando e importando um módulo próprio (exemplo: `meu_modulo.py`)
# Em meu_modulo.py:
# def ola(): print("Olá do módulo!")

# No arquivo principal:
# import meu_modulo
# meu_modulo.ola()  # "Olá do módulo!"

# 4. Usando `datetime`
import datetime
print(datetime.datetime.now())  # Exibe a data e hora atuais

# 5. Trabalhando com `os` para interagir com o sistema operacional
import os
print(os.getcwd())  # Retorna o diretório atual
