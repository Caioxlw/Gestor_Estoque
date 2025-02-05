import os
from time import sleep
from dados import *
from salvar_dados import salvarCsv

#------FUNCOES AUX-------
    
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

def cancelar(variavelInput:str, funcaoDeVolta, tipo:str='str'):
    if tipo == 'int' and variavelInput == 0:
        os.system('cls')
        print(f'{mensagemFormat('ACAO CANCELADA!! RETORNANDO...')}')
        sleep(1)
        return funcaoDeVolta()

    if not variavelInput:
        os.system('cls')
        print(f'{mensagemFormat('ACAO CANCELADA!! RETORNANDO...')}')
        sleep(1)

        return funcaoDeVolta()
    pass


#------/FUNCOES AUX-------

#------MENU PRINCIPAL-------

def menuPrincipal():

    while True:
        os.system('cls')
        try: 
            menu = int(input('''
    
    ╔═════╣MENU PRINCIPAL╠═════╗
    ║    1.MENU PRODUTOS       ║
    ║    2.MENU CLIENTES       ║
    ║    3.MENU FORNECEDORES   ║
    ║    4.MENU CATEGORIA      ║
    ║                          ║
    ║  0.SALVAR E SALVAR       ║             
    ╚══════════════════════════╝
                             
R:'''))
            match menu:
                case 1:
                    os.system('cls')
                    print(mensagemFormat('INDO PARA O MENU DE PRODUTOS...'))
                    sleep(1)
                    return menuProdutos()
                case 2:
                    os.system('cls')
                    print(mensagemFormat('INDO PARA O MENU DE CLIENTES...'))
                    sleep(1)
                    return menuClientes()
                case 3:
                    os.system('cls')
                    print(mensagemFormat('INDO PARA O MENU DE FORNECEDORES...'))
                    sleep(1)
                    return menuFornecedores()
                case 4:
                    os.system('cls')
                    print(mensagemFormat('INDO PARA O MENU DE CATEGORIA...'))
                    sleep(1)
                    return menuCategoria()
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
    ║    4.MOVIMENTACOES     ║
    ║    5.MOSTRAR ESTOQUE   ║ 
    ║                        ║
    ║ 0.VOLTAR               ║             
    ╚════════════════════════╝
    

R:'''))

            match menu:
                case 1:
                    
                    return cadastrarProduto()
                case 2:
                    
                    return editarProduto()
                case 3:
                    
                    return excluirItem() 
                case 4:
                    return movimentacoesItem()
                case 5:
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
                
def cadastrarProduto():
        if not dadosFornecedor["ID_FORNECEDOR"]:
            print(mensagemFormat('ANTES CADASTRE UM FORNECEDOR!!!!'))
            sleep(2.5)
            return cadastrarFornecedor()
    
        if not dadosCategoria["ID_CATEGORIA"]:
            print(mensagemFormat('ANTES CADASTRE UMA CATEGORIA!!!!'))
            sleep(2.5)
            return cadastrarCategoria()
        
        print(listarFornecedores())
        idFornecedor = int(input('QUAL O ID FORNECEDOR O PRODUTO PERTENCE(digite 0 para voltar): '))
        cancelar(idFornecedor,menuProdutos,'int')

        for linha in range(len(dadosFornecedor['ID_FORNECEDOR'])):
            if dadosFornecedor['ID_FORNECEDOR'][linha] == idFornecedor:
                dadosProduto['FORNECEDOR_PRODUTO'].append(dadosFornecedor['NOME_FORNECEDOR'][linha])
                break

        print(listarCategoria())
        idCategoria = int(input('\QUAL O ID DA CATEGORIA O PRODUTO PERTENCE(digite 0 para voltar): '))
        cancelar(idCategoria,menuProdutos,'int')
        
        for linha in range(len(dadosCategoria['ID_CATEGORIA'])):
            if dadosCategoria['ID_CATEGORIA'][linha] == idCategoria:
                dadosProduto['CATEGORIA_PRODUTO'].append(dadosCategoria['NOME_CATEGORIA'][linha])
                break
            
        while True:
            os.system('cls')

            
            print('═══╣CADASTRO DE ITEM╠═══')
            
            nomeProduto = str(input('\nNOME DO PRODUTO(enter para voltar): ')).upper()
            cancelar(nomeProduto,menuProdutos)
            if not nomeProduto:
                print(f"\n{mensagemFormat('NOME DO PRODUTO NAO PODE ESTAR EM BRANCO!!!')}")
                sleep(1)
            else:
                break
            
        while True:
            try:
                precoProduto = str(input('PRECO: ').replace(',','.'))
                precoProduto = float(precoProduto)
                break
            except ValueError:
                print(mensagemFormat('Apenas números!!'))
                sleep(0.5)

        if not dadosProduto['ID_PRODUTO']:
            dadosProduto['ID_PRODUTO'].append(1)
        else:
            dadosProduto['ID_PRODUTO'].append(dadosProduto["ID_PRODUTO"][len(dadosProduto["ID_PRODUTO"])-1]+1)        
 
        dadosProduto['NOME_PRODUTO'].append(nomeProduto)                
        dadosProduto['PRECO_PRODUTO'].append(precoProduto)      
        dadosProduto['QUANTIDADE_PRODUTO'].append(0)
   
        os.system('cls')
        salvarCsv('Produto')
        print(mensagemFormat('Item cadastrado!!'))

        sleep(1)
        menuProdutos()
      
def editarProduto():
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
            idProduto = int(input('Qual item deseja editar? (ID)(digite 0 para voltar): '))
            cancelar(idProduto,menuProdutos,'int')
            
        except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel
            print('APENAS NUMEROS!!')
            
        if idProduto not in dadosProduto['ID_PRODUTO']:
            print('OPÇÃO INVÁLIDA!!')
            continue
        
        break
    opcao = int(input('''
  ╔═══════════════╗
  ║  1.NOME       ║
  ║  2.PREÇO      ║ 
  ║               ║
  ║ 0.VOLTAR      ║
  ╚═══════════════╝
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
            return editarProduto()
        case _:
            print(mensagemFormat("OPÇÃO INVÁLIDA!"))   
            sleep(0.5)
            return editarProduto()

