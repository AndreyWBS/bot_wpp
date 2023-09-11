import json
import multiprocessing
from main import inicio

processos = []
numeros_wpps = []

with open('informacoes_json/dados.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)
with open('informacoes_json/dados_teste.json', 'r', encoding='utf-8') as arquivo:
    dados2 = json.load(arquivo)

numeros_wpps.append(dados)
numeros_wpps.append(dados2)
def vamosla():
    if __name__ == '__main__':

        for infos in numeros_wpps:
            novo_inicio = inicio(infos)
            p = multiprocessing.Process(target= novo_inicio.comecar_ ,args=())
            processos.append(p)

        for p in processos:
            p.start()

        for p in processos:
            p.join()

vamosla()