import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import json

import pandas as pd


def salvando_drive():
    seletor = "#profile_path"
    driver = webdriver.Chrome()
    driver.get('chrome://version/')
    wait = WebDriverWait(driver, 120)
    elemento = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, seletor)))
    caminho = driver.find_element(By.CSS_SELECTOR, seletor)
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo_json = os.path.join(diretorio_atual, '../informacoes_json/dados.json')

    # Abra o arquivo JSON para leitura
    with open(caminho_arquivo_json, 'r') as arquivo_json:
        dados = json.load(arquivo_json)


    # Passo 2: Modifique o Elemento
    dados['novo_caminho'] = str(caminho.text).replace("\Default", "")

    with open(caminho_arquivo_json, 'w') as arquivo_json:
        json.dump(dados, arquivo_json, indent=4)
    print("pegar o caminho do driver")
    return driver


class UsarSele:
    def __init__(self, driver):
        self.driver = driver

    def procurarElementocomSeletor(self, seletor):
        wait = WebDriverWait(self.driver, 120)
        elemento = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, seletor)))
        return self.driver.find_element(By.CSS_SELECTOR, seletor)

    def procurarElementscomseletor(self, seletor):
        wait = WebDriverWait(self.driver, 25)
        elemento = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, seletor)))
        return self.driver.find_elements(By.CSS_SELECTOR, seletor)

    def clicar_seletor_elemento(self, seletor, elementoP):
        wait = WebDriverWait(self.driver, 25)
        elemento = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, seletor)))
        elementoP.find_element(By.CSS_SELECTOR, seletor).click()

    def escrever(self, seletor, txt):
        wait = WebDriverWait(self.driver, 25)
        elemento = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, seletor)))
        for letra in txt:
            if letra == "#":
                self.driver.find_element(By.CSS_SELECTOR, seletor).send_keys(Keys.CONTROL, Keys.ENTER)
            else:
                self.driver.find_element(By.CSS_SELECTOR, seletor).send_keys(letra)
        self.driver.find_element(By.CSS_SELECTOR, seletor).send_keys(Keys.ENTER)


class Guardar_drive():
    def __init__(self, caminho, ativo, dados="a"):
        self.ativo = ativo
        self.caminho = caminho
        self.dados = dados
        print("deu bom")

    def iniciando_drive(self):
        # TODO: escrver em json o dirr user-data-dir={valor}
        perfil = "\Profile 2"


        options = webdriver.ChromeOptions()
        # options.add_argument("--headless=new")
        caminho_nav = f"user-data-dir={self.caminho}\\{self.ativo}"
        options.add_argument(caminho_nav)
        driver = webdriver.Chrome(options=options)
        return driver
