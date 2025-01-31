import os
from time import sleep
from dados import *
from salvar_dados import *

#------FUNCAO LISTAGEM-------
    
def listagem(listaId, listaNome):
    listagem_string = ""    

    espacoId = max( len(str(max(listaId))), 2)
    espacoNome = max( len(max(listaNome, key=len)), 4)

    '''
    ex: max( len(str(max(id))), 2)
    nesse exemplo 'len(str(max(id)))' retorna um numero correspondente à maior palavra
    logo em seguida 'max( len(str(max(id))), 2)' atribui a 'espacoId' o maior entre os 2 ('len(str(max(id)))' ou 2)

    essa logica segue para todos os demais
    '''
    listagem_string += (f'┌─'
                    f'{"─"*espacoId}'
                    f'─┬─'
                    f'{"─"*espacoNome}'
                    f'─┐\n')
    listagem_string += (f'│ ID{" "*(espacoId-2)} '
                       f'│ NOME{" "*(espacoNome-4)} │\n')
    listagem_string += (f'├─'
                       f'{"─"*espacoId}'
                       f'─┼─'
                       f'{"─"*espacoNome}'
                       f'─┤\n')

    '''
    ex: QUANTIDADE{" "*(espacoQtd-10)}
    ja aqui, a correcao de espacos é feita de acordo com a variavel 'espacoQtd', pois se o maior 
    nome da lista 'dadosProduto['QUANTIDADE_PRODUTO']' for menor que 10 (quantidade de caracteres da palavra 'quantidade') o delimitador (barra vertical) ficará rente ao
    nome 'QUANTIDADE', ja se o maior nome da lista 'dadosProduto['QUANTIDADE_PRODUTO']' for maior que 10 o delimitador ficara a uma distancia de (tamanho da maior palavra menos 10) da palavra 'QUANTIDADE'
    '''

    for i in range(len(listaId)):
        listagem_string += (f'│ {listaId[i]}{" "*(espacoId-len(str(listaId[i])))} '
                           f'│ {listaNome[i]}{" "*(espacoNome-len(listaNome[i]))} │\n')

    listagem_string += (f'└─'
                f'{"─"*espacoId}'
                f'─┴─'
                f'{"─"*espacoNome}'
                f'─┘\n')

    '''
    ex: {categ[i]}{" "*(espacoCategCab-len(categ[i]))}

    aqui, segue a mesma logica do cabeçalho, mas a diferencça é que a quantidade de espacos sera subtraida da palavra 
    atual dentro do for (espacoCategCab-len(categ[i]) 
    '''
        
    return listagem_string

def mensagemFormat(mensagem:str):
    tamanhoMsg = len(mensagem)
    retorno = (
              f'╔═{"═"*tamanhoMsg}═╗\n'
              f'║ {mensagem} ║\n'           
              f'╚═{"═"*tamanhoMsg}═╝\n'
              )
    return retorno

#------/FUNCAO LISTAGEM-------

#------MENU PRINCIPAL-------
def menuPrincipal():
    obterCsv('Produtos')
    obterCsv('Clientes')
    obterCsv('Fornecedores')
    obterCsv('Categorias')
    
    while True:
        os.system('cls')
        try: #try vai rodar o bloco dentro dele, caso der algum erro o except é chamado
            menu = int(input('''
    
    ╔═════╣MENU PRINCIPAL╠═════╗
    ║    1.MENU PRODUTOS       ║
    ║    2.MENU CLIENTES       ║
    ║    3.MENU FORNECEDORES   ║
    ║    4.MENU ENTRADA        ║
    ║    5.MENU VENDAS         ║
    ║                          ║
    ║  0.SALVAR E SALVAR       ║             
    ╚══════════════════════════╝
                             
R:'''))
            match menu:
                case 1:
                    os.system('cls')
                    print(mensagemFormat('INDO PARA O MENU DE PRODUTOS...'))
                    sleep(1.5)
                    return menuProdutos()
                case 2:
                    os.system('cls')
                    print(mensagemFormat('INDO PARA O MENU DE CLIENTES...'))
                    sleep(1.5)
                    return menuClientes()
                case 3:
                    os.system('cls')
                    print(mensagemFormat('INDO PARA O MENU DE FORNECEDORES...'))
                    sleep(1.5)
                    return menuFornecedores() #pra fazer ainda
                case 4:
                    os.system('cls')
                    print(mensagemFormat('INDO PARA O MENU DE VENDAS...'))
                    sleep(1.5)
                    return menuVendas() #pra fazer ainda

                case 0:
                    print(mensagemFormat('SALVANDO E SAINDO...'))
                    sleep(1.5)
                    exit()
                case _:
                    print(mensagemFormat("OPÇÃO INVÁLIDA!!"))   
                    sleep(0.5)
                    continue 

        except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel
            os.system('cls')
            print(mensagemFormat('APENAS NÚMEROS!!'))
            sleep(1)
            continue  
