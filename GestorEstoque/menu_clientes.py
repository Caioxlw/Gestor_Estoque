import os
from time import sleep
from dados import dadosCliente
from salvar_dados import salvar_csv

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
                    cadastrarCliente()
                case 2:
                    editarCliente()
                case 3:
                    listaClientes(1)
                case 0:
                    return
                case _:
                    print("OPÇÃO INVÁLIDA!")    
                    menuClientes()

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

    dadosCliente['ID_CLIENTE'].append(f'{len(dadosCliente['ID_CLIENTE'])+1}')     #------------
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
        print(f'{dadosCliente["ID_CLIENTE"][i]}  │ {dadosCliente["NOME_CLIENTE"][i]}{' '*correcaoEspacos}')                         #------------
    
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
            nomeEditado = str(input(f'\nRenomear [{dadosCliente['NOME_CLIENTE'][idCliente]}] para: ').upper())

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
