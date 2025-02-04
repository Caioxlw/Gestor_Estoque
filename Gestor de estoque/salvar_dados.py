from dados import *


def obterCsv(opcao):

    # # global dadosProduto
    # dadosProduto = {
    #     'ID_PRODUTO':[],
    #     'NOME_PRODUTO':[],
    #     'PRECO_PRODUTO':[],
    #     'QUANTIDADE_PRODUTO':[],
    #     'FORNECEDOR_PRODUTO':[],
    #     'CATEGORIA_PRODUTO':[]
    # } 
    
    # # global dadosCliente
    # dadosCliente = {
    #     'ID_CLIENTE':[],
    #     'NOME_CLIENTE':[]
    # } 

    # # global dadosFornecedor
    # dadosFornecedor = {
    #     'ID_FORNECEDOR':[],
    #     'NOME_FORNECEDOR':[]
    # }

    # # global dadosCategoria
    # dadosCategoria = {
    #     'ID_CATEGORIA':[],
    #     'NOME_CATEGORIA':[]
    # }

    # # global dadosVendas
    # dadosVendas = {
    #     'ID_VENDAS':[],
    #     'NOME_VENDA':[],
    #     'VALOR_VENDA':[]
    # }


    if opcao == 'Produtos':
        with open("banco_de_dados/produtos.csv", "r") as arquivo:
            
            linha = arquivo.readline()
            while linha: 
                dado = linha.strip()   
                dado = dado.split(',') 
                dado[0] = int(dado[0])
                dado[2] = float(dado[2])
                dado[3] = int(dado[3]) 
                dadosProduto['ID_PRODUTO'].append(dado[0]) 
                dadosProduto['NOME_PRODUTO'].append(dado[1])
                dadosProduto['PRECO_PRODUTO'].append(dado[2])
                dadosProduto['QUANTIDADE_PRODUTO'].append(dado[3])
                dadosProduto['FORNECEDOR_PRODUTO'].append(dado[4])
                dadosProduto['CATEGORIA_PRODUTO'].append(dado[5])

                linha = arquivo.readline()  
        arquivo.close()
    
    elif opcao == 'Clientes':
        with open("banco_de_dados/clientes.csv", "r") as arquivo:
            
            linha = arquivo.readline()
            while linha: 
                dado = linha.strip()   
                dado = dado.split(',') 
                dado[0] = int(dado[0])
                dadosCliente['ID_CLIENTE'].append(dado[0]) 
                dadosCliente['NOME_CLIENTE'].append(dado[1])
                linha = arquivo.readline()  
        arquivo.close()

    elif opcao == 'Fornecedores':
        with open('banco_de_dados/fornecedores.csv','r') as arquivo:
            
            linha = arquivo.readline()
            while linha:
                dado = linha.strip()   
                dado = dado.split(',') 
                dado[0] = int(dado[0])

                dadosFornecedor['ID_FORNECEDOR'].append(dado[0]) 
                dadosFornecedor['NOME_FORNECEDOR'].append(dado[1])
                linha = arquivo.readline()  
        arquivo.close()

    elif opcao == 'Categorias':
        
        with open('banco_de_dados/categorias.csv','r') as arquivo:
            
            linha = arquivo.readline()
            while linha:
                dado = linha.strip()   
                dado = dado.split(',') 
                
                dado[0] = int(dado[0])

                dadosCategoria['ID_CATEGORIA'].append(dado[0])
                dadosCategoria['NOME_CATEGORIA'].append(dado[1])
                linha = arquivo.readline()  
        arquivo.close()        

    
def salvarCsv(opcao:str):
    if opcao == 'Produto':
        with open('banco_de_dados/produtos.csv','w') as arquivo:
            for i in range(len(dadosProduto['ID_PRODUTO'])):
                arquivo.write(f'{dadosProduto["ID_PRODUTO"][i]},{dadosProduto["NOME_PRODUTO"][i]},'
                              f'{dadosProduto["PRECO_PRODUTO"][i]},{dadosProduto["QUANTIDADE_PRODUTO"][i]},'
                              f'{dadosProduto["FORNECEDOR_PRODUTO"][i]},{dadosProduto["CATEGORIA_PRODUTO"][i]}\n')
        arquivo.close()
        
    elif opcao == 'Cliente':
        with open('banco_de_dados/clientes.csv','w') as arquivo:
            for i in range(len(dadosCliente['ID_CLIENTE'])):
                arquivo.write(f'{dadosCliente["ID_CLIENTE"][i]},'
                              f'{dadosCliente["NOME_CLIENTE"][i]}\n')
        arquivo.close()
        
    elif opcao == 'Fornecedor':
        with open('banco_de_dados/fornecedores.csv','w') as arquivo:
            for i in range(len(dadosFornecedor['ID_FORNECEDOR'])):
                arquivo.write(f'{dadosFornecedor["ID_FORNECEDOR"][i]},'
                              f'{dadosFornecedor["NOME_FORNECEDOR"][i]}\n')
        arquivo.close()

    elif opcao == 'Categoria':
        with open('banco_de_dados/categorias.csv','w') as arquivo:
            for i in range(len(dadosCategoria['ID_CATEGORIA'])):
                arquivo.write(f'{dadosCategoria['ID_CATEGORIA'][i]},'
                              f'{dadosCategoria['NOME_CATEGORIA'][i]}\n')
        arquivo.close()        
