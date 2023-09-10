import json
import time

import pandas as pd

from interacoes.trabalhando_selenium import UsarSele
from interacoes.trabalhando_wpp import Wpp

with open('informacoes_json/dados.json', 'r',encoding='utf-8') as arquivo:
    dados = json.load(arquivo)



def comecar(dados):
    numeroPrincipal = dados["numeroPrincipal"]
    caminhoPlanilha = dados["caminhoPlanilha"]
    mensagem = dados["mensagem"]
    caminho_drive = dados["caminho_drive"]
    ativo = dados["ativo"]

    driver_ = UsarSele(caminho_drive, ativo, dados)
    driver = driver_.iniciando_drive()

    driver.get('https://web.whatsapp.com/')
    #driver_.procurarElementocomSeletor("#app > div > div > div._2Ts6i._3RGKj > header > div._3WByx")
    novo_wpp = Wpp(driver_)
    numeros = pd.read_excel(caminhoPlanilha)

    for numero in numeros['numero']:
        novo_wpp.clicar_conversa(numeroPrincipal)
        novo_wpp.escrever_mensagem_txt(str(numero))
        novo_wpp.clicar_numero(str(numero))
        novo_wpp.clicar_conversar_com()
        novo_wpp.escrever_mensagem_txt2(mensagem)
        time.sleep(5)


comecar(dados)
