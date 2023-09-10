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


class UsarSele:
    def __init__(self, caminho, ativo, dados="a"):
        self.ativo = ativo
        self.caminho = caminho
        self.dados = dados
        options = webdriver.ChromeOptions()
        caminho_nav = f"user-data-dir={self.caminho}\\{self.ativo}"
        options.add_argument(caminho_nav)
        self.driver = webdriver.Chrome(options=options)
        print("iniciado")

    def iniciando_drive(self):
        return self.driver

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
