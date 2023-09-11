import time
import datetime
import pandas as pd
from interacoes.trabalhando_selenium import UsarSele
from interacoes.trabalhando_wpp import Wpp
from interacoes.trabalhando_planilhas import Planilhas


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
    # print(planilha_df.columns)
    return planilha_df.columns


def salvar_palinlha(planilha_df, ativo):
    caminho = "planilhas\\"
    nova_planilha = {}
    for coluna in verificar_colunas(planilha_df):
        nova_planilha[str(coluna)] = []
    nova_planilha_df = Planilhas()
    # print(nova_planilha)
    novo_caminho = nova_planilha_df.gerar_planilhas(nova_planilha, ativo, caminho)
    return novo_caminho


def atualizar_planilha(caminho, index, planilha_df):
    trabalhando_planilhas = Planilhas()
    for i, coluna in enumerate(verificar_colunas(planilha_df)):
        valor_atual = str(planilha_df.loc[index, coluna])
        coluna_letra = chr(65 + i)

        trabalhando_planilhas.atualizando_planilhas(caminho, coluna_letra, (index + 2), valor_atual)


def mandar_mensagem_por_numero(novo_wpp, numeros, dados):
    global mensagem2
    numero_principal = dados["numeroPrincipal"]
    mensagem = dados["mensagem"]

    ativo = dados["ativo"]

    novo_caminho = salvar_palinlha(numeros, ativo)

    for i, numero in enumerate(numeros['numero']):
        for coluna in verificar_colunas(numeros):
            coluna_str = "["+str(coluna)+"]"
            trocar = numeros.loc[i, coluna]
            mensagem2 =str(mensagem).replace(f"{coluna_str}", str(trocar))

        novo_wpp.clicar_conversa(numero_principal)
        novo_wpp.escrever_mensagem_txt(str(numero))

        if not novo_wpp.clicar_numero(str(numero)):
            continue
        if novo_wpp.clicar_conversar_com():
            continue

        bom = pegar_bom()
        novo_wpp.escrever_mensagem_txt2(bom)
        novo_wpp.escrever_mensagem_txt2(mensagem2)

        atualizar_planilha(novo_caminho, i, numeros)

        time.sleep(5)
    pass


class inicio:
    def __init__(self, dados_json):
        self.dados_json = dados_json

    def comecar_(self):
        caminho_planilha = self.dados_json["caminhoPlanilha"]

        caminho_drive = self.dados_json["caminho_drive"]
        ativo = self.dados_json["ativo"]

        driver_ = UsarSele(caminho_drive, ativo, self.dados_json)
        driver = driver_.iniciando_drive()

        driver.get('https://web.whatsapp.com/')
        novo_wpp = Wpp(driver_)
        numeros = pd.read_excel(caminho_planilha)

        mandar_mensagem_por_numero(novo_wpp, numeros, self.dados_json)
