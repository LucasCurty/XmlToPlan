import xmltodict
import os
import pandas as pd

def pegarInfosXml(arquivo, valores):
    with open(f'xmls/{arquivo}', "rb") as arquivo_xml:
        dic_arquivo = xmltodict.parse(arquivo_xml)
        inf_nota = dic_arquivo["nfeProc"]["NFe"]["infNFe"]
        destinatario_nome = inf_nota["dest"]["xNome"]
        destinatario_CNPJ = inf_nota["dest"]["CNPJ"]
        emitente_CNPJ = inf_nota["emit"]["CNPJ"]
        valor = float(inf_nota["pag"]["detPag"]["vPag"])
        
        if destinatario_nome in valores:
            valores[destinatario_nome][3] += valor
        else:
            valores[destinatario_nome] = [destinatario_nome, destinatario_CNPJ, emitente_CNPJ, valor]

listar_arquivos = os.listdir("xmls")

#colunas = ["Destinaratio nome", "destinaratio CNPJ", "emitente_CNPJ", "valores"]
valores = {}

for arquivo in listar_arquivos:
    pegarInfosXml(arquivo, valores)

resultado_final = list(valores.values())

print(resultado_final)

#criar uma pasta com o nome xmls e colocar as notas fiscais, descomentar os 2 codigos abaixo e a variavel colunas para gerar o arquivo de planilha
#tabelas = pd.DataFrame(columns=colunas, data=resultado_final)
#tabelas.to_excel("NotasFiscais.xlsx", index=False)