def excluirItem():
    while True:

        print(mostrarEstoque())
        
        try: #try vai rodar o bloco dentro dele, caso der algum erro o except é chamado
            excluir = (input('\nQual item deseja exlcuir do seu estoque? [ID](enter para voltar):'))
            cancelar(excluir, menuProdutos)
            # if excluir == "":
            #     return menuProdutos()
            
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
        
def movimentacoesItem():
    os.system('cls')
    
    print('═══╣MOVIMENTACAO DE ITEM╠═══')
    if not dadosProduto['ID_PRODUTO']:
        print('ESTOQUE VAZIO!!')
        sleep(1)
        menuProdutos()

    while True:
        print(mostrarEstoque())
        try:
            idProduto = int(input('\nQUAL ITEM DESEJA FAZER UMA MOVIMENTACAO? [ID](DITIGE 0 PARA VOLTAR): '))
            cancelar(idProduto,menuProdutos,'int')
            if idProduto not in dadosProduto['ID_PRODUTO']:
                print(mensagemFormat('OPÇÃO INVÁLIDA!!'))
                sleep(1.5)
                continue
            break
        except ValueError:
            print(mensagemFormat('APENAS NUMEROS!!'))
            sleep(1.5)
            
            

    while True:
        try:
            opcaoMov = int(input(f'''
FAZER QUE TIPO DE MOVIMENTACAO NO ITEM ID[{idProduto}]:
    ╔═════════════╗
    ║  1.ENTRADA  ║
    ║  2.SAIDA    ║
    ║             ║
    ║ 0.VOLTAR    ║             
    ╚═════════════╝
R: '''))
            cancelar(opcaoMov,menuProdutos,'int')
            break
        except ValueError:
            print(mensagemFormat('APENAS NUMEROS!!'))
            sleep(1.5)


    while True:
        
        try:    
            if opcaoMov == 1:
                quantidadeItem = int(input(f'\nENTRADA ID[{idProduto}] DE: '))
                if quantidadeItem < 0:
                    print(mensagemFormat("ENTRADA NÃO PODE SER NEGATIVA!"))
                    sleep(1.5)
                    continue
                break
            elif opcaoMov == 2:
                quantidadeItem = int(input(f'\nSAIDA ID[{idProduto}] DE: '))
                if quantidadeItem > 0:
                    quantidadeItem = quantidadeItem * (-1)
                break

        except ValueError:
            print(mensagemFormat('APENAS NUMEROS!!'))
        
    for linha in range(len(dadosProduto['ID_PRODUTO'])):
        if dadosProduto['ID_PRODUTO'][linha] == idProduto:
            if dadosProduto['QUANTIDADE_PRODUTO'][linha] + quantidadeItem < 0:
                print(mensagemFormat(f'MOVIMENTACAO INVALIDA !! NAO É POSSIVEL QUE O ITEM ID[{idProduto}] FIQUE NEGATIVADO'))
                sleep(2)
                return movimentacoesItem()
            dadosProduto['QUANTIDADE_PRODUTO'][linha] += quantidadeItem
            break #sai do for
        
            
    salvarCsv('Produto')
    print(mensagemFormat('MOVIMENTACAO FEITA COM SUCESSO!!!'))
    sleep(0.5)
    menuProdutos()

