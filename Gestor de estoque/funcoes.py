import os
from time import sleep
from dados import *
from salvar_dados import *

#------MENU PRINCIPAL-------
def menuPrincipal():
    obterCsv('Produtos')
    obterCsv('Clientes')
    obterCsv('Fornecedores')
    
    while True:
        os.system('cls')
        try: #try vai rodar o bloco dentro dele, caso der algum erro o except é chamado
            menu = int(input('''
    --MENU--
    1.PRODUTOS
    2.CLIENTES
    3.FORNECEDORES
    4.VENDAS
    
    0.SALVAR E SAIR
                             
R:'''))
            if menu > 4 or menu < 0:
                os.system('cls')
                print('OPÇÃO INVÁLIDA!!')
                sleep(0.5)
                continue
            match menu:
                case 1:
                    print('\nIndo para o menu de produtos...')
                    sleep(0.5)
                    return menuProdutos()
                case 2:
                    print('\nIndo para o menu de clientes...')
                    sleep(0.5)
                    menuClientes()
                case 3:
                    print('\nMenu de fornecedores ainda nao existe...')
                    sleep(0.5)
                    menuFornecedores() #pra fazer ainda
                case 4:
                    print('\nMenu de vendas ainda nao existe...')
                    sleep(0.5)
                    menuVendas() #pra fazer ainda

                case 0:
                    print('\nSalvando e saindo...')
                    sleep(0.5)
                    exit()
                case _:
                    print("\nOPÇÃO INVÁLIDA!")   
                    sleep(0.5)
                    continue 

        except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel
            os.system('cls')
            print('APENAS NÚMEROS!!')
            sleep(0.5)
            continue  
#------/MENU PRINCIPAL-------

#------MENU PRODUTOS------ 
def menuProdutos():

    while True:
        os.system('cls')

     
        try: #try vai rodar o bloco dentro dele, caso der algum erro o except é chamado
            menu = int(input('''
    ---MENU DE PRODUTOS---
    1.CADASTRAR
    2.RENOMEAR
    3.EXCLUIR
    4.ENTRADA
    5.MOSTRAR ESTOQUE
    
    0.VOLTAR

R:'''))
            if menu > 5 or menu < 0:
                os.system('cls')
                print('OPÇÃO INVÁLIDA!!')
                sleep(0.5)
                continue

            match menu:
                case 1:
                    return cadastrar()
                case 2:
                    return editarItem()
                case 3:
                    return excluirItem() 
                case 4:
                    return entradaItem()
                case 5:
                    print(mostrarEstoque())
                    input('\nPressione enter para sair')
                    return menuProdutos()
                case 0:
                    return menuPrincipal()
                case _:
                    print("OPÇÃO INVÁLIDA!")   
                    sleep(0.5)
                    return menuProdutos() 

        except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel
            os.system('cls')
            print('APENAS NÚMEROS!!')
            sleep(0.5)
                
def entradaItem():
    #for com {i}.{dadosProduto['NOME_PRODUTO'][i]
    os.system('cls')
    print('---ENTRADA DE ITEM---')

    if not dadosProduto['ID_PRODUTO']: #python trata vazios como falso
        os.system('cls')
        print('Estoque vazio!!')
        menuProdutos()

    mostrarEstoque()
    
    try: #try vai rodar o bloco dentro dele, caso der algum erro o except é chamado
        idProduto = int(input('\nQual item deseja dar entrada? [ID]: '))
    except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel
        print('Apenas numeros!!')
        
    if idProduto not in dadosProduto['ID_PRODUTO']:
        print('OPÇÃO INVÁLIDA!!')
        
    else:
        while True:
            try:
                quantidadeItem = int(input(f'Dar entrada em no item ID[{dadosProduto["QUANTIDADE_PRODUTO"][idProduto]}] de: '))
                if quantidadeItem < 0:
                    print("Apenas entradas de Estoque!")
                    continue
                break
            except ValueError:
                print('Apenas numeros!!')
        
            dadosProduto['QUANTIDADE_PRODUTO'][idProduto] += quantidadeItem

            salvarCsv('Produto')
            menuProdutos()