#------/MENU PRINCIPAL-------

#------MENU PRODUTOS------ 
def menuProdutos():

    while True:
        os.system('cls')

     
        try: #try vai rodar o bloco dentro dele, caso der algum erro o except é chamado
            menu = int(input('''
                             
    ╔═══╣MENU DE PRODUTOS╠═══╗
    ║    1.CADASTRAR         ║
    ║    2.EDITAR            ║
    ║    3.EXCLUIR           ║
    ║    4.ENTRADA           ║
    ║    5.CATEGORIA         ║
    ║    6.MOSTRAR ESTOQUE   ║ 
    ║                        ║
    ║ 0.VOLTAR               ║             
    ╚════════════════════════╝
    

R:'''))

            match menu:
                case 1:
                    
                    return cadastrarProduto()
                case 2:
                    
                    return editarItem()
                case 3:
                    
                    return excluirItem() 
                case 4:
                    return entradaItem()
                case 5:
                    return cadastrarCategoria()
                case 6:
                    print(mostrarEstoque())
                    input(f'\n{mensagemFormat("PRESSIONE ENTER PARA SAIR")}')
                    
                    return menuProdutos()
                case 0:
                    
                    return menuPrincipal()
                case _:
                    print(mensagemFormat("OPÇÃO INVÁLIDA!"))   
                    sleep(1)
                    
                    return menuProdutos() 

        except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel
            os.system('cls')
            print(mensagemFormat('APENAS NÚMEROS!!'))
            sleep(0.5)
                
def entradaItem():
    ##for com {i}.{dadosProduto['NOME_PRODUTO'][i]
    os.system('cls')
    print('═══╣ENTRADA DE ITEM╠═══')
    
    os.system('cls')
    if not dadosProduto['ID_PRODUTO']:
        print('ESTOQUE VAZIO!!')
        sleep(1)
        menuProdutos()

    while True:
        print(mostrarEstoque())
        try: #try vai rodar o bloco dentro dele, caso der algum erro o except é chamado
            idProduto = int(input('\nQual item deseja dar entrada? [ID]: '))
        except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel
            print(mensagemFormat('Apenas numeros!!'))
            
        if idProduto not in dadosProduto['ID_PRODUTO']:
            print(mensagemFormat('OPÇÃO INVÁLIDA!!'))
            continue
        break

    while True:
        try:
            quantidadeItem = int(input(f'Dar entrada no item ID[{idProduto}] de: '))
            if quantidadeItem < 0:
                print(mensagemFormat("Apenas entradas de Estoque!"))
                continue
            break
        except ValueError:
            print(mensagemFormat('Apenas numeros!!'))

    for linha in range(len(dadosProduto['ID_PRODUTO'])):
        if dadosProduto['ID_PRODUTO'][linha] == idProduto:
            dadosProduto['QUANTIDADE_PRODUTO'][linha] += quantidadeItem
            break
    salvarCsv('Produto')
    print(mensagemFormat('Item adicionado com sucesso!!!'))
    sleep(0.5)
    menuProdutos()

