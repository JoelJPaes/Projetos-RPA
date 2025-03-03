import http.client
import json
import pandas as pd

def limpar_cnpj(cnpj):
    return ''.join(filter(str.isdigit, str(cnpj)))

def obter_dados_empresa_por_cnpj(cnpj):
    cnpj = limpar_cnpj(cnpj)

caminho_planilha = r"C:\Users\Joden\OneDrive\Área de Trabalho\CARREIRA PROGRAMAÇÃO\CNPJ.xlsx"
planilha_cnpjs = pd.read_excel(caminho_planilha, sheet_name="CNPJ", dtype={'CNPJ': str})

resultados = []
for cnpj in planilha_cnpjs['CNPJ'].dropna():
    print(f"Lendo CNPJ: {cnpj}")

    dados_empresa = obter_dados_empresa_por_cnpj(str(cnpj))

