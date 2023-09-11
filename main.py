import json
import time
import datetime

import pandas as pd

from interacoes.trabalhando_selenium import UsarSele
from interacoes.trabalhando_wpp import Wpp
from interacoes.trabalhando_planilhas import Planilhas

with open('informacoes_json/dados.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)


def pegar_bom():
    hora_atual = datetime.datetime.now().time()
    hora = hora_atual.strftime("%H")

    if int(hora) < 12:
        bom = "Bom dia"
    elif 12 <= int(hora) < 18:
        bom = "Boa tarde"
    else:
        bom = "Boa noite"
    return bom


def verificar_colunas(planilha_df):
    print(planilha_df.columns)
    return planilha_df.columns


def salvar_palinlha(planilha_df, ativo):
    caminho = "planilhas\\"
    nova_planilha = {}
    for coluna in verificar_colunas(planilha_df):
        nova_planilha[str(coluna)] = []
    nova_planilha_df = Planilhas()
    print(nova_planilha)
    novo_caminho = nova_planilha_df.gerar_Planilhas(nova_planilha, ativo, caminho)
    return novo_caminho


def atualizar_planilha(caminho, index, planilha_df):
    trabalhando_planilhas = Planilhas()
    for i, coluna in enumerate(verificar_colunas(planilha_df)):
        valor_atual = str(planilha_df.loc[index, coluna])
        coluna_letra = chr(65 + i )

        trabalhando_planilhas.atualizando_planilhas(caminho, coluna_letra, (index+2), valor_atual)


def mandar_mensagem_por_numero(novo_wpp, numeros):
    numero_principal = dados["numeroPrincipal"]
    mensagem = dados["mensagem"]
    ativo = dados["ativo"]

    novo_caminho = salvar_palinlha(numeros, ativo)

    for i, numero in enumerate(numeros['numero']):
        novo_wpp.clicar_conversa(numero_principal)
        novo_wpp.escrever_mensagem_txt(str(numero))
        novo_wpp.clicar_numero(str(numero))
        novo_wpp.clicar_conversar_com()

        bom = pegar_bom()
        novo_wpp.escrever_mensagem_txt2(bom)
        novo_wpp.escrever_mensagem_txt2(mensagem)
        # TODO: colocar pra verificarse tem nome ou algo a mais na planilha pode ser no proio ttrabalhano com planilhas
        atualizar_planilha(novo_caminho, i, numeros)

        time.sleep(5)
    pass


def comecar(dados_json):
    caminho_planilha = dados_json["caminhoPlanilha"]

    caminho_drive = dados_json["caminho_drive"]
    ativo = dados_json["ativo"]

    driver_ = UsarSele(caminho_drive, ativo, dados_json)
    driver = driver_.iniciando_drive()

    driver.get('https://web.whatsapp.com/')
    novo_wpp = Wpp(driver_)
    numeros = pd.read_excel(caminho_planilha)

    # TODO: gerar uma função a partir  daqui
    mandar_mensagem_por_numero(novo_wpp, numeros)


comecar(dados)
