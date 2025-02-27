Automacao de Extracao de Cotacao do Dolar e Euro

Descricao do Projeto

Este projeto automatiza a extração das cotações do dólar e euro do site Wise e salva os valores em uma planilha do Excel. Utiliza Selenium para navegação e captura de dados, PyAutoGUI para pausas, e XlsxWriter para manipulação de arquivos Excel. Esse tipo de automação é útil para profissionais e empresas que necessitam monitorar a cotação de moedas regularmente sem precisar acessar manualmente os sites de referência.

Tecnologias Utilizadas

Python

Selenium

PyAutoGUI

XlsxWriter

Como Funciona

O script abre o navegador e acessa a página de cotação do dólar no Wise.

Captura o valor da cotação e armazena em uma variável.

Em seguida, acessa a página de cotação do euro e captura seu valor.

Os valores extraídos são salvos em uma planilha do Excel.

O arquivo Excel é aberto automaticamente ao final do processo.

Requisitos

Python 3+ instalado.

Google Chrome instalado.

ChromeDriver compatível com a versão do Chrome.

Bibliotecas Python: selenium, pyautogui, xlsxwriter.

Como Executar

Instale as bibliotecas necessárias com:

pip install selenium pyautogui xlsxwriter

Baixe o ChromeDriver correspondente à sua versão do Google Chrome e forneça o caminho correto no script.

Execute o script Python:

python nome_do_arquivo.py

Exemplo de Uso

A saída do script gerará uma planilha com as seguintes informações:

|  Dolar  |  Euro  |
|---------|--------|
|  5.30   |  6.20  |

(Esses valores são apenas ilustrativos, o script sempre buscará a cotação atualizada.)

Aplicabilidade na Automação de Processos (RPA)

Redução de trabalho manual ao buscar cotações diariamente.

Geração automática de relatórios financeiros.

Integração com sistemas de análise e tomada de decisão.

Este projeto demonstra uma abordagem simples, mas eficaz, de automação que pode ser expandida para outras necessidades empresariais.
