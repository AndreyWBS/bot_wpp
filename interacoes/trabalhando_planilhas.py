import openpyxl
import pandas as pd


class Planilhas:
    def __init__(self):
        return
    def gerar_Planilhas(self,dados,ativo,caminho):
        df_Planilha = pd.DataFrame(dados)
        nome_planilha = f"{ativo}numeros.xlsx"
        caminho_planilha = caminho
        df_Planilha.to_excel(caminho_planilha + nome_planilha, index=False)
        return

    def atualizando_planilhas(self,caminho, coluna, index, valor_atual):
        workbook = openpyxl.load_workbook(caminho)
        sheet = workbook.active
        sheet[coluna+index] = valor_atual
        workbook.save(caminho)
        workbook.close()
        return