def cadastrarProduto():
        while True:
            os.system('cls')
            print('═══╣CADASTRO DE ITEM╠═══')
            
            nomeProduto = str(input('\nNOME DO PRODUTO: ')).upper()
            if not nomeProduto:
                print(f"\n{mensagemFormat('NOME DO PRODUTO NAO PODE ESTAR EM BRANCO!!!')}")
                sleep(1)
            else:
                break
            
        while True:
            try: #try vai rodar o bloco dentro dele, caso der algum erro o except é chamado
                precoProduto = float(input('PRECO: '))
                break
            except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel
                print(mensagemFormat('Apenas números!!'))
                sleep(0.5)

        while True:
            try:
                if not dadosFornecedor["ID_FORNECEDOR"]:
                    print(mensagemFormat('ANTES CADASTRE UM FORNECEDOR!!!!'))
                    sleep(2.5)
                    fornecedor = cadastrarFornecedor()

                print(listarFornecedores("CadastrarProduto"))
                print(mensagemFormat("Enter para cadastrar agora"))
                fornecedor = (input(f'\n{nomeProduto} é vinculado a qual fornecedor? [ID]: '))
                if not fornecedor:
                    fornecedor = cadastrarFornecedor()
                     
                    break
                else:
                    fornecedor = int(fornecedor)
                    if fornecedor not in dadosFornecedor["ID_FORNECEDOR"]:
                        print(mensagemFormat(f"Fornecedor ID:{fornecedor} não encontrado"))
                        sleep(2.5)
                    else:
                        break
            
            except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel

                print('Apenas números!!')
                sleep(0.5)

        while True:
            try:
                if not dadosCategoria["ID_CATEGORIA"]:
                    print(mensagemFormat('ANTES CADASTRE UMA CATEGORIA!!!!'))
                    sleep(2.5)
                    categoria = cadastrarCategoria("CadastrarProduto")

                print(listarCategoria("CadastrarProduto"))
                print(mensagemFormat("Enter para cadastrar agora"))
                categoria = (input(f'\n{nomeProduto} é vinculado a qual categoria? [ID]: '))
                if not categoria:
                    categoria = cadastrarCategoria("CadastrarProduto")

                    break
                else:
                    categoria = int(categoria)
                    if categoria not in dadosCategoria["ID_CATEGORIA"]:
                        print(mensagemFormat(f"Categoria ID:{categoria} não encontrado"))
                        sleep(2.5)
                    else:
                        break

            except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel

                print('Apenas números!!')
                sleep(0.5)

        if not dadosProduto['ID_PRODUTO']:
            dadosProduto['ID_PRODUTO'].append(1)
        else:
            dadosProduto['ID_PRODUTO'].append(dadosProduto["ID_PRODUTO"][len(dadosProduto["ID_PRODUTO"])-1]+1)        
 
        dadosProduto['NOME_PRODUTO'].append(nomeProduto)                
        dadosProduto['PRECO_PRODUTO'].append(precoProduto)      
        dadosProduto['QUANTIDADE_PRODUTO'].append(0)
        

        for linha in range(len(dadosFornecedor['ID_FORNECEDOR'])):
            if dadosFornecedor['ID_FORNECEDOR'][linha] == fornecedor:
                dadosProduto['FORNECEDOR_PRODUTO'].append(dadosFornecedor['NOME_FORNECEDOR'][linha])
                break
        
        for linha in range(len(dadosCategoria['ID_CATEGORIA'])):
            if dadosCategoria['ID_CATEGORIA'][linha] == categoria:
                dadosProduto['CATEGORIA_PRODUTO'].append(dadosCategoria['NOME_CATEGORIA'][linha])
                break
            
        os.system('cls')
        salvarCsv('Produto')
        print(mensagemFormat('Item cadastrado!!'))

        sleep(1)
        menuProdutos()
        