def mostrarEstoque():

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

    '''
    ┴
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

#------MENU CATEGORIAS------ 

def menuCategoria():
    while True:
        os.system('cls')

        try:
            menu = int(input('''
    ╔══╣MENU DE CATEGORIA╠══╗
    ║      1.CRIAR          ║
    ║      2.EDITAR         ║
    ║      3.EXCLUIR        ║
    ║      4.LISTAR         ║
    ║                       ║
    ║   0.VOLTAR            ║
    ╚═══════════════════════╝
R:'''))

            match menu:
                case 1:
                    return cadastrarCategoria()
                case 2:
                    return editarCategoria()
                case 3:
                    return excluirCategoria() 
                case 4:
                    print(listarCategoria())
                    input(f'\n{mensagemFormat("PRESSIONE ENTER PARA SAIR")}')
                    
                    return menuCategoria()
                case 0:
                    
                    return menuPrincipal()
                case _:
                    print(mensagemFormat("OPÇÃO INVÁLIDA!"))   
                    sleep(1)
                    
                    return menuCategoria() 

        except ValueError: #valueerror verifica se o valor colocado esta de acordo com a tipificacao da variavel
            os.system('cls')
            print(mensagemFormat('APENAS NÚMEROS!!'))
            sleep(0.5)

def cadastrarCategoria(): 
    while True:
        os.system('cls')
        print('═══╣CADASTRO DE CATEGORIA╠═══\n') 
        nomeCateg = input('\nDEFINA O NOME DA CATEGORIA(enter para voltar):').upper()
        cancelar(nomeCateg,menuCategoria)
        if not dadosCategoria["ID_CATEGORIA"]:
            dadosCategoria["ID_CATEGORIA"].append(1)
        else:
            dadosCategoria["ID_CATEGORIA"].append(dadosCategoria["ID_CATEGORIA"][len(dadosCategoria["ID_CATEGORIA"])-1] +1 )

        dadosCategoria["NOME_CATEGORIA"].append(nomeCateg)
        break
    salvarCsv('Categoria')
    print('CATEGORIA CRIADA!!')
    sleep(1.5)

    return menuCategoria()

def editarCategoria():

    if not dadosCategoria["ID_CATEGORIA"]:
        print(mensagemFormat('ANTES CADASTRE UMA CATEGORIA!!!!'))
        sleep(2.5)
        return cadastrarCategoria()
    
    while True:
        os.system("cls")
        print(listarCategoria())
        try:
            idCateg = int(input("QUAL CATEGORIA VOCE DESEJA EDITAR? [ID](digite 0 para voltar):\n"))
            cancelar(idCateg,cadastrarCategoria,'int')
            if idCateg not in dadosCategoria["ID_CATEGORIA"]:
                print(mensagemFormat("OPÇÃO INVÁLIDA!!"))
                sleep(1.5)
            else:
                break
        except ValueError:
            print(mensagemFormat("APENAS NUMEROS!!"))
            
        
    for i in range(len(dadosCategoria["ID_CATEGORIA"])):
        if dadosCategoria["ID_CATEGORIA"][i] == idCateg:
            nome = input("NOVO NOME: ").upper()
            dadosCategoria["NOME_CATEGORIA"][i] = nome
            break
    os.system('cls')
    print(f"CATEGORIA EDITADA PARA: {nome}!!")
    sleep(1.5)
    salvarCsv("Categoria")

    return menuCategoria()
                    
def excluirCategoria():
    if not dadosCategoria["ID_CATEGORIA"]:
        print(mensagemFormat('ANTES CADASTRE UMA CATEGORIA!!!!'))
        sleep(2.5)
        return cadastrarCategoria()
    
    while True:
        os.system("cls")
        print(listarCategoria())
        try:
            idCateg = int(input("QUAL CATEGORIA VOCE DESEJA EXCLUIR? [ID](digite 0 para voltar):\n"))
            cancelar(idCateg,cadastrarCategoria,'int')
            break
        except ValueError:
            print(mensagemFormat("APENAS NUMEROS!!"))

    if idCateg not in dadosCategoria["ID_CATEGORIA"]:
        print(mensagemFormat("OPÇÃO INVÁLIDA!!"))
        sleep(1.5)
    else:   
        for i in range(len(dadosCategoria["ID_CATEGORIA"])):
            if dadosCategoria["ID_CATEGORIA"][i] == idCateg:
                print(f"CATEGORIA {dadosCategoria["NOME_CATEGORIA"][i]} REMOVIDO!!")
                dadosCategoria["ID_CATEGORIA"].pop(i)
                dadosCategoria["NOME_CATEGORIA"].pop(i)
                break

    salvarCsv('Categoria')
    print('CATEGORIA EXCLUIDA!!')
    sleep(1.5)

    return menuCategoria()

def listarCategoria():
    os.system('cls')
    if not dadosCategoria["ID_CATEGORIA"]:
        print(mensagemFormat('SEM CATEGORIAS!!'))
        sleep(1)
        return cadastrarCategoria()
        
    return listagem(dadosCategoria['ID_CATEGORIA'],dadosCategoria['NOME_CATEGORIA'] )    

#------/MENU CATEGORIAS------ 

#------MENU FORNECEDORES------ 
def menuFornecedores():
    while True:
        os.system('cls')
        try: #try vai rodar o bloco dentro dele, caso der algum erro o except é chamado
            menu = int(input('''
                             
    ╔═════╣MENU FORNECEDOR╠═════╗
    ║   1.CADASTRAR FORNECEDOR  ║
    ║   2.EDITAR FORNECEDOR     ║
    ║   3.EXCLUIR FORNECEDOR    ║
    ║   4.LISTAR FORNECEDOR     ║
    ║                           ║
    ║  0.SALVAR E SAIR          ║             
    ╚═══════════════════════════╝              
