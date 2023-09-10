import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd
from interacoes.trabalhando_selenium import UsarSele
import json

def obterPrimeiraLinha(texto):
    linhas = texto.split("\n")
    return linhas[0]

with open('../informacoes_json/dados_wpp.json', 'r') as arquivo:
    dados_Wpp = json.load(arquivo)

class Wpp:
    def __init__(self,drive, Usersele):
        self.drive = drive
        self.Usersele = Usersele

    def puxar_conversas(self, seletor):
        conversa = self.Usersele.procurarElementscomseletor(seletor)
        array_nome_conversas =[]
        for linha in conversa:
            linhatxt = obterPrimeiraLinha(linha.text)
            array_nome_conversas.append(linhatxt)

        return array_nome_conversas