def editarItem():
    if not dadosProduto['ID_PRODUTO']: #python trata vazios como falso
        os.system('cls')
        print('ESTOQUE VAZIO!!')
        sleep(0.5)
        return menuProdutos()

    while True:
        os.system('cls')
        print(mostrarEstoque())
        print('═══╣EDITAR PRODUTO╠═══')
        
        try: #try vai rodar o bloco dentro dele, caso der algum erro o except é chamado
            idProduto = int(input('\nQual item deseja editar? (ID): '))
            
        except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel
            print('Apenas numeros!!')
            
        if idProduto not in dadosProduto['ID_PRODUTO']:
            print('OPÇÃO INVÁLIDA!!')
            continue
        
        break
    
    opcao = int(input('''
  ╔════════════╗
  ║  1.NOME    ║
  ║  2.PREÇO   ║ 
  ║            ║
  ║ 0.VOLTAR   ║
  ╚════════════╝
R:'''))
    match opcao:
        case 1:
            for idDoProduto in range(len(dadosProduto["ID_PRODUTO"])):
                if dadosProduto["ID_PRODUTO"][idDoProduto] == idProduto:
                    nomeEditado = str(input(f'Renomear [{dadosProduto["NOME_PRODUTO"][idDoProduto]}] para: ').upper())
                    dadosProduto['NOME_PRODUTO'][idDoProduto] = nomeEditado
                    break
            print(mensagemFormat('NOME EDITADO COM SUCESSO!!'))
            salvarCsv('Produto')
            sleep(0.5)
            return menuProdutos()

        case 2:
            for idDoProduto in range(len(dadosProduto["ID_PRODUTO"])):                          
                if dadosProduto["ID_PRODUTO"][idDoProduto] == idProduto:
                    precoEditado = float(input(f'Trocar preço atual ({dadosProduto["PRECO_PRODUTO"][idDoProduto]}) para: ')) 
                    dadosProduto["PRECO_PRODUTO"][idDoProduto] = precoEditado
                    break
            print("PREÇO EDITADO COM SUCESSO!!!")
            salvarCsv('Produto')
            sleep(1)
            return menuProdutos()   
        case 0:
            return editarItem()
        case _:
            print("OPÇÃO INVÁLIDA!")   
            sleep(0.5)
            return editarItem()
        
def excluirItem():
    while True:

        print(mostrarEstoque())
        
        try: #try vai rodar o bloco dentro dele, caso der algum erro o except é chamado
            excluir = (input('\nQual item deseja exlcuir do seu estoque? [ID]:\n(Enter para cancelar)\n'))
            if excluir == "":
                return menuProdutos()
            
            excluir = int(excluir)
            if excluir not in dadosProduto['ID_PRODUTO']:
                print('ESSE ITEM NÃO EXISTE')
                sleep(1)
                continue
            else:
                break
        except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel
            print('APENAS NUMEROS!!')
            sleep(1)
        
    for i in range(len(dadosProduto['ID_PRODUTO'])):
        if excluir == dadosProduto['ID_PRODUTO'][i]:
            dadosProduto['ID_PRODUTO'].pop(i)
            dadosProduto['NOME_PRODUTO'].pop(i)
            dadosProduto['QUANTIDADE_PRODUTO'].pop(i)
            dadosProduto['PRECO_PRODUTO'].pop(i)
            dadosProduto['FORNECEDOR_PRODUTO'].pop(i)
            dadosProduto['CATEGORIA_PRODUTO'].pop(i)
            print('ITEM REMOVIDO COM SUCESSO!')    
            sleep(1)
            break
    
    salvarCsv('Produto')
    return menuProdutos()
        
