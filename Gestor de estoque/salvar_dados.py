from dados import *

def obterProdutosCsv():
    with open("banco_de_dados/produtos.csv", "r") as arquivo:
        
        linha = arquivo.readline()
        while linha: 
            dado = linha.strip()   #-> strip retorna -> 'ID_PRODUTO,NOME_PRODUTO,'PRECO_PRODUTO',QUNATIDADE_PRODUTO'
            dado = dado.split(',') #-> split retorna -> ['ID_PRODUTO', 'NOME_PRODUTO', 'PRECO_PRODUTO', 'QUNATIDADE_PRODUTO']
            dado[0] = int(dado[0])
            dado[2] = float(dado[2])
            dado[3] = int(dado[3]) #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
            dadosProduto['ID_PRODUTO'].append(dado[0]) 
            dadosProduto['NOME_PRODUTO'].append(dado[1])
            dadosProduto['PRECO_PRODUTO'].append(dado[2])
            dadosProduto['QUANTIDADE_PRODUTO'].append(dado[3]) #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
            linha = arquivo.readline()  
    arquivo.close()

def salvarProdutosCsv():
    with open('banco_de_dados/produtos.csv','w') as arquivo:
        for i in range(len(dadosProduto['ID_PRODUTO'])):
            arquivo.write(f'{dadosProduto['ID_PRODUTO'][i]},{dadosProduto['NOME_PRODUTO'][i]},{dadosProduto['PRECO_PRODUTO'][i]},{dadosProduto['QUANTIDADE_PRODUTO'][i]}\n')
    arquivo.close()
  
def obterClientesCsv():
    pass

def SalvarClienteCsv():
    pass