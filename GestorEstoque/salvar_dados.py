from dados import dadosProduto

def obterProdutosCsv():
    with open("GestorEstoque/banco_de_dados/produtos.csv", "r") as arquivo:
        
        linha = arquivo.readline()
        while linha: 
            dado = linha.strip()   #-> strip retorna -> 'ID_PRODUTO,NOME_PRODUTO,QUNATIDADE_PRODUTO'
            dado = dado.split(',') #-> split retorna -> ['ID_PRODUTO', 'NOME_PRODUTO', 'QUNATIDADE_PRODUTO']
            dadosProduto['ID_PRODUTO'].append(dado[0]) 
            dadosProduto['NOME_PRODUTO'].append(dado[1])
            dadosProduto['QUANTIDADE_PRODUTO'].append(dado[2])
            linha = arquivo.readline()  
    arquivo.close()

def salvarProdutosCsv():
    with open('banco_de_dados/produtos.csv','w') as arquivo:
        for i in range(len(dadosProduto['ID_PRODUTO'])):
            arquivo.write(f'{dadosProduto['ID_PRODUTO'][i]},{dadosProduto['NOME_PRODUTO'][i]},{dadosProduto['QUANTIDADE_PRODUTO'][i]}')
    arquivo.close()
  
def obterClientesCsv():
    pass

def SalvarClienteCsv():
    pass
obterProdutosCsv()