def cadastrarCategoria(parametro = ''):
    
    while True:
        os.system('cls')
        
            
        try:
            menu = int(input('''
    ---MENU DE CATEGORIA---
    1.CRIAR CATEGORIA
    2.EDITAR CATEGORIA
    3.EXCLUIR CATEGORIA

    0.VOLTAR

R:'''))
        except ValueError:
            os.system('cls')
            print('APENAS NUMEROS!!')
            sleep(1)
            
        match menu:
            case 1:
                nomeCateg = input('DEFINA O NOME DA CATEGORIA:\n').upper()
                if not dadosCategoria["ID_CATEGORIA"]:
                    dadosCategoria["ID_CATEGORIA"].append(1)
                    dadosCategoria["NOME_CATEGORIA"].append(nomeCateg)
                else:
                    dadosCategoria["ID_CATEGORIA"].append(dadosCategoria["ID_CATEGORIA"][len(dadosCategoria["ID_CATEGORIA"])-1] +1 )
                    dadosCategoria["NOME_CATEGORIA"].append(nomeCateg)
                    
                salvarCsv('Categoria')
                print('CATEGORIA CRIADA!!')
                sleep(1.5)
                if parametro == "CadastrarProduto":
                    
                    return

            case 2:
                while True:
                    os.system("cls")
                    print(listarCategoria())
                    try:
                        idCateg = int(input("QUAL CATEGORIA? [ID]\n"))
                        if idCateg not in dadosCategoria["ID_CATEGORIA"]:
                            print("OPÇÃO INVÁLIDA!!")
                            sleep(1.5)
                        else:
                            break
                    except ValueError:
                        print("APENAS NUMEROS!!")
                        
                   
                for i in range(len(dadosCategoria["ID_CATEGORIA"])):
                    if dadosCategoria["ID_CATEGORIA"][i] == idCateg:
                        nome = input("NOVO NOME: ").upper()
                        dadosCategoria["NOME_CATEGORIA"][i] = nome
                        break
                os.system('cls')
                print(f"CATEGORIA EDITADA PARA: {nome}!!")
                sleep(1.5)
                salvarCsv("Categoria")
                    
            case 3:
                while True:
                    os.system("cls")
                    print(listarCategoria())
                    try:
                        idCateg = int(input("QUAL CATEGORIA? [ID]\n"))
                        break
                    except ValueError:
                        print("APENAS NUMEROS!!")

                if idCateg not in dadosCategoria["ID_CATEGORIA"]:
                    print("OPÇÃO INVÁLIDA!!")
                    sleep(1.5)
                else:   
                    for i in range(len(dadosCategoria["ID_CATEGORIA"])):
                        if dadosCategoria["ID_CATEGORIA"][i] == idCateg:
                            print(f"CATEGORIA [{dadosCategoria["ID_CATEGORIA"]}] REMOVIDO!!")
                            dadosCategoria["ID_CATEGORIA"].pop(i)
                            dadosCategoria["NOME_CATEGORIA"].pop(i)
                            break

            case 0:
                return menuProdutos()
            
            case _:
                print("OPÇÃO INVÁLIDA!")   
                sleep(0.5)
                return cadastrarCategoria()
                          
