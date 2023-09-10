import json
import time

from interacoes.trabalhando_selenium import UsarSele
from interacoes.trabalhando_wpp import Wpp

with open('informacoes_json/dados.json', 'r') as arquivo:
    dados = json.load(arquivo)
with open('informacoes_json/dados_wpp.json', 'r') as arquivo:
    wpp_info = json.load(arquivo)


def comecar( dados ,wpp_info):
    caminho = dados['caminho_drive']
    ativo = dados['ativo']
    numeroPrincipal = dados['numeroPrincipal']

    driver_ = UsarSele(caminho, ativo, dados)
    driver = driver_.iniciando_drive()

    driver.get('https://web.whatsapp.com/')
    driver_.procurarElementocomSeletor("#app > div > div > div._2Ts6i._3RGKj > header > div._3WByx")

    nome_conversas = wpp_info['nome_conversas']
    novo_wpp = Wpp(driver_)
    nome = novo_wpp.clicar_conversa(numeroPrincipal, nome_conversas)
    print(nome)
    time.sleep(5)




comecar( dados ,wpp_info)
