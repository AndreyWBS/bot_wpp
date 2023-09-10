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

dadosWPP = r"C:\Users\gabri\PycharmProjects\salvandoWPP_navegador\informacoes_json\dados_wpp.json"
with open(dadosWPP, 'r',encoding='utf-8') as arquivo:
    wpp_info = json.load(arquivo)


def obterPrimeiraLinha(texto):
    linhas = texto.split("\n")
    return linhas[0]


class Wpp:
    def __init__(self, Usersele):

        self.Usersele = Usersele
        self.nome_conversas = wpp_info["nome_conversas"]
        self.escrever_mensagem = wpp_info["escrever_mensagem"]
        self.todas_menagens = wpp_info["todas_menagens"]
        self.mensagem_link = wpp_info["mensagem_link"]
        self.conversar_com = wpp_info["conversar_com"]
        self.outra_caixa_txt = wpp_info["outra_caixa_txt"]

    def puxar_nome_conversas(self):
        conversa = self.Usersele.procurarElementscomseletor(self.nome_conversas)
        array_nome_conversas = []
        for linha in conversa:
            linhatxt = obterPrimeiraLinha(linha.text)
            array_nome_conversas.append(linhatxt)

        return array_nome_conversas

    def clicar_conversa(self, nome):
        conversa = self.Usersele.procurarElementscomseletor(self.nome_conversas)
        array_nome_conversas = []
        for linha in conversa:
            linhatxt = obterPrimeiraLinha(linha.text)
            if linhatxt == nome:
                linha.click()
        # print("click na conversa com o nome " + nome)

    def escrever_mensagem_txt(self, txt):
        self.Usersele.escrever(self.escrever_mensagem, txt)
        return
    def escrever_mensagem_txt2(self, txt):
        time.sleep(2)
        self.Usersele.escrever(self.outra_caixa_txt, txt)
        return
    def pegar_mensagens(self):
        mensagens = self.Usersele.procurarElementscomseletor(self.todas_menagens)
    def clicar_numero(self, numero):
        mensagens = self.Usersele.procurarElementscomseletor(self.todas_menagens)
        for linha in mensagens:
            linhatxt = obterPrimeiraLinha(linha.text)
            if linhatxt == numero:
                self.Usersele.clicar_seletor_elemento( self.mensagem_link, linha)
                break
    def clicar_conversar_com(self):
        conversar_com = self.Usersele.procurarElementocomSeletor(self.conversar_com)
        if conversar_com.get_attribute("aria-label") == "Conversar com ":
            conversar_com.click()