def listarCategoria(opcao = "Categoria"):
    os.system('cls')
    if opcao == "CadastrarCategoria":
        if not dadosCategoria["ID_CATEGORIA"]:
            print('SEM CATEGORIAS!!')
            sleep(1)
    elif opcao == "Categoria":
        if not dadosCategoria["ID_CATEGORIA"]:
            print('SEM CATEGORIAS!!')
            sleep(1)
            return cadastrarCategoria()
        
    return listagem(dadosCategoria['ID_CATEGORIA'],dadosCategoria['NOME_CATEGORIA'] )    

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
    categ = dadosProduto['CATEGORIA_PRODUTO']
    
    estoque_string = ""

    espacoId = max( len(str(max(id))), 2)
    espacoNome = max( len(max(nome, key=len)), 4)
    espacoPreco = max( len(str(max(preco))), 5)
    espacoQtd = max( len(str(max(qtd))), 10)
    espacoCateg = max( len(max(categ, key=len)), 9)
    espacoForn = max( len(max(forn, key=len)), 10)

    '''
    ex: max( len(str(max(id))), 2)
    nesse exemplo 'len(str(max(id)))' retorna um numero correspondente à maior palavra
    logo em seguida 'max( len(str(max(id))), 2)' atribui a 'espacoId' o maior entre os 2 ('len(str(max(id)))' ou 2)

    essa logica segue para todos os demais
    '''
    estoque_string += (f'┌─'
                    f'{"─"*espacoId}'
                    f'─┬─'
                    f'{"─"*espacoNome}'
                    f'─┬─'
                    f'{"─"*espacoPreco}'
                    f'─┬─'
                    f'{"─"*espacoQtd}'
                    f'─┬─'
                    f'{"─"*espacoCateg}'
                    f'─┬─'
                    f'{"─"*espacoForn}'
                    f'─┐\n')

    estoque_string += (f'│ ID{" "*(espacoId-2)} '
                       f'│ NOME{" "*(espacoNome-4)} '
                       f'│ PRECO{" "*(espacoPreco-5)} '
                       f'│ QUANTIDADE{" "*(espacoQtd-10)} '
                       f'│ CATEGORIA{" "*(espacoCateg-9)} '
                       f'│ FORNECEDOR{" "*(espacoForn-10)} │\n')

    estoque_string += (f'├─'
                       f'{"─"*espacoId}'
                       f'─┼─'
                       f'{"─"*espacoNome}'
                       f'─┼─'
                       f'{"─"*espacoPreco}'
                       f'─┼─'
                       f'{"─"*espacoQtd}'
                       f'─┼─'
                       f'{"─"*espacoCateg}'
                       f'─┼─'
                       f'{"─"*espacoForn}'
                       f'─┤\n')

    '''┴
    ┘
    ┐
    ┌
    ┘
    └
    ┬
    ┤
    ├
    ┼
    ─ '''

    '''
    ex: QUANTIDADE{" "*(espacoQtd-10)}
    ja aqui, a correcao de espacos é feita de acordo com a variavel 'espacoQtd', pois se o maior 
    nome da lista 'dadosProduto['QUANTIDADE_PRODUTO']' for menor que 10 (quantidade de caracteres da palavra 'quantidade') o delimitador (barra vertical) ficará rente ao
    nome 'QUANTIDADE', ja se o maior nome da lista 'dadosProduto['QUANTIDADE_PRODUTO']' for maior que 10 o delimitador ficara a uma distancia de (tamanho da maior palavra menos 10) da palavra 'QUANTIDADE'
    '''

    for i in range(len(id)):
        estoque_string += (f'│ {id[i]}{" "*(espacoId-len(str(id[i])))} '
                           f'│ {nome[i]}{" "*(espacoNome-len(nome[i]))} '
                           f'│ {preco[i]}{" "*(espacoPreco-len(str(preco[i])))} '
                           f'│ {qtd[i]}{" "*(espacoQtd-len(str(qtd[i])))} '
                           f'│ {categ[i]}{" "*(espacoCateg-len(categ[i]))} '
                           f'│ {forn[i]}{" "*(espacoForn-len(forn[i]))} │\n')

    estoque_string += (f'└─'
                f'{"─"*espacoId}'
                f'─┴─'
                f'{"─"*espacoNome}'
                f'─┴─'
                f'{"─"*espacoPreco}'
                f'─┴─'
                f'{"─"*espacoQtd}'
                f'─┴─'
                f'{"─"*espacoCateg}'
                f'─┴─'
                f'{"─"*espacoForn}'
                f'─┘\n')

    '''
    ex: {categ[i]}{" "*(espacoCategCab-len(categ[i]))}

    aqui, segue a mesma logica do cabeçalho, mas a diferencça é que a quantidade de espacos sera subtraida da palavra 
    atual dentro do for (espacoCategCab-len(categ[i]) 
    '''
        
    return estoque_string


#------/MENU PRODUTOS------ 