R:'''))

            match menu:
                case 1:
                    return cadastrarFornecedor()
                case 2:
                    return editarFornecedor()
                case 3:
                    return excluirFornecedor()
                case 4:
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

def cadastrarFornecedor():
    os.system('cls')
    print('═══╣CADASTRO DE FORNECEDOR╠═══\n')   
    nome = str(input('NOME DO FORNECEDOR (enter para voltar):\n')).upper()
    cancelar(nome,menuFornecedores)
    if not dadosFornecedor["ID_FORNECEDOR"]:
        dadosFornecedor["ID_FORNECEDOR"].append(1)
    else:
        dadosFornecedor['ID_FORNECEDOR'].append(dadosFornecedor["ID_FORNECEDOR"][len(dadosFornecedor["ID_FORNECEDOR"])-1] +1 )
    dadosFornecedor['NOME_FORNECEDOR'].append(nome)                                   

    os.system('cls')
    
    salvarCsv('Fornecedor')
    print(mensagemFormat('FORNECEDOR CADASTRADO!!'))
    sleep(1.5)
    
    return menuFornecedores()

def excluirFornecedor():
    if not dadosFornecedor["ID_FORNECEDOR"]:
        print(mensagemFormat('ANTES CADASTRE UM FORNECEDOR!!!!'))
        sleep(2.5)
        return cadastrarFornecedor()
    
    while True:
        os.system("cls")
        print(listarFornecedores())
        try:
            idForn = int(input("QUAL FORNECEDOR VOCE DESEJA EXCLUIR? [ID](digite 0 para voltar):\n"))
            cancelar(idForn,menuFornecedores,'int')
            break
        except ValueError:
            print(mensagemFormat("APENAS NUMEROS!!"))

    if idForn not in dadosFornecedor["ID_FORNECEDOR"]:
        print(mensagemFormat("OPÇÃO INVÁLIDA!!"))
        sleep(1.5)
    else:   
        for i in range(len(dadosFornecedor["ID_FORNECEDOR"])):
            if dadosFornecedor["ID_FORNECEDOR"][i] == idForn:
                print(f"FORNECEDOR '{dadosFornecedor["NOME_FORNECEDOR"][i]}' REMOVIDO!!")
                dadosFornecedor["ID_FORNECEDOR"].pop(i)
                dadosFornecedor["NOME_FORNECEDOR"].pop(i)
                break

    salvarCsv('Fornecedor')
    sleep(1.5)

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
        idFornecedor = int(input('Qual item deseja editar? [ID](digite 0 para voltar): '))
        cancelar(idFornecedor,menuFornecedores,'int')
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

def listarFornecedores():
    os.system('cls')
    if not dadosFornecedor["ID_FORNECEDOR"]:
        print('SEM FORNECEDORES CADASTRADOS!!')
        sleep(1)
        return cadastrarFornecedor()
    
    return listagem(dadosFornecedor['ID_FORNECEDOR'],dadosFornecedor['NOME_FORNECEDOR'] )

#------/MENU FORNECEDORES------ 

#------MENU CLIENTES------ 
def menuClientes():     

    while True:
        os.system('cls')

        try:
            menu = int(input('''
    ╔═╣MENU DE CLIENTES╠═╗
    ║    1.CADASTRAR     ║    
    ║    2.EDITAR        ║
    ║    3.EXCLUIR       ║
    ║    4.LISTAR        ║
    ║                    ║    
    ║    0. VOLTAR       ║
    ╚════════════════════╝
