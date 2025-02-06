from funcoes import menuPrincipal,mensagemFormat
from salvar_dados import obterCsv
import os
from time import sleep

obterCsv('Produtos')
obterCsv('Clientes')
obterCsv('Fornecedores')
obterCsv('Categorias')

carregar = [' ','.','..','...']

os.system('cls')
input('''
    ╔═════╣GESTOR DE ESTOQUE╠═════╗
    ║    ─ALUNOS:                 ║
    ║      1.CAIO VINICIUS        ║
    ║      2.RUAN HENRIQUE        ║
    ║      3.PEDRO XAVIER         ║
    ║                             ║
    ║  -ENTER PARA CONTINUAR      ║             
    ╚═════════════════════════════╝
''')
for i in range(2):
    for i in carregar:
        os.system('cls')
        print(mensagemFormat(f'ENTRANDO NO GESTOR DE ESTOQUE {i}'))
        sleep(0.3)
try:
    menuPrincipal()
except KeyboardInterrupt:
    print(mensagemFormat('FECHANDO CODIGO...'))
    
