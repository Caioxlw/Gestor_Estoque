def limpar_csv(csv):
    with open(csv, 'w'):
        print(f'Arquivo {csv} clear')

arquivos = ["banco_de_dados/produtos.csv", "banco_de_dados/categorias.csv", "banco_de_dados/fornecedores.csv", "banco_de_dados/clientes.csv"]

for arquivo in arquivos:
    limpar_csv(arquivo)
