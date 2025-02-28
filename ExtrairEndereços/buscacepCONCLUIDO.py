import http.client
import json
import pandas as pd
import os

# Função para obter endereço por CEP
def obter_endereco_por_cep(cep):
    conexao = http.client.HTTPSConnection('viacep.com.br')
    conexao.request('GET', f"/ws/{cep}/json/")
    resposta = conexao.getresponse()
    if resposta.status != 200:
        conexao.close()
        return None
    dados = resposta.read()
    endereco = json.loads(dados.decode('utf-8'))
    conexao.close()
    return endereco if "erro" not in endereco else None

# Caminho completo da planilha
caminho_planilha = r"C:\Users\Joden\OneDrive\Área de Trabalho\CARREIRA PROGRAMAÇÃO\Projetos-RPA\Projetos-RPA\ExtrairEndereços\CEP.xlsx"

# Verifica se o arquivo existe
if not os.path.exists(caminho_planilha):
    print(f"Erro: O arquivo '{caminho_planilha}' não foi encontrado.")
    exit(1)

# Lendo a planilha
planilha_ceps = pd.read_excel(caminho_planilha, sheet_name="CEP")
ceps = planilha_ceps["CEP"].dropna()

# DataFrame para armazenar os resultados
resultados = pd.DataFrame(columns=["CEP", "Logradouro", "Bairro", "Localidade", "UF"])

# Para cada CEP, busca o endereço
for cep in ceps:
    endereco = obter_endereco_por_cep(str(cep).replace("-", ""))
    if endereco:
        nova_linha = pd.DataFrame([{
            "CEP": cep,
            "Logradouro": endereco.get("logradouro", ""),
            "Bairro": endereco.get("bairro", ""),
            "Localidade": endereco.get("localidade", ""),
            "UF": endereco.get("uf", "")
        }])
        resultados = pd.concat([resultados, nova_linha], ignore_index=True)

# Salvando os resultados na planilha
with pd.ExcelWriter(caminho_planilha, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    resultados.to_excel(writer, sheet_name="Dados", index=False)

print("Endereços salvos com sucesso!")