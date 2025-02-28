import http.client
import json
import pandas as pd

def obter_endereco_por_cep(cep):
    conexao = http.client.HTTPSConnection('viacep.com.br')
    conexao.request('GET', f"/ws/{cep}/json/")
    resposta = conexao.getresponse()
    dados = resposta.read()
    endereco = json.loads(dados.decode('utf-8'))
    conexao.close()
    return endereco

def salvar_endereco_excel(endereco, nome_arquivo="enderecos.xlsx"):
    if"erro" not in endereco:
        df = pd.DataFrame([endereco])
        df.to_excel(nome_arquivo, index=False)
        print(f"Endereço salvo em {nome_arquivo}")
    else:
        print("CEP não encontrado.")
cep_exemplo = "88099-899"
endereco_resultado = obter_endereco_por_cep(cep_exemplo)
salvar_endereco_excel(endereco_resultado)