#------MENU FORNECEDORES------ 
def menuFornecedores():
    while True:
        os.system('cls')
        try: #try vai rodar o bloco dentro dele, caso der algum erro o except é chamado
            menu = int(input('''
                             
    ╔══════MENU FORNECEDOR══════╗
    ║   1.CADASTRAR FORNECEDOR  ║
    ║   2.EDITAR FORNECEDOR     ║
    ║   3.LISTAR FORNECEDOR     ║
    ║                           ║
    ║  0.SALVAR E SALVAR        ║             
    ╚═══════════════════════════╝              
R:'''))

            match menu:
                case 1:
                    return cadastrarFornecedor()
                case 2:
                    return editarFornecedor()
                case 3:
                    print(listarFornecedores())
                    sleep(0.5)
                    input(f'{mensagemFormat("PRESSIONE ENTER PARA SAIR")}')
                    
                    return menuFornecedores()
                case 0:
                    return menuPrincipal()
                case _:
                    print(mensagemFormat("OPÇÃO INVÁLIDA!")) 
                    continue

        except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel
            os.system('cls')
            print('APENAS NÚMEROS!!')
            sleep(0.5)
            continue

def cadastrarFornecedor(parametro = "CadastroFornecedor"): #parametro fica opcional, mas quando chamado sem nenhum parametro "CadastroFornecedor" é o valor padrão
    os.system('cls')
    print('═══╣CADASTRO DE FORNECEDOR╠═══\n')   

    nome = str(input('NOME: ')).upper()
    if not dadosFornecedor["ID_FORNECEDOR"]:
        dadosFornecedor["ID_FORNECEDOR"].append(1)
        idFornecedor = 1
    else:
        idFornecedor = dadosFornecedor["ID_FORNECEDOR"][len(dadosFornecedor["ID_FORNECEDOR"])-1] +1 
        dadosFornecedor['ID_FORNECEDOR'].append(idFornecedor)
    dadosFornecedor['NOME_FORNECEDOR'].append(nome)                                   

    os.system('cls')
    
    salvarCsv('Fornecedor')
    print(mensagemFormat('FORNECEDOR CADASTRADO!!'))
    sleep(1.5)
    if parametro == "CadastroProduto":
        return idFornecedor
    
    return menuFornecedores()

def editarFornecedor():
    if not dadosFornecedor['ID_FORNECEDOR']: #python trata vazios como falso
        os.system('cls')
        print('SEM FORNECEDORES CADASTRADOS!!')
        sleep(0.5)
        return menuFornecedores()


    os.system('cls')
    print(listarFornecedores())
    print('═══╣EDITAR FORNECEDOR╠═══')
    
    try: #try vai rodar o bloco dentro dele, caso der algum erro o except é chamado
        idFornecedor = int(input('Qual item deseja editar? [ID]: '))
    except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel
        print(mensagemFormat('APENAS NUMEROS!!'))
        
    if idFornecedor not in dadosFornecedor['ID_FORNECEDOR']:
        print(mensagemFormat('OPÇÃO INVÁLIDA!!'))
        sleep(0.5)
        return editarFornecedor()
    
    for idDoFornecedor in dadosFornecedor["ID_FORNECEDOR"]:
        if dadosFornecedor["ID_FORNECEDOR"][idDoFornecedor] == idFornecedor:
            nomeEditado = str(input(f'Renomear [{dadosFornecedor["NOME_FORNECEDOR"][idFornecedor]}] para: ').upper())
            dadosFornecedor['NOME_FORNECEDOR'][idDoFornecedor] = nomeEditado
            break
    print(mensagemFormat('NOME EDITADO COM SUCESSO!!'))
    salvarCsv('Fornecedor')
    sleep(0.5)
    return menuFornecedores()

def listarFornecedores(opcao = "Fornecedor"):
    os.system('cls')
    if opcao == "CadastrarProduto":
        if not dadosFornecedor["ID_FORNECEDOR"]:
            print('SEM FORNECEDORES CADASTRADOS!!')
            sleep(1)
    elif opcao == "Fornecedor":
        if not dadosFornecedor["ID_FORNECEDOR"]:
            print('SEM FORNECEDORES CADASTRADOS!!')
            sleep(1)
            return menuFornecedores()
    
    return listagem(dadosFornecedor['ID_FORNECEDOR'],dadosFornecedor['NOME_FORNECEDOR'] )


