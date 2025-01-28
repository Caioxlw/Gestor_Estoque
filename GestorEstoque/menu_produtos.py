import os
from time import sleep
from dados import dadosProduto
from salvar_dados import salvarProdutosCsv
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
                    cadastrar()
                case 2:
                    editarItem()
                case 3:
                    excluirItem() 
                case 4:
                    entradaItem()
                case 5:
                    mostrarEstoque(1)
                case 0:
                    return
                case _:
                    print("OPÇÃO INVÁLIDA!")   
                    sleep(0.5)
                    menuProdutos() 

        except ValueError:
            os.system('cls')
            print('APENAS NÚMEROS!!')
            sleep(0.5)
                
def entradaItem():
    pass

def cadastrar():
        os.system('cls')
        print('---CADASTRO DE ITEM---')

        while True:
            nomeProduto = str(input('\nNOME DO PRODUTO: ')).upper()
            if nomeProduto in dadosProduto['NOME_PRODUTO']:
                print(f'Item {nomeProduto} já existe!!')
                sleep(0.5)
            else:
                break
            
        while True:
            try: #try vai rodar o bloco dentro dele, caso der algum erro o except é chamado
                quantidadeProduto = int(input('QUANTIDADE: '))
                break
            except ValueError:
                print('Apenas numeros!!')
                sleep(0.5)

        dadosProduto['ID_PRODUTO'].append(f'{len(dadosProduto['ID_PRODUTO'])}')           #--------------
        dadosProduto['NOME_PRODUTO'].append(nomeProduto)                   #fazer uma funcao para adicionar item ao estoque
        dadosProduto['QUANTIDADE_PRODUTO'].append(quantidadeProduto)       #--------------

        os.system('cls')
        salvarProdutosCsv()
        print('Item cadastrado!!')

        sleep(0.5)
        menuProdutos()
        
def editarItem():
    if not dadosProduto['ID_PRODUTO']: #python trata vazios como falso
        os.system('cls')
        print('Estoque vazio!!')
        
        menuProdutos()

    os.system('cls')
    mostrarEstoque()
    try: #try vai rodar o bloco dentro dele, caso der algum erro o except é chamado
        idProduto = int(input('Qual item deseja editar? [ID]: '))
    except ValueError:
        print('Apenas numeros!!')
        
    if idProduto not in dadosProduto['ID_PRODUTO']:
        print('OPÇÃO INVÁLIDA!!')
        
    else:
        while True:
            nomeEditado = str(input(f'Renomear [{dadosProduto['NOME_PRODUTO'][idProduto]}] para: ').upper())

            if nomeEditado == dadosProduto['NOME_PRODUTO'][idProduto]:
                print('NOVO NOME NÃO PODE SER IGUAL AO ANTERIOR!!')
    
            elif nomeEditado in dadosProduto['NOME_PRODUTO']:
                print('ESSE NOME JA EXISTE!!')

            else:    
                dadosProduto['NOME_PRODUTO'][idProduto] = nomeEditado
                print('ITEM RENOMEADO!!')
    
    
                break
        salvarProdutosCsv()
        menuProdutos()

def excluirItem():
        correcaoID = False
        mostrarEstoque()

        try: #try vai rodar o bloco dentro dele, caso der algum erro o except é chamado
            excluir = int(input('\nQual item deseja exlcuir do seu estoque? [ID]: '))
        except ValueError:
            print('Apenas numeros!!')

        for id in dadosProduto['ID_PRODUTO']:
            if correcaoID:
                dadosProduto['ID_PRODUTO'][id] == dadosProduto['ID_PRODUTO'][id] - 1

            if excluir == dadosProduto['ID_PRODUTO'][id]:
                dadosProduto['ID_PRODUTO'].pop(id)
                dadosProduto['NOME_PRODUTO'].pop(id)
                dadosProduto['QUANTIDADE_PRODUTO'].pop(id)
                correcaoID = True # JA APAGOU O ITEM
        salvarProdutosCsv()
        print('Item removido com sucesso!')

def mostrarEstoque(flagParada = 0): #defino o parametro igual a zero para ele ser opcional, por que se o usuario nao digitar nada ele esta pre setado com um valor
    os.system('cls')
    correcaoEspacos   = len(max(dadosProduto['NOME_PRODUTO'], key=len)) - 3
    correcaoEspacosID = len(max(dadosProduto['ID_PRODUTO'], key=len)) 
    
    print(f'''ID{' '*correcaoEspacosID}│ NOME{' '*correcaoEspacos}│ QUANTIDADE''') 

    for i in range(len(dadosProduto['ID_PRODUTO'])):                                                                                                                                #---------
            correcaoEspacos   = len(max(dadosProduto['NOME_PRODUTO'], key=len)) - len(dadosProduto['NOME_PRODUTO'][i])                                                              #estrutura de mostrar estoque
            correcaoEspacosID = len(max(dadosProduto['ID_PRODUTO'], key=len))   - len(dadosProduto['ID_PRODUTO'][i])                                         
            print(f'{dadosProduto["ID_PRODUTO"][i]}{' '*correcaoEspacosID}  │ {dadosProduto["NOME_PRODUTO"][i]}{' '*correcaoEspacos} │ {dadosProduto["QUANTIDADE_PRODUTO"][i]}')    #---------
        
    if flagParada == 1:
        sleep(1)
        input('\nPressione enter para sair')
        menuProdutos()