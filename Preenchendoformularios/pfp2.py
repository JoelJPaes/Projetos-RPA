from openpyxl import load_workbook
from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

nomeCaminhoArquivo = r"C:\Users\Joden\OneDrive\Área de Trabalho\CARREIRA PROGRAMAÇÃO\DadosFormulario.xlsx"
planilha_aberta = load_workbook(filename=nomeCaminhoArquivo)
sheet_selecionada = planilha_aberta['Dados']

for linha in range(2, len(sheet_selecionada['A']) + 1):
    nome = sheet_selecionada[f'A{linha}'].value
    email = sheet_selecionada[f'B{linha}'].value
    telefone = sheet_selecionada[f'C{linha}'].value
    sexo = sheet_selecionada[f'D{linha}'].value
    sobre = sheet_selecionada[f'E{linha}'].value
    navegadorFormulario = opcoesSelenium.Chrome()
    navegadorFormulario.get("https://pt.surveymonkey.com/r/WLXYDX2")
    espera = WebDriverWait(navegadorFormulario, 5)

    campo_nome = espera.until(EC.presence_of_element_located((By.NAME, "166517069")))
    campo_nome.send_keys(nome)
    campo_email = espera.until(EC.presence_of_element_located((By.NAME, "166517072")))
    campo_email.send_keys(email)
    campo_telefone = espera.until(EC.presence_of_element_located((By.NAME, "166517070")))
    campo_telefone.send_keys(telefone)
    campo_sobre = espera.until(EC.presence_of_element_located((By.NAME, "166517073")))
    campo_sobre.send_keys(sobre)

    if sexo == "Masculino":
        botao_masculino = espera.until(EC.element_to_be_clickable((By.ID, "1215509812")))
        botao_masculino.click()

    else:
        botao_feminino = espera.until(EC.element_to_be_clickable((By.ID, "1215509813")))
        botao_feminino.click()
    botao_enviar = espera.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="view-pageNavigation"]/div/button')))
print("Pronto!")