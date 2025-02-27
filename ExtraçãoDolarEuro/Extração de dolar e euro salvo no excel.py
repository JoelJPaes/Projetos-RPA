from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys  
import pyautogui as tempoPausaComputador  
from selenium.webdriver.common.by import By  
caminho_driver = r"C:\Users\Joden\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(caminho_driver)
meuNavegador = webdriver.Chrome(service=service)
meuNavegador.get("https://wise.com/br/currency-converter/dolar-hoje")
tempoPausaComputador.sleep(5)
valorDolar = meuNavegador.find_element(By.XPATH, '//*[@id="target-input"]').get_attribute("value")
print(f"Valor do dólar hoje pelo wise: {valorDolar}")
tempoPausaComputador.sleep(5)
meuNavegador.get("https://wise.com/br/currency-converter/eur-to-brl-rate?amount=1")
tempoPausaComputador.sleep(5)
valorEuro = meuNavegador.find_element(By.XPATH, '//*[@id="target-input"]').get_attribute("value")
print(f"Valor do Euro hoje pelo wise: {valorEuro}")
tempoPausaComputador.sleep(5)


import xlsxwriter
import os
nomeCaminhoArquivo = r"C:\Users\Joden\OneDrive\Área de Trabalho\CARREIRA PROGRAMAÇÃO\CursoPythonRPA\ExtraindoValorDolarEuroExcel\Dolar e Euro Wise.xlsx"
planilhaCriada = xlsxwriter.Workbook(nomeCaminhoArquivo)
sheet1 = planilhaCriada.add_worksheet()
sheet1.write("A1", "Dolar")
sheet1.write("A2", valorDolar)
sheet1.write("B1", "Euro")
sheet1.write("B2", valorEuro)
planilhaCriada.close()
os.startfile(nomeCaminhoArquivo)

input("Pressione Enter para sair...")