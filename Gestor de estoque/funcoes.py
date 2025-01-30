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
                    menuProdutos()
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
    2.EDITAR
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
                    
                    cadastrarProduto()
                case 2:
                    
                    editarItem()
                case 3:
                    
                    excluirItem() 
                case 4:
                    entradaItem()
                case 5:
                    print(mostrarEstoque())
                    input('\nPressione enter para sair')
                    
                    menuProdutos()
                case 0:
                    
                    menuPrincipal()
                case _:
                    print("OPÇÃO INVÁLIDA!")   
                    sleep(0.5)
                    
                    menuProdutos() 

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

    while True:
        print(mostrarEstoque())
        try: #try vai rodar o bloco dentro dele, caso der algum erro o except é chamado
            idProduto = int(input('\nQual item deseja dar entrada? [ID]: '))
        except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel
            print('Apenas numeros!!')
            
        if idProduto not in dadosProduto['ID_PRODUTO']:
            print('OPÇÃO INVÁLIDA!!')
            continue
        break

    while True:
        try:
            quantidadeItem = int(input(f'Dar entrada no item ID[{idProduto}] de: '))
            if quantidadeItem < 0:
                print("Apenas entradas de Estoque!")
                continue
            break
        except ValueError:
            print('Apenas numeros!!')
    
    dadosProduto['QUANTIDADE_PRODUTO'][idProduto] += quantidadeItem

    salvarCsv('Produto')
    menuProdutos()

def cadastrarProduto():
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
                print(listarFornecedores())
                fornecedor = (input(f'{nomeProduto} é vinculado a qual fornecedor? [ID]\nEnter para cadastrar agora\n'))
                if not fornecedor:
                    cadastrarFornecedor('CadastroProduto')
                    break
                else:
                    
                    fornecedor = int(fornecedor)
                    if fornecedor not in dadosFornecedor["ID_FORNECEDOR"]:
                        print(f"Fornecedor ID:{fornecedor} não encontrado")
                    else:
                        break
            
            except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel

                print('Apenas números!!')
                sleep(0.5)

        dadosProduto['ID_PRODUTO'].append(len(dadosProduto["ID_PRODUTO"]))         
        dadosProduto['NOME_PRODUTO'].append(nomeProduto)                
        dadosProduto['PRECO_PRODUTO'].append(precoProduto)      
        dadosProduto['QUANTIDADE_PRODUTO'].append(0)

        for linha in dadosFornecedor['ID_FORNECEDOR']:
            if dadosFornecedor['ID_FORNECEDOR'][linha] == fornecedor:
                dadosProduto['FORNECEDOR_PRODUTO'].append(dadosFornecedor['NOME_FORNECEDOR'][linha])
                break
            
        os.system('cls')
        salvarCsv('Produtos')
        print('Item cadastrado!!')

        sleep(1)
        menuProdutos()
        
def editarItem():
    if not dadosProduto['ID_PRODUTO']: #python trata vazios como falso
        os.system('cls')
        print('Estoque vazio!!')
        sleep(0.5)
        return menuProdutos()

    while True:
        os.system('cls')
        print(mostrarEstoque())
        print('---EDITAR PRODUTO---')
        
        try: #try vai rodar o bloco dentro dele, caso der algum erro o except é chamado
            idProduto = int(input('Qual item deseja editar? [ID]: '))
        except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel
            print('Apenas numeros!!')
            
        if idProduto not in dadosProduto['ID_PRODUTO']:
            print('OPÇÃO INVÁLIDA!!')
            continue
        break
    
    opcao = int(input('''
    1.NOME
    2.PREÇO

    0.VOLTAR

R:'''))
    match opcao:
        case 1:
            for idDoProduto in dadosProduto["ID_PRODUTO"]:
                if dadosProduto["ID_PRODUTO"][idDoProduto] == idProduto:
                    nomeEditado = str(input(f'Renomear [{dadosProduto["NOME_PRODUTO"][idProduto]}] para: ').upper())
                    break
            dadosProduto['NOME_PRODUTO'][idProduto] = nomeEditado
            print('NOME EDITADO COM SUCESSO!!')
            salvarCsv('Produto')
            sleep(0.5)
            return menuProdutos()

        case 2:
            for idDoProduto in dadosProduto["ID_PRODUTO"]:
                if dadosProduto["ID_PRODUTO"][idDoProduto] == idProduto:
                    precoEditado = float(input(f'Trocar preço atual ({dadosProduto["PRECO_PRODUTO"][idProduto]}) para: ')) 
                    break
            dadosProduto["PRECO_PRODUTO"][idProduto] = precoEditado
            print("PREÇO EDITADO COM SUCESSO!!!")
            salvarCsv('Produto')
            sleep(0.5)
            return menuProdutos()    
                        

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
            print('Item removido com sucesso!')    
            sleep(1)
            break
    
    salvarCsv('Produto')
    return menuProdutos()

def mostrarEstoque(): #defino o parametro igual a zero para ele ser opcional, por que se o usuario nao digitar nada ele esta pre setado com um valor
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

    estoque_string += (f'ID{" "*(maiorID-2)} │ NOME{" "*(maiorNOME-4)} │ PRECO{" "*(maiorPRECO-5)} │ QUANTIDADE{" "*(maiorQTD-10)} │ FORNECEDOR\n')
    # estoque_string += (f'') #fazer uma listrinha para separar do cabecalho

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

def cadastrarFornecedor(parametro = "CadastroFornecedor"): #parametro fica opcional, mas quando chamado sem nenhum parametro "CadastroFornecedor" é o valor padrão
    os.system('cls')
    print('---CADASTRO DE FORNECEDOR---\n')   

    while True:
        nome = str(input('NOME: ')).upper()
        if nome in dadosFornecedor['NOME_FORNECEDOR']:
            print(f'Item {nome} já existe!!')
            sleep(0.5)
        break

    dadosFornecedor['ID_FORNECEDOR'].append(len(dadosFornecedor["ID_FORNECEDOR"]))    
    dadosFornecedor['NOME_FORNECEDOR'].append(nome)                                    

    os.system('cls')
    
    salvarCsv('Fornecedor')
    print('Fornecedor cadastrado!!')
    sleep(0.5)
    if parametro != "CadastroProduto":
        return menuFornecedores()

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
    maiorID = len(max(str( id )))

    fornecedor_string += (f'ID{" "*(maiorID-2)} │ NOME\n')

    for i in range(len(id)):
        
        maiorID    = len(max(str( id ), key=len))      - len(str( id[i] ))
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
                    return listaClientes()
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
        nome = str(input('NOME CLIENTE DO CLIENTE: ')).upper()
        if nome in dadosCliente['NOME_CLIENTE']:
            print(f'Item {nome} já existe!!')
            sleep(0.5)
        break

    dadosCliente['ID_CLIENTE'].append(len(dadosCliente["ID_CLIENTE"]))     #------------
    dadosCliente['NOME_CLIENTE'].append(nome)                                     #fazer uma funcao para cadastrar cliente
    salvarCsv('Cliente')
    
    os.system('cls')
    print('Cliente cadastrado!!')
    sleep(0.5)
    return menuClientes()
    
def listaClientes(): #defino o parametro igual a zero para ele ser opcional, por que se o usuario nao digitar nada ele esta pre setado com um valor
    os.system('cls')
    
    if not dadosCliente["ID_CLIENTE"]:
        print('SEM CLIENTES!!')
        sleep(1)
        return menuClientes()
        
    id = dadosCliente['ID_CLIENTE']
    nome = dadosCliente['NOME_CLIENTE']
    
    cliente_string = ''
    maiorID = len(str(max( id )))

    cliente_string += (f'ID{" "*(maiorID-2)} │ NOME\n')

    for i in range(len(id)):
        
        maiorID    = len(str(max( id ))) - len(str( id[i] ))
        cliente_string += (f'{id[i]}{" "*(maiorID)} │ {nome[i]}\n')
    return cliente_string


def editarCliente():
    if not dadosCliente['ID_CLIENTE']: #python trata vazios como falso
        os.system('cls')
        print('SEM CLIENTES CADASTRADOS!!')
        sleep(0.5)
        return menuClientes()

    os.system('cls')
    print(listaClientes())
    try: #try vai rodar o bloco dentro dele, caso der algum erro o except é chamado
        idCliente = int(input('\nQual item deseja editar? [ID]:'))
    except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel
        print('Apenas numeros!!')
        sleep(0.5)
        
    if idCliente not in dadosCliente['ID_CLIENTE']:
        print('OPÇÃO INVÁLIDA!!')
        sleep(0.5)
        return menuClientes()
        
    else:
        for idDoCliente in dadosCliente["ID_CLIENTE"]:
            if dadosCliente["ID_CLIENTE"][idDoCliente] == idCliente:
                nomeEditado = str(input(f'\nRenomear [{dadosCliente["NOME_CLIENTE"][idDoCliente]}] para: ').upper())
                
                dadosCliente['NOME_CLIENTE'][idDoCliente] = nomeEditado
                print('ITEM RENOMEADO!!')
                sleep(0.5)
                break
        salvarCsv('Cliente')
        print('ITEM RENOMEADO!!')
        sleep(0.5)
        return menuClientes()   
#------/MENU CLIENTES------ 
