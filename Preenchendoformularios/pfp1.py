from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui as tempoEspera

navegadorFormulario = opcoesSelenium.Chrome()
navegadorFormulario.get("https://pt.surveymonkey.com/r/WLXYDX2")
tempoEspera.sleep(6)
nome = navegadorFormulario.find_element(By.NAME, "166517069")
tempoEspera.sleep(1)
nome.send_keys("Eduardo Borges Alves")
tempoEspera.sleep(10)
email = navegadorFormulario.find_element(By.NAME, "166517072")
tempoEspera.sleep(1)
email.send_keys("edu.b_alves@gmail.com")
tempoEspera.sleep(1)
telefone = navegadorFormulario.find_element(By.NAME, "166517070")
tempoEspera.sleep(1)
telefone.send_keys("(99) 6666 - 5555")
tempoEspera.sleep(1)
sobre = navegadorFormulario.find_element(By.NAME, "166517073")
tempoEspera.sleep(1)
sobre.send_keys("Sei automatizar processos e planilhas com Python")
tempoEspera.sleep(1)
radio_button = navegadorFormulario.find_element(By.ID, "1215509813")
tempoEspera.sleep(1)
radio_button.click()
tempoEspera.sleep(2)
enviar = navegadorFormulario.find_element(By.XPATH, '//*[@id="view-pageNavigation"]/div/button')
