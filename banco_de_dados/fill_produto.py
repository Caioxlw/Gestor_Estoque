import random

produtos = [
    "Teclado Mecanico", "Mouse Gamer", "Monitor Full HD", "Cadeira Ergonomica",
    "Headset Wireless", "Placa de Video", "Notebook Gamer", "SSD 1TB",
    "Memoria RAM 16GB", "Fonte 750W", "Gabinete ATX", "Cooler para CPU",
    "Mousepad Gamer", "Webcam Full HD", "Microfone Condensador",
    "Placa-Mae B550", "Processador Ryzen 7", "Processador i7",
    "Placa de Captura", "Monitor 144Hz", "Hub USB 3.0", "Roteador Wi-Fi 6",
    "Cabo HDMI 2m", "Cabo DisplayPort", "Controle Bluetooth",
    "Controle PS5", "Bateria Externa 20000mAh", "Carregador USB-C",
    "Smartwatch", "Cadeira Gamer", "Volante para PC", "Monitor Ultrawide",
    "Teclado Bluetooth", "SSD NVMe 2TB", "HD Externo 4TB",
    "Fone de Ouvido Bluetooth", "Cadeira Escritorio", "Mouse Ergonomico",
    "Notebook Ultrafino", "Placa de Som USB"
]

fornecedores = ["Logitech", "Razer", "Samsung", "DXRacer", "HyperX", "NVIDIA", "Dell", "Kingston",
                "Corsair", "EVGA", "NZXT", "Noctua", "SteelSeries", "Fifine", "ASUS", "AMD", "Intel",
                "Elgato", "AOC", "TP-Link", "Asus", "Fischer", "Xbox", "Sony", "Anker", "Xiaomi",
                "ThunderX3", "LG", "Microsoft", "Crucial", "Seagate", "JBL", "Flexform", "Lenovo",
                "Behringer"]

with open("produtos.csv", "w", encoding="utf-8") as f:
    for i in range(0, 100):
        nome = random.choice(produtos).replace(" ", "")
        preco = round(random.uniform(50, 5000), 2)
        quantidade = random.randint(1, 50)
        fornecedor = random.choice(fornecedores)
        f.write(f"{i},{nome},{preco},{quantidade},{fornecedor}\n")

print("Arquivo 'produtos.csv' adicionado com sucesso!")  