def cadastrar():
        os.system('cls')
        print('---CADASTRO DE ITEM---')

        while True:
            nomeProduto = str(input('\nNOME DO PRODUTO: ')).upper()
            if nomeProduto in dadosProduto['NOME_PRODUTO']:
                print(f'\nItem {nomeProduto} já existe!!')
                sleep(1)
            elif not nomeProduto:
                print('\nNome do produto nao pode estar em branco!!!')
                sleep(1)
            else:
                break
            
        while True:
            try: #try vai rodar o bloco dentro dele, caso der algum erro o except é chamado
                precoProduto = float(input('PRECO: '))
                break
            except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel
                print('\nApenas números!!')
                sleep(0.5)

        while True:
            
            try:
                fornecedor = int(input(f'{nomeProduto} é vinculado a qual fornecedor? [ID]\nEnter para cadastrar agora\n'))
                break
            except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel
                print('Apenas números!!')
                sleep(0.5)

        dadosProduto['ID_PRODUTO'].append(f'{len(dadosProduto["ID_PRODUTO"])}')           #--------------
        dadosProduto['NOME_PRODUTO'].append(nomeProduto)                   #fazer uma funcao para adicionar item ao estoque
        dadosProduto['PRECO_PRODUTO'].append(precoProduto)       #--------------
        dadosProduto['QUANTIDADE_PRODUTO'].append(0)
        dadosProduto['FORNECEDOR_PRODUTO'].append(dadosFornecedor['NOME_FORNECEDOR'][fornecedor])
        os.system('cls')
        salvarCsv()
        print('Item cadastrado!!')

        sleep(0.5)
        menuProdutos('Produto')
        
def editarItem():
    if not dadosProduto['ID_PRODUTO']: #python trata vazios como falso
        os.system('cls')
        print('Estoque vazio!!')
        
        menuProdutos()

    os.system('cls')
    mostrarEstoque()
    try: #try vai rodar o bloco dentro dele, caso der algum erro o except é chamado
        idProduto = int(input('Qual item deseja editar? [ID]: '))
    except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel
        print('Apenas numeros!!')
        
    if idProduto not in dadosProduto['ID_PRODUTO']:
        print('OPÇÃO INVÁLIDA!!')
        
    else:
        while True:
            nomeEditado = str(input(f'Renomear [{dadosProduto["NOME_PRODUTO"][idProduto]}] para: ').upper())

            if nomeEditado == dadosProduto['NOME_PRODUTO'][idProduto]:
                print('NOVO NOME NÃO PODE SER IGUAL AO ANTERIOR!!')
    
            elif nomeEditado in dadosProduto['NOME_PRODUTO']:
                print('ESSE NOME JA EXISTE!!')

            else:    
                dadosProduto['NOME_PRODUTO'][idProduto] = nomeEditado
                print('ITEM RENOMEADO!!')
    
    
                break
        salvarCsv('Produto')
        menuProdutos()

def excluirItem():
    while True:

        print(mostrarEstoque())
        
        try: #try vai rodar o bloco dentro dele, caso der algum erro o except é chamado
            excluir = int(input('\nQual item deseja exlcuir do seu estoque? [ID]: '))
            if excluir not in dadosProduto['ID_PRODUTO']:
                print('Esse item não existe')
                sleep(1)
                continue
            else:
                break
        except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel
            print('Apenas numeros!!')
            sleep(1)
        
    for i in range(len(dadosProduto['ID_PRODUTO'])):
        if excluir == dadosProduto['ID_PRODUTO'][i]:
            dadosProduto['ID_PRODUTO'].pop(i)
            dadosProduto['NOME_PRODUTO'].pop(i)
            dadosProduto['QUANTIDADE_PRODUTO'].pop(i)
            dadosProduto['PRECO_PRODUTO'].pop(i)
            # removeu = True
            print('Item removido com sucesso!')    
            sleep(1)
            break
    
    salvarCsv('Produto')
    return menuProdutos()

def mostrarEstoque() -> str: #defino o parametro igual a zero para ele ser opcional, por que se o usuario nao digitar nada ele esta pre setado com um valor
    os.system('cls')
    if not dadosProduto['ID_PRODUTO']:
        print('ESTOQUE VAZIO!!')
        sleep(1)
        menuProdutos()
        
    id = dadosProduto['ID_PRODUTO']
    nome = dadosProduto['NOME_PRODUTO']
    preco = dadosProduto['PRECO_PRODUTO']
    qtd = dadosProduto['QUANTIDADE_PRODUTO']
    forn = dadosProduto['FORNECEDOR_PRODUTO']
    
    estoque_string = ''
    maiorID = len(str(max( id )))
    maiorNOME = len(max( nome ,key=len))
    maiorPRECO = len(str(max( preco )))
    maiorQTD = len(str(max( qtd )))
    # maiorFORN = len(max(dadosProduto['FORNECEDOR_PRODUTO'],key=len))

    estoque_string += (f'ID{" "*(maiorID-2)} │ NOME{" "*(maiorNOME-4)} │ PRECO{" "*(maiorPRECO-5)} │ QUANTIDADE{" "*(maiorQTD-10)} │ FORNECEDOR\n')

    for i in range(len(dadosProduto['ID_PRODUTO'])):
        
        maiorID    = len(str(max( id )))      - len(str( id[i] ))
        maiorNOME  = len(max( nome ,key=len)) - len( nome[i] )
        maiorPRECO = len(str(max( preco )))   - len(str( preco[i] ))
        maiorQTD   = len(str(max( qtd )))     - len(str( qtd[i] ))
        
        estoque_string += (f'{id[i]}{" "*(maiorID)} │ {nome[i]}{" "*(maiorNOME)} │ {preco[i]}{" "*(maiorPRECO)} │ {qtd[i]}{" "*(10-len(str( qtd[i] )))} │ {forn[i]}\n')
    return estoque_string

    
#------/MENU PRODUTOS------ 

#------MENU FORNECEDORES------ 
def menuFornecedores():
    while True:
        os.system('cls')
        try: #try vai rodar o bloco dentro dele, caso der algum erro o except é chamado
            menu = int(input('''
    --MENU DE FORNECEDORES--
    1.CADASTRAR
    2.EDITAR
    3.LISTAR FORNECEDORES

    0.VOLTAR
                                
R:'''))
            if menu > 3 or menu < 0:
                os.system('cls')
                print('OPÇÃO INVÁLIDA!!')
                sleep(0.5)
                continue

            match menu:
                case 1:
                    return cadastrarFornecedor()
                case 2:
                    return editarFornecedor()
                case 3:
                    print(listarFornecedores())
                    sleep(0.5)
                    input('\nPressione enter para sair')
                    return menuFornecedores()
                case 0:
                    return menuPrincipal()
                case _:
                    print("OPÇÃO INVÁLIDA!") 
                    continue

        except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel
            os.system('cls')
            print('APENAS NÚMEROS!!')
            sleep(0.5)
            continue

def cadastrarFornecedor():
    os.system('cls')
    print('---CADASTRO DE FORNECEDOR---\n')   

    while True:
        nome = str(input('NOME: ')).upper()
        if nome in dadosFornecedor['NOME_FORNECEDOR']:
            print(f'Item {nome} já existe!!')
            sleep(0.5)
        break

    dadosFornecedor['ID_FORNECEDOR'].append(f'{len(dadosFornecedor["ID_FORNECEDOR"])+1}')     #------------
    dadosFornecedor['NOME_FORNECEDOR'].append(nome)                                      #fazer uma funcao para cadastrar cliente

    os.system('cls')
    salvarCsv('Fornecedor')
    print('Fornecedor cadastrado!!')
    sleep(0.5)
    
    menuFornecedores()

def editarFornecedor():
    pass

def listarFornecedores():
    os.system('cls')
    if not dadosFornecedor["ID_FORNECEDOR"]:
        print('ESTOQUE VAZIO!!')
        sleep(1)
        return menuFornecedores()
        
    id = dadosFornecedor['ID_FORNECEDOR']
    nome = dadosFornecedor['NOME_FORNECEDOR']
    
    fornecedor_string = ''
    maiorID = len(str(max( id )))

    fornecedor_string += (f'ID{" "*(maiorID-2)} │ NOME\n')

    for i in range(len(id)):
        
        maiorID    = len(str(max( id )))      - len(str( id[i] ))
        maiorNOME  = len(max( nome ,key=len)) - len( nome[i] )
        
        fornecedor_string += (f'{id[i]}{" "*(maiorID)} │ {nome[i]}\n')
    return fornecedor_string

#------/MENU FORNECEDORES------ 

#------MENU VENDAS------ 
def menuVendas():
    pass
#------/MENU VENDAS------ 

#------MENU CLIENTES------ 
def menuClientes():           
    while True:
        os.system('cls')

        try: #try vai rodar o bloco dentro dele, caso der algum erro, o except é chamado
            menu = int(input('''
    ---MENU DE CLIENTES---
    1.CADASTRAR CLIENTE
    2.EDITAR 
    3.LISTAR CLIENTES
    
    0. VOLTAR

R:'''))
            if menu > 3 or menu < 0:
                os.system('cls')
                print('OPÇÃO INVÁLIDA!!')
                sleep(0.5)
                continue

            match menu:
                case 1:
                    return cadastrarCliente()
                case 2:
                    return editarCliente()
                case 3:
                    return listaClientes(1)
                case 0:
                    return menuPrincipal()
                case _:
                    print("OPÇÃO INVÁLIDA!")    
                    continue

        except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel
            
            os.system('cls')
            print('APENAS NÚMEROS!!')
            sleep(0.5)
            continue

def cadastrarCliente(): 
    os.system('cls')
    print('---CADASTRO DE CLIENTE---\n')   

    while True:
        nome = str(input('NOME_CLIENTE DO CLIENTE: ')).upper()
        if nome in dadosCliente['NOME_CLIENTE']:
            print(f'Item {nome} já existe!!')
            sleep(0.5)
        break

    dadosCliente['ID_CLIENTE'].append(f'{len(dadosCliente["ID_CLIENTE"])+1}')     #------------
    dadosCliente['NOME_CLIENTE'].append(nome)                                     #fazer uma funcao para cadastrar cliente

    os.system('cls')
    print('Cliente cadastrado!!')
    sleep(0.5)
    
    menuClientes()
    
def listaClientes(flagParada = 0): #defino o parametro igual a zero para ele ser opcional, por que se o usuario nao digitar nada ele esta pre setado com um valor
    os.system('cls')
    correcaoEspacos = len(max(dadosCliente['NOME_CLIENTE'], key=len)) - 3 #max(dadosCliente, key=len) é o jeito de pegar a maior palavra por tamanho 
    
    print(f'ID │ NOME') 

    for i in range(len(dadosCliente['ID_CLIENTE'])):                                                                                #------------
        correcaoEspacos -= len(dadosCliente['NOME_CLIENTE'][i])                                                                     # estrutura de mostra de clientes
        print(f'{dadosCliente["ID_CLIENTE"][i]}  │ {dadosCliente["NOME_CLIENTE"][i]}{" "*correcaoEspacos}')                         #------------
    
    if flagParada == 1:
        sleep(1)
        input('\nPressione enter para sair')
        menuClientes()
    else:
        pass

def editarCliente():
    if not dadosCliente['ID_CLIENTE']: #python trata vazios como falso
        os.system('cls')
        print('SEM CLIENTES CADASTRADOS!!')
        sleep(0.5)
        menuClientes()

    os.system('cls')
    listaClientes(0)
    try: #try vai rodar o bloco dentro dele, caso der algum erro o except é chamado
        idCliente = int(input('\nQual item deseja editar? [ID]: '))
    except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel
        print('Apenas numeros!!')
        sleep(0.5)
        
    if idCliente not in dadosCliente['ID_CLIENTE']:
        print('OPÇÃO INVÁLIDA!!')
        sleep(0.5)
        menuClientes()
        
    else:
        while True:
            nomeEditado = str(input(f'\nRenomear [{dadosCliente["NOME_CLIENTE"][idCliente]}] para: ').upper())

            if nomeEditado == dadosCliente['NOME_CLIENTE'][idCliente]:
                print('O NOVO NOME NÃO PODE SER IGUAL AO ANTERIOR!!')
                sleep(0.5)

            elif nomeEditado in dadosCliente['NOME_CLIENTE']:
                print(f'"{nomeEditado}" JA EXISTE!!')
                sleep(0.5)
            else:    
                dadosCliente['NOME_CLIENTE'][idCliente] = nomeEditado
                print('ITEM RENOMEADO!!')
                sleep(0.5)
                break
        menuClientes()   
#------/MENU CLIENTES------ 
