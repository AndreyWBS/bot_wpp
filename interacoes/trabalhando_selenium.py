import pickle
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import pandas as pd




class usarSele:
    def procurarElementocomSeletor(seletor, driver):
        wait = WebDriverWait(driver, 120)
        elemento = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, seletor)))
        return driver.find_element(By.CSS_SELECTOR, seletor)


    def procurarElementscomseletor(seletor, driver):
        wait = WebDriverWait(driver, 25)
        elemento = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, seletor)))
        return driver.find_elements(By.CSS_SELECTOR, seletor)


    def clicar_seletor_elemento(seletor, elementoP, driver):
        wait = WebDriverWait(driver, 25)
        elemento = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, seletor)))
        elementoP.find_element(By.CSS_SELECTOR, seletor).click()


    def escrever(seletor, txt, driver):
        wait = WebDriverWait(driver, 25)
        elemento = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, seletor)))
        for letra in txt:
            if letra == "#":
                driver.find_element(By.CSS_SELECTOR, seletor).send_keys(Keys.CONTROL, Keys.ENTER)
            else:
                driver.find_element(By.CSS_SELECTOR, seletor).send_keys(letra)
        driver.find_element(By.CSS_SELECTOR, seletor).send_keys(Keys.ENTER)


class guardar_drive:
    def iniciando_drive(self, caminho):
        try:
            with open(f'{caminho}driver.pkl', 'rb') as driver_file:
                driver = pickle.load(driver_file)
        except FileNotFoundError:
            driver = webdriver.Chrome()

        return driver


    def fechando_drive(self, driver, caminho):
        with open(f'{caminho}driver.pkl', 'wb') as driver_file:
            pickle.dump(driver, driver_file)

