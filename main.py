import xmltodict
import os
import pandas as pd

def pegarInfosXml(arquivo, valores):
    with open(f'xmls/{arquivo}', "rb") as arquivo_xml:
        dic_arquivo = xmltodict.parse(arquivo_xml)
        inf_nota = dic_arquivo["nfeProc"]["NFe"]["infNFe"]
        chave_nota = inf_nota["@Id"]
        emitente_CNPJ = inf_nota["emit"]["CNPJ"]
        emitente_nome = inf_nota["emit"]["xNome"]
        destinatario_CNPJ = inf_nota["dest"]["CNPJ"]
        destinatario_nome = inf_nota["dest"]["xNome"]
        valores.append([chave_nota, emitente_CNPJ,emitente_nome,destinatario_CNPJ,destinatario_nome])


listar_arquivos = os.listdir("xmls")

colunas = ["Chave_NFe", "CNPJ_Emissor","Nome_Emissor", "CNPJ_Destinatario", "Nome_Destinatario"]
valores = []


for arquivo in listar_arquivos:
    pegarInfosXml(arquivo, valores)

tabelas = pd.DataFrame(columns=colunas, data=valores)
tabelas.to_excel("NotasFiscais.xlsx", index=False)