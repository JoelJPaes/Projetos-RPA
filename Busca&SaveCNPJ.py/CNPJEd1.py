import http.client
import json
import pandas as pd


def obter_dados_empresa(cnpj):
    conexão = http.client.HTTPSConnection("receitaws.com.br")
    conexão.request("GET", f"/v1/cnpj/{cnpj}")
    resposta = conexão.getresponse()
    print(f"Status da resposta HTTP: {resposta.status}")
    if resposta.status != 200:
        return{"Status": "ERROR", "Message": f"Resposta HTPP com status {resposta.status}"}
    dados = resposta.read()
    conexão.close()
    try:
        empresa = json.loads(dados)
        print(f"Empresa decodificada:{empresa}")
        return empresa
    except json.JSONDecoder as e:
        print(f"Erro ao decodificar JSON: {str(e)}")
        return{"status": "ERROR", "message": f"Erro ao decodificar JSON: {str(e)}"}
def salvar_dados_empresa(dados_empresa):
    if dados_empresa.get('status') != 'ERROR':
        dados_empresa = tratar_dados_aninhados(dados_empresa)
cnpj_exemplo = "33157312000162"
dados_empresa = obter_dados_empresa(cnpj_exemplo)
salvar_dados_empresa(dados_empresa)
print(dados_empresa)
