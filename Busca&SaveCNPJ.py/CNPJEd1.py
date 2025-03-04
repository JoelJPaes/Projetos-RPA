
import http.client  # Importa a biblioteca para requisições HTTP
import json  # Importa a biblioteca para manipulação de JSON
import pandas as pd  # Importa a biblioteca para manipulação de planilhas

def limpar_cnpj(cnpj):
    return ''.join(filter(str.isdigit, str(cnpj)))  # Remove caracteres não numéricos do CNPJ

def obter_dados_empresa_por_cnpj(cnpj):
    cnpj = limpar_cnpj(cnpj)
    
    conexao = http.client.HTTPSConnection("www.receitaws.com.br")
    conexao.request("GET", f"/v1/cnpj/{cnpj}")
    resposta = conexao.getresponse()  # Keep only this line
    print(f"Processando CNPJ {cnpj}: Status {resposta.status}")
    
    if resposta.status != 200:
        conexao.close()
        return None
        
    dados = resposta.read()
    conexao.close()
    empresa = json.loads(dados.decode('utf-8'))
    
    if "status" in empresa and empresa["status"] == "ERROR":
        print(f"Erro ao obter dados para o CNPJ {cnpj}: {empresa.get('message')}")
    return empresa

def formatar_dados(empresa):
    campos_interesse = ['cnpj', 'nome', 'telefone', 'email', 'logradouro', 'bairro', 'municipio', 'uf', 'cep', 'atividade_principal']

    dados_formatados = {campo: empresa.get(campo, '') for campo in campos_interesse}

    if 'atividade_principal' in empresa and empresa['atividade_principal']:
        dados_formatados['atividade_principal'] = empresa['atividade_principal'][0].get('text', '')

    return dados_formatados 

def salvar_dados_empresa_excel(resultados, nome_arquivo, nome_aba='Dados'):
    with pd.ExcelWriter(nome_arquivo, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
        try:
            worksheeet = writer.book[nome_aba]
            start_row = worksheeet.max_row
            resultados.to_excel(writer,sheet_name=nome_aba, index=False, herder = True)
            
        except KeyError:
            resultados.to_excel(writer, sheet_name=nome_aba, index=False, herder=False, startrow=start_row)
        df = pd.DataFrame(resultados)
        df.to_excel(writer, sheet_name=nome_aba, index=False)

# Define o caminho do arquivo Excel contendo os CNPJs
caminho_planilha = r"C:\Users\Joden\OneDrive\Área de Trabalho\CARREIRA PROGRAMAÇÃO\CNPJ.xlsx"

# Lê a planilha especificando a aba e garantindo que a coluna 'CNPJ' seja string
planilha_cnpjs = pd.read_excel(caminho_planilha, sheet_name="CNPJ", dtype={'CNPJ': str})

resultados = []  # Lista para armazenar os resultados das consultas

# Itera sobre os CNPJs na planilha, ignorando valores nulos
for cnpj in planilha_cnpjs['CNPJ'].dropna():
    print(f"Lendo CNPJ: {cnpj}")  # Exibe o CNPJ que está sendo processado

    # Obtém os dados da empresa com base no CNPJ
    dados_empresa = obter_dados_empresa_por_cnpj(str(cnpj))
    if dados_empresa:
        dados_formatados = formatar_dados(dados_empresa)
        resultados.append(dados_formatados)

if resultados:
    resultados_df = pd.DataFrame(resultados)

    salvar_dados_empresa_excel(resultados_df, caminho_planilha)

print("Dados salvos com sucesso na planilha na aba Dados!")


