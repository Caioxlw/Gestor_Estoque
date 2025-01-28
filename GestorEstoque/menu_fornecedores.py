import os
from time import sleep
from dados import dadosFornecedor
from menu_clientes import menuClientes

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
                    cadastrarFornecedor()
                case 2:
                    editarFornecedor()
                case 3:
                    listarFornecedores(1)
                case 0:
                    return
                case _:
                    print("OPÇÃO INVÁLIDA!") 
                    menuFornecedores()

        except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel
            os.system('cls')
            print('APENAS NÚMEROS!!')
            sleep(0.5)
            continue

def cadastrarFornecedor():
    os.system('cls')
    print('---CADASTRO DE FORNECEDOR---\n')   

    while True:
        nome = str(input('NOME CLIENTE DO FORNECEDOR: ')).upper()
        if nome in dadosFornecedor['NOME_FORNECEDOR']:
            print(f'Item {nome} já existe!!')
            sleep(0.5)
        break

    dadosFornecedor['ID_FORNECEDOR'].append(f'{len(dadosFornecedor['ID_FORNECEDOR'])+1}')     #------------
    dadosFornecedor['NOME_FORNECEDOR'].append(nome)                                      #fazer uma funcao para cadastrar cliente

    os.system('cls')
    print('Fornecedor cadastrado!!')
    sleep(0.5)
    
    menuFornecedores()

def editarFornecedor():
    pass

def listarFornecedores(flagParada = 0):
    os.system('cls')
    correcaoEspacos = len(max(dadosFornecedor['NOME_FORNECEDOR'], key=len)) - 3 #max(dadosFornecedor, key=len) é o jeito de pegar a maior palavra por tamanho 
    
    print(f'ID │ NOME') 

    for i in range(len(dadosFornecedor['ID_FORNECEDOR'])):                                                                            #------------
        correcaoEspacos -= len(dadosFornecedor['NOME_FORNECEDOR'][i])                                                                 # estrutura de mostra de clientes
        print(f'{dadosFornecedor["ID_FORNECEDOR"][i]}  │ {dadosFornecedor["NOME_FORNECEDOR"][i]}{' '*correcaoEspacos}')               #------------
    
    if flagParada == 1:
        sleep(1)
        input('\nPressione enter para sair')
        menuClientes()
    else:
        pass
