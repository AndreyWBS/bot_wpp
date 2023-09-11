import openpyxl
import pandas as pd


class Planilhas:
    def __init__(self):
        return

    def gerar_planilhas(self, dados_planilha, ativo, caminho):
        df_planilha = pd.DataFrame(dados_planilha)
        nome_planilha = f"{ativo}numeros.xlsx"
        caminho_planilha = caminho
        df_planilha.to_excel(caminho_planilha + nome_planilha, index=False)
        return caminho_planilha + nome_planilha

    def atualizando_planilhas(self, caminho, coluna, index, valor_atual):
        workbook = openpyxl.load_workbook(caminho)
        sheet = workbook.active
        #print(str(coluna) + str(index))
        sheet[str(coluna) + str(index)] = valor_atual
        workbook.save(caminho)
        workbook.close()
        return
