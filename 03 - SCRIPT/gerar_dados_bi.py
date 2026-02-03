import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import getpass


user = getpass.getuser()
np.random.seed(100)

NUM_CLIENTES = 3000
NUM_VENDAS = 20000

DATA_INICIO = datetime(2020, 1, 1)
DATA_FIM = datetime(2025, 12, 31)

# =====================================================
# BASES FICTÍCIAS
# =====================================================
NOMES_PESSOA = [
    "Ana", "Carlos", "João", "Mariana", "Pedro", "Lucas", "Fernanda",
    "Bruno", "Rafael", "Camila", "Juliana", "Renata", "Paulo", "Rodrigo",
    "Eduardo", "Felipe", "Gabriela", "Patrícia", "Daniel", "Beatriz"
]

SOBRENOMES = [
    "Silva", "Santos", "Oliveira", "Pereira", "Costa", "Rodrigues",
    "Almeida", "Nascimento", "Lima", "Araujo", "Ribeiro", "Martins"
]

EMPRESAS = [
    "Tech", "Solutions", "Comercial", "Distribuidora", "Indústria",
    "Serviços", "Logística", "Digital", "Holding", "Group"
]

REGIOES = ["Norte", "Sul", "Leste", "Oeste", "Centro"]

# =====================================================
# CATÁLOGO DE PRODUTOS
# =====================================================
CATEGORIAS = {
    "Eletrônicos": [
        "Smart TV Samsung 55'' 4K",
        "Smart TV LG 50'' UHD",
        "Soundbar JBL 2.1",
        "Home Theater Sony 5.1",
        "TV Box Xiaomi Mi S",
        "Projetor Epson Full HD",
        "Console PlayStation 5",
        "Console Xbox Series X"
    ],
    "Informática": [
        "Notebook Dell Inspiron i7",
        "Notebook Lenovo ThinkPad i5",
        "Mouse Logitech MX Master",
        "Teclado Mecânico Redragon",
        "Monitor LG 27'' IPS",
        "Impressora HP LaserJet",
        "SSD Kingston 1TB NVMe",
        "Roteador TP-Link Archer AX"
    ],
    "Eletrodomésticos": [
        "Geladeira Brastemp Frost Free",
        "Geladeira Electrolux Duplex",
        "Fogão Consul 5 Bocas",
        "Micro-ondas Panasonic 34L",
        "Lava e Seca Samsung 11kg",
        "Máquina de Lavar LG 12kg",
        "Freezer Vertical Consul"
    ],
    "Móveis": [
        "Sofá Retrátil 3 Lugares",
        "Mesa de Jantar 6 Lugares",
        "Cadeira Escritório Presidente",
        "Guarda-Roupa Casal 6 Portas",
        "Rack para TV até 65''",
        "Cama Box Queen Ortobom"
    ]
}

# =====================================================
# DIM CLIENTES
# =====================================================
def gerar_clientes(qtd):
    clientes = []

    for i in range(1, qtd + 1):
        tipo = np.random.choice(["PF", "PJ"], p=[0.7, 0.3])

        if tipo == "PF":
            nome = f"{np.random.choice(NOMES_PESSOA)} {np.random.choice(SOBRENOMES)}"
        else:
            nome = f"{np.random.choice(SOBRENOMES)} {np.random.choice(EMPRESAS)} LTDA"

        clientes.append({
            "ID_Cliente": i,
            "Nome_Cliente": nome,
            "Tipo_Cliente": tipo,
            "Regiao": np.random.choice(REGIOES)
        })

    return pd.DataFrame(clientes)

# =====================================================
# DIM PRODUTOS
# =====================================================
def gerar_produtos():
    produtos = []
    id_produto = 1

    for categoria, lista_produtos in CATEGORIAS.items():
        for nome in lista_produtos:
            preco = round(np.random.uniform(300, 8000), 2)
            custo = round(preco * np.random.uniform(0.55, 0.7), 2)

            produtos.append({
                "ID_Produto": id_produto,
                "Produto": nome,
                "Categoria": categoria,
                "Preco_Unitario": preco,
                "Custo_Unitario": custo
            })

            id_produto += 1

    return pd.DataFrame(produtos)

# =====================================================
# FATO VENDAS
# =====================================================
def gerar_vendas(qtd, df_clientes, df_produtos):
    datas = [
        DATA_INICIO + timedelta(days=np.random.randint(0, (DATA_FIM - DATA_INICIO).days))
        for _ in range(qtd)
    ]

    vendas = {
        "ID_Venda": range(1, qtd + 1),
        "Data": datas,
        "ID_Cliente": np.random.choice(df_clientes["ID_Cliente"], qtd),
        "ID_Produto": np.random.choice(df_produtos["ID_Produto"], qtd),
        "Quantidade": np.random.randint(1, 8, qtd),
        "Canal_Venda": np.random.choice(["Online", "Loja Física"], qtd, p=[0.6, 0.4])
    }

    df = pd.DataFrame(vendas)

    df = df.merge(df_produtos, on="ID_Produto", how="left")

    df["Valor_Total"] = df["Quantidade"] * df["Preco_Unitario"]
    df["Custo_Total"] = df["Quantidade"] * df["Custo_Unitario"]
    df["Lucro"] = df["Valor_Total"] - df["Custo_Total"]

    return df

# =====================================================
# FATO METAS (POR CATEGORIA)
# =====================================================
def gerar_metas():
    meses = pd.date_range(DATA_INICIO, DATA_FIM, freq="MS")
    metas = []

    for mes in meses:
        for categoria in CATEGORIAS.keys():
            metas.append({
                "Mes_Ano": mes,
                "Categoria": categoria,
                "Meta_Vendas": round(np.random.uniform(20000, 60000), 2)
            })

    return pd.DataFrame(metas)

df_clientes = gerar_clientes(NUM_CLIENTES)
df_produtos = gerar_produtos()
df_vendas = gerar_vendas(NUM_VENDAS, df_clientes, df_produtos)
df_metas = gerar_metas()

caminho_Dim = rf"C:\Users\{user}\OneDrive - TERRA TECNOLOGIA AGRICOLA\Documents\Projeto PowerBI\01 - DIMENSÕES"
caminho_Fato = rf"C:\Users\{user}\OneDrive - TERRA TECNOLOGIA AGRICOLA\Documents\Projeto PowerBI\02 - FATO"

df_clientes.to_csv(f"{caminho_Dim}\\Dim_Clientes.csv", index=False, encoding="utf-8-sig")
df_produtos.to_csv(f"{caminho_Dim}\\Dim_Produtos.csv", index=False, encoding="utf-8-sig")
df_vendas.to_csv(f"{caminho_Fato}\\Fato_Vendas.csv", index=False, encoding="utf-8-sig")
df_metas.to_csv(f"{caminho_Fato}\\Fato_Metas.csv", index=False, encoding="utf-8-sig")

print("✅ Dados gerados com sucesso!")
print(f"Clientes: {len(df_clientes)}")
print(f"Produtos: {len(df_produtos)}")
print(f"Vendas: {len(df_vendas)}")
print(f"Metas: {len(df_metas)}")