R:'''))
            
            match menu:
                case 1:
                    return cadastrarCliente()
                case 2:
                    return editarCliente()
                case 3:
                    return excluirCliente()
                case 4:
                    print(listarClientes())
                    sleep(0.5)
                    input(mensagemFormat('PRESSIONE ENTER PARA SAIR'))
                    return menuClientes()
                case 0:
                    return menuPrincipal()
                case _:
                    print(mensagemFormat("OPÇÃO INVÁLIDA!")) 
                    sleep(1.5)   
                    continue

        except ValueError: 
            
            os.system('cls')
            print('APENAS NÚMEROS!!')
            sleep(0.5)
            continue

def cadastrarCliente(): 
    while True:
        os.system('cls')
        print('═══╣CADASTRO DE CLIENTE╠═══\n')   
        nome = str(input('NOME CLIENTE DO CLIENTE(enter para voltar): ')).upper()
        cancelar(nome,menuClientes)

        if not dadosCliente["ID_CLIENTE"]:
            dadosCliente["ID_CLIENTE"].append(1)
        else:
            dadosCliente["ID_CLIENTE"].append(dadosCliente["ID_CLIENTE"][len(dadosCliente["ID_CLIENTE"])-1] +1 )

        dadosCliente["NOME_CLIENTE"].append(nome)
        break

    os.system('cls')

    salvarCsv('Cliente')
    print('CLIENTE CADASTRADO!!')
    sleep(0.5)
    return menuClientes()

def excluirCliente():
    if not dadosCliente["ID_CLIENTE"]:
        print(mensagemFormat('ANTES CADASTRE UM CLIENTE!!!!'))
        sleep(2.5)
        return cadastrarCliente()
    
    while True:
        os.system("cls")
        print(listarClientes())
        try:
            idClient = int(input("QUAL CLIENTE VOCE DESEJA EXCLUIR? [ID](digite 0 para voltar):\n"))
            cancelar(idClient,cadastrarCliente,'int')
            break
        except ValueError:
            print(mensagemFormat("APENAS NUMEROS!!"))

    if idClient not in dadosCliente["ID_CLIENTE"]:
        print(mensagemFormat("OPÇÃO INVÁLIDA!!"))
        sleep(1.5)
    else:   
        for i in range(len(dadosCliente["ID_CLIENTE"])):
            if dadosCliente["ID_CLIENTE"][i] == idClient:
                print(f"CLIENTE '{dadosCliente["NOME_CLIENTE"][i]}' REMOVIDO!!")
                dadosCliente["ID_CLIENTE"].pop(i)
                dadosCliente["NOME_CLIENTE"].pop(i)
                break

    salvarCsv('Cliente')
    sleep(1.5)

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
        idCliente = int(input('\nQual item deseja editar? [ID](digite 0 para voltar):'))
        cancelar(idCliente,menuClientes)

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
