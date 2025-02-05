from funcoes import menuPrincipal
from salvar_dados import obterCsv

obterCsv('Produtos')
obterCsv('Clientes')
obterCsv('Fornecedores')
obterCsv('Categorias')

try:
    menuPrincipal()
except KeyboardInterrupt:
    print('\n\nFechando codigo...\n\n')
    
