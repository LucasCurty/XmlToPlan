import pandas as pd
#Lendo a tabela inteira
my_table = pd.read_excel("teste.xlsx", sheet_name="exemplo")
#Criando uma tabela com dados selecionados
new_table = my_table[['Número da nota fiscal','Nome Emissor', 'Rua', 'Numero', 'Cidade Emissor', 'Peso bruto Item', 'Valor total da Ordem de Venda']]

#função para somar os valore se referindo a alguns argumentos
def somandoPor():
    soma_valores = new_table.groupby(['Número da nota fiscal','Nome Emissor', 'Rua', 'Numero', 'Cidade Emissor',])
    return soma_valores.sum()

#chamando a função
print(somandoPor())