#------/MENU FORNECEDORES------ 

#------MENU VENDAS------ 
def menuVendas():

    while True:
        os.system('cls')

     
        try: #try vai rodar o bloco dentro dele, caso der algum erro o except é chamado
            menu = int(input('''
    ╔══╣MENU DE VENDAS══╗
    ║    1.EM BREVE     ║
    ║    2.EM BREVE     ║
    ║    3.EM BREVE     ║
    ║                   ║
    ║  0.VOLTAR         ║
    ╚═══════════════════╝
R:'''))
            

            match menu:
                case 1:
                    return soon()

                case 2:
                    return soon()

                case 3:
                    return soon()

                case 0:
                    
                    return menuPrincipal()
                case _:
                    print(mensagemFormat("OPÇÃO INVÁLIDA!"))   
                    sleep(0.7)
                    continue

        except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel
            os.system('cls')
            print(mensagemFormat('APENAS NÚMEROS!!'))
            sleep(0.5)   

def soon():
    os.system('cls')
    print(mensagemFormat('IMPLEMENTAÇÃO EM BREVE)'))
    sleep(1.5)
    os.system('cls')
    print(mensagemFormat('VOLTANDO PARA MENU PRINCIPAL...'))
    sleep(1.5)
    return menuPrincipal() 
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
            
            match menu:
                case 1:
                    return cadastrarCliente()
                case 2:
                    return editarCliente()
                case 3:
                    print(listarClientes())
                    sleep(0.5)
                    input('\nPRESSIONE ENTER PARA SAIR')
                    return menuClientes()
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
    print('═══╣CADASTRO DE CLIENTE╠═══\n')   

    nome = str(input('NOME CLIENTE DO CLIENTE: ')).upper()

    dadosCliente['ID_CLIENTE'].append(len(dadosCliente["ID_CLIENTE"]))     #------------
    dadosCliente['NOME_CLIENTE'].append(nome)                                     #fazer uma funcao para cadastrar cliente
    
    os.system('cls')

    salvarCsv('Cliente')
    print('CLIENTE CADASTRADO!!')
    sleep(0.5)
    return menuClientes()
    
def listarClientes(): #defino o parametro igual a zero para ele ser opcional, por que se o usuario nao digitar nada ele esta pre setado com um valor
    os.system('cls')
    
    if not dadosCliente["ID_CLIENTE"]:
        print('SEM CLIENTES CADASTRADOS!!')
        sleep(0.5)
        return menuClientes()
        
    
    return listagem(dadosCliente['ID_CLIENTE'], dadosCliente['NOME_CLIENTE'])

def editarCliente():
    if not dadosCliente['ID_CLIENTE']: #python trata vazios como falso
        os.system('cls')
        print('SEM CLIENTES CADASTRADOS!!')
        sleep(0.5)
        return menuClientes()

    os.system('cls')
    print(listarClientes())
    try: #try vai rodar o bloco dentro dele, caso der algum erro o except é chamado
        idCliente = int(input('\nQual item deseja editar? [ID]:'))
    except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel
        print('APENAS NUMEROS!!')
        sleep(0.5)
        
    if idCliente not in dadosCliente['ID_CLIENTE']:
        print('OPÇÃO INVÁLIDA!!')
        sleep(0.5)
        return editarCliente()
        
    else:
        for idDoCliente in dadosCliente["ID_CLIENTE"]:
            if dadosCliente["ID_CLIENTE"][idDoCliente] == idCliente:
                nomeEditado = str(input(f'\nRenomear [{dadosCliente["NOME_CLIENTE"][idDoCliente]}] para: ').upper())
                dadosCliente['NOME_CLIENTE'][idDoCliente] = nomeEditado
                sleep(0.5)
                break
        salvarCsv('Cliente')
        print(mensagemFormat('NOME EDITADO COM SUCESSO!!'))
        sleep(0.5)
        return menuClientes()   
#------/MENU CLIENTES------ 
