import http.client
import json


def obter_dados_empresa_por_cnpj(cnpj):
    conexao = http.client.HTTPSConnection('receitaws.com.br')
    conexao.request('GET', f"/v1/cnpj/{cnpj}")
    resposta = conexao.getresponse()
    dados = resposta.read()
    empresa = json.loads(dados.decode('utf-8'))
    conexao.close()
    return empresa

caminho_planilha = r"C:\Users\Joden\OneDrive\Área de Trabalho\CARREIRA PROGRAMAÇÃO\Projetos-RPA\Projetos-RPA\Busca&SaveCNPJ.py\CNPJ.xlsx"
for cnpj in cnpjs:
    
    empresa = obter_dados_empresa_por_cnpj(cnpj)
    if empresa.get("status", '') == 'ERROR':
        return empresa.get("message", 'Erro desconhecido')
    else:
        return empresa
if not os.path.exists(caminho_planilha):
    print(f"Erro: O arquivo '{caminho_planilha}' não foi encontrado.")
    exit(1)

planilha_cnpjs = pd.read_excel(caminho_planilha, sheet_name="CNPJ")
cnpjs = planilha_cnpjs["CNPJ"].dropna()

    if empresa.get("status", '') == 'ERROR':
        return empresa.get("message", 'Erro desconhecido')
    else:
        return empresa

cnpj_exemplo = "33157312000162"
dados_empresa = obter_dados_empresa_por_cnpj(cnpj_exemplo)

with pd.ExcelWriter(caminho_planilha, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    resultados.to_excel(writer, sheet_name="Dados", index=False)

print(dados_empresa)