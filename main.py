import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from interacoes.trabalhando_selenium import Guardar_drive
from interacoes.trabalhando_selenium import UsarSele
import json

with open('informacoes_json/dados.json', 'r') as arquivo:
    dados = json.load(arquivo)


def comecar(caminho, ativo, dados):
    guarda_drive = Guardar_drive(caminho, ativo)
    driver = guarda_drive.iniciando_drive()
    sele = UsarSele(driver)
    driver.get('https://web.whatsapp.com/')
    sele.procurarElementocomSeletor("#app > div > div > div._2Ts6i._3RGKj > header > div._3WByx")
    guarda_drive.fechando_drive(driver)
    time.sleep(25)


caminho = dados['caminh_drive']
ativo = dados['ativo']

comecar(caminho, ativo, dados)
