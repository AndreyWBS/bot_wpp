import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from interacoes.trabalhando_selenium import UsarSele
from interacoes.trabalhando_wpp import UsarSele
import json

with open('informacoes_json/dados.json', 'r') as arquivo:
    dados = json.load(arquivo)


def comecar(caminho, ativo, dados):
    driver_ = UsarSele(caminho, ativo, dados)
    driver = driver_.iniciando_drive()
    driver.get('https://web.whatsapp.com/')
    #driver.get('chrome://version/')
    driver_.procurarElementocomSeletor("#app > div > div > div._2Ts6i._3RGKj > header > div._3WByx")


    time.sleep(5)


caminho = dados['caminho_drive']
ativo = dados['ativo']

comecar(caminho, ativo, dados)
