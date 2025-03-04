import http.client  # Importa a biblioteca para requisições HTTP
import json  # Importa a biblioteca para manipulação de JSON
import pandas as pd  # Importa a biblioteca para manipulação de planilhas
import time  # Importa a biblioteca para pausas entre requisições

# Define o caminho do arquivo Excel contendo os CNPJs
caminho_planilha = r"C:\Users\Joden\OneDrive\Área de Trabalho\CARREIRA PROGRAMAÇÃO\CNPJ.xlsx"

# Lê a planilha especificando a aba e garantindo que a coluna 'CNPJ' seja string
planilha_cnpjs = pd.read_excel(caminho_planilha, sheet_name="CNPJ", dtype={'CNPJ': str})

resultados = []  # Lista para armazenar os resultados das consultas

def limpar_cnpj(cnpj):
    return ''.join(filter(str.isdigit, str(cnpj)))  # Remove caracteres não numéricos do CNPJ

def obter_dados_empresa_por_cnpj(cnpj):
    cnpj = limpar_cnpj(cnpj)
    
    try:
        conexao = http.client.HTTPSConnection("www.receitaws.com.br")
        conexao.request("GET", f"/v1/cnpj/{cnpj}")
        resposta = conexao.getresponse()
        print(f"Processando CNPJ {cnpj}: Status {resposta.status}")
        
        if resposta.status != 200:
            conexao.close()
            return None
            
        dados = resposta.read()
        conexao.close()
        empresa = json.loads(dados.decode('utf-8'))
        
        if "status" in empresa and empresa["status"] == "ERROR":
            print(f"Erro ao obter dados para o CNPJ {cnpj}: {empresa.get('message')}")
            return None  # Retorna None para evitar salvar dados inválidos
        
        return empresa
    except Exception as e:
        print(f"Erro ao consultar o CNPJ {cnpj}: {str(e)}")
        return None

def formatar_dados(empresa):
    campos_interesse = ['cnpj', 'nome', 'telefone', 'email', 'logradouro', 'bairro', 'municipio', 'uf', 'cep', 'atividade_principal']

    dados_formatados = {campo: empresa.get(campo, '') for campo in campos_interesse}

    if 'atividade_principal' in empresa and empresa['atividade_principal']:
        dados_formatados['atividade_principal'] = empresa['atividade_principal'][0].get('text', '')

    return dados_formatados 

def salvar_dados_empresa_excel(resultados, nome_arquivo, nome_aba='Dados'):
    try:
        with pd.ExcelWriter(nome_arquivo, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
            if nome_aba in writer.sheets:  # Verifica se a aba já existe
                start_row = writer.sheets[nome_aba].max_row
            else:
                start_row = 0
            
            resultados.to_excel(writer, sheet_name=nome_aba, index=False, header=(start_row == 0), startrow=start_row)

    except Exception as e:
        print(f"Erro ao salvar os dados no Excel: {str(e)}")

# Itera sobre os CNPJs na planilha, ignorando valores nulos
for cnpj in planilha_cnpjs['CNPJ'].dropna():
    print(f"Lendo CNPJ: {cnpj}")  # Exibe o CNPJ que está sendo processado

    # Obtém os dados da empresa com base no CNPJ
    dados_empresa = obter_dados_empresa_por_cnpj(str(cnpj))
    if dados_empresa:
        dados_formatados = formatar_dados(dados_empresa)
        resultados.append(dados_formatados)

    time.sleep(10)  # Aguarda 2 segundos entre cada requisição

# Salva os dados caso tenha resultados
if resultados:
    resultados_df = pd.DataFrame(resultados)
    salvar_dados_empresa_excel(resultados_df, caminho_planilha)

print("Dados salvos com sucesso na planilha na aba Dados!")
