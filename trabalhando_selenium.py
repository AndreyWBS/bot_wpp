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


def gerarPLanilahas(nomeWPP, planilha_de_numeros_Erro,planilha_de_numeros_env):
    df_Planilha_com_ERRO = pd.DataFrame(planilha_de_numeros_Erro)
    df_Planilha_com_ENV = pd.DataFrame(planilha_de_numeros_env)
    nome_env = f"{nomeWPP}numeros_env.xlsx"
    nome_erro = f"{nomeWPP}numeros_erros.xlsx"
    caminho_planilha = r"C:\Users\Micro\Desktop\planilhasGeradasBOT\acionamentosWPP\pla"

    df_Planilha_com_ERRO.to_excel(caminho_planilha + nome_erro, index=False)
    df_Planilha_com_ENV.to_excel(caminho_planilha + nome_env, index=False)


def obterPrimeiraLinha(texto):
    linhas = texto.split("\n")
    return linhas[0]
