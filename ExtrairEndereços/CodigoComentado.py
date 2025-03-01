import http.client  # Vamos usar uma biblioteca para fazer requisições HTTP!
import json  # Vamos precisar de uma ferramenta para lidar com dados em formato JSON.
import pandas as pd  # Pandas vai ser nossa ferramenta para salvar os dados em Excel!

# Função para buscar o endereço com base no CEP
def obter_endereco_por_cep(cep):
    # Criamos a conexão com o site "viacep.com.br", que nos ajuda a buscar o endereço.
    conexao = http.client.HTTPSConnection('viacep.com.br')  
    # Enviamos uma requisição do tipo GET, pedindo o endereço no formato JSON para o CEP informado.
    conexao.request('GET', f"/ws/{cep}/json/")  
    # Esperamos a resposta do servidor.
    resposta = conexao.getresponse()  
    # Lemos os dados da resposta.
    dados = resposta.read()  
    # Decodificamos os dados e transformamos o JSON em um formato Python (um dicionário).
    endereco = json.loads(dados.decode('utf-8'))  

    # Fechamos a conexão. Estamos terminando nossa comunicação com o servidor.
    conexao.close()  
    # Retornamos o endereço que encontramos, se tudo correu bem!
    return endereco  

# Função para salvar os dados do endereço em um arquivo Excel
def salvar_endereco_excel(endereco, nome_arquivo="enderecos.xlsx"):
    # Se não houver erro no endereço, vamos prosseguir.
    if "erro" not in endereco:  
        # Criamos um DataFrame (uma tabela) com o endereço que recebemos.
        df = pd.DataFrame([endereco])  
        # Salvamos esse DataFrame em um arquivo Excel com o nome fornecido (ou o padrão).
        df.to_excel(nome_arquivo, index=False)  
        # E mostramos uma mensagem para o usuário avisando que deu tudo certo!
        print(f"Endereço salvo em {nome_arquivo}")  
    else:
        # Caso o CEP tenha dado erro, mostramos uma mensagem de erro.
        print("CEP não encontrado.")  

# Vamos testar com o CEP '01001000' (um CEP de São Paulo)
cep_exemplo = "01001000"
# Chamamos a função para buscar o endereço.
endereco_resultado = obter_endereco_por_cep(cep_exemplo)  
