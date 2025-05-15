# ESTE ARQUIVO É SOMENTE PARA PREENCHER
# O BANCO DE DADOS PARA TESTES

import random

produtos = [
    ("TECLADO MECANICO", "PERIFERICOS"), ("MOUSE GAMER", "PERIFERICOS"), ("MONITOR FULL HD", "MONITORES"),
    ("CADEIRA ERGONOMICA", "MOVEIS"), ("HEADSET WIRELESS", "AUDIO"), ("PLACA DE VIDEO", "HARDWARE"),
    ("NOTEBOOK GAMER", "COMPUTADORES"), ("SSD 1TB", "ARMAZENAMENTO"), ("MEMORIA RAM 16GB", "HARDWARE"),
    ("FONTE 750W", "HARDWARE"), ("GABINETE ATX", "HARDWARE"), ("COOLER PARA CPU", "HARDWARE"),
    ("MOUSEPAD GAMER", "PERIFERICOS"), ("WEBCAM FULL HD", "PERIFERICOS"), ("MICROFONE CONDENSADOR", "AUDIO"),
    ("PLACA-MAE B550", "HARDWARE"), ("PROCESSADOR RYZEN 7", "HARDWARE"), ("PROCESSADOR I7", "HARDWARE"),
    ("PLACA DE CAPTURA", "HARDWARE"), ("MONITOR 144HZ", "MONITORES"), ("HUB USB 3.0", "ACESSORIOS"),
    ("ROTEADOR WI-FI 6", "REDES"), ("CABO HDMI 2M", "ACESSORIOS"), ("CABO DISPLAYPORT", "ACESSORIOS"),
    ("CONTROLE BLUETOOTH", "GAMES"), ("CONTROLE PS5", "GAMES"), ("BATERIA EXTERNA 20000MAH", "ENERGIA"),
    ("CARREGADOR USB-C", "ENERGIA"), ("SMARTWATCH", "WEARABLES"), ("CADEIRA GAMER", "MOVEIS"),
    ("VOLANTE PARA PC", "GAMES"), ("MONITOR ULTRAWIDE", "MONITORES"), ("TECLADO BLUETOOTH", "PERIFERICOS"),
    ("SSD NVME 2TB", "ARMAZENAMENTO"), ("HD EXTERNO 4TB", "ARMAZENAMENTO"),
    ("FONE DE OUVIDO BLUETOOTH", "AUDIO"), ("CADEIRA ESCRITORIO", "MOVEIS"), ("MOUSE ERGONOMICO", "PERIFERICOS"),
    ("NOTEBOOK ULTRAFINO", "COMPUTADORES"), ("PLACA DE SOM USB", "AUDIO")
]

fornecedores = ["LOGITECH", "RAZER", "SAMSUNG", "DXRACER", "HYPERX", "NVIDIA", "DELL", "KINGSTON",
                "CORSAIR", "EVGA", "NZXT", "NOCTUA", "STEELSERIES", "FIFINE", "ASUS", "AMD", "INTEL",
                "ELGATO", "AOC", "TP-LINK", "FISCHER", "XBOX", "SONY", "ANKER", "XIAOMI",
                "THUNDERX3", "LG", "MICROSOFT", "CRUCIAL", "SEAGATE", "JBL", "FLEXFORM", "LENOVO",
                "BEHRINGER"]


CLIENTES = [
    "JOAO SILVA", "MARIA OLIVEIRA", "CARLOS SANTOS", "ANA SOUZA", "PEDRO LIMA",
    "FERNANDA COSTA", "LUCAS ALMEIDA", "PAULO RIBEIRO", "MARCOS MARTINS", "PATRICIA MELO",
    "GABRIELA ROCHA", "RICARDO NUNES", "CAMILA FERREIRA", "ANDRE GOMES", "JULIA MENDES",
    "FELIPE TEIXEIRA", "LETICIA BARBOSA", "GUSTAVO PINTO", "RAFAELA CAMPOS", "DIEGO CARDOSO"
]

FORNECEDORES = [
    "LOGITECH", "RAZER", "SAMSUNG", "DXRACER", "HYPERX", "NVIDIA", "DELL", "KINGSTON",
    "CORSAIR", "EVGA", "NZXT", "NOCTUA", "STEELSERIES", "FIFINE", "ASUS", "AMD", "INTEL",
    "ELGATO", "AOC", "TP-LINK", "FISCHER", "XBOX", "SONY", "ANKER", "XIAOMI",
    "THUNDERX3", "LG", "MICROSOFT", "CRUCIAL", "SEAGATE", "JBL", "FLEXFORM", "LENOVO",
    "BEHRINGER"
]

CATEGORIAS = [
    "PERIFERICOS", "MONITORES", "MOVEIS", "COMPUTADORES", "HARDWARE",
    "ARMAZENAMENTO", "ACESSORIOS", "REDES", "IMPRESSAO", "AUDIO",
    "VIDEO", "DISPOSITIVOS MOVEIS", "WEARABLES", "ENERGIA", "SEGURANCA",
    "GAMING", "SMART HOME", "ILUMINACAO", "FERRAMENTAS", "ESCRITORIO"
]


with open("./banco_de_dados/produtos.csv", "w", encoding="utf-8") as f:
    for i in range(100):
        produto, categoria = random.choice(produtos)
        preco = round(random.uniform(50, 5000), 2)
        quantidade = random.randint(1, 50)
        fornecedor = random.choice(fornecedores)
        f.write(f"{i},{produto.replace(' ', '')},{preco},{quantidade},{categoria},{fornecedor}\n")

# Gerar clientes
with open("./banco_de_dados/clientes.csv", "w", encoding="utf-8") as f:
    for i in range(len(CLIENTES)):
        f.write(f"{i},{random.choice(CLIENTES)}\n")

# Gerar fornecedores
with open("./banco_de_dados/fornecedores.csv", "w", encoding="utf-8") as f:
    for i in range(len(FORNECEDORES)):
        f.write(f"{i},{random.choice(FORNECEDORES)}\n")

# Gerar categorias
with open("./banco_de_dados/categorias.csv", "w", encoding="utf-8") as f:
    for i in range(len(CATEGORIAS)):
        f.write(f"{i},{random.choice(CATEGORIAS)}\n")

print("Arquivos :\n'clientes.csv'\n'fornecedores.csv'\n'categorias.csv'\n'produtos.csv'\npreenchidos com sucesso!")
