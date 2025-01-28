import os
from time import sleep
from menu_produtos import menuProdutos
from menu_clientes import menuClientes
from menu_fornecedores import menuFornecedores
from menu_vendas import menuVendas
from salvar_dados import obterProdutosCsv


def menuPrincipal():
    obterProdutosCsv()
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
                    menuPrincipal() 

        except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel
            os.system('cls')
            print('APENAS NÚMEROS!!')
            sleep(0.5)
            continue