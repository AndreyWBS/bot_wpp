import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd
import json

with open('../informacoes_json/dados_wpp.json', 'r') as arquivo:
    dados = json.load(arquivo)

print(dados)

