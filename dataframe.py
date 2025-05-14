import pandas as pd
import numpy as np


# Criando um dataset de exemplo
np.random.seed(42)  # Para garantir reprodutibilidade

# Criando dados de exemplo
datas = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
categorias = ['Eletrônicos', 'Roupas', 'Alimentos', 'Casa', 'Beleza']
produtos = {
    'Eletrônicos': ['Smartphone', 'Laptop', 'Tablet', 'Fones de ouvido', 'Smart TV'],
    'Roupas': ['Camiseta', 'Calça', 'Vestido', 'Sapato', 'Jaqueta'],
    'Alimentos': ['Arroz', 'Feijão', 'Óleo', 'Açúcar', 'Café'],
    'Casa': ['Sofá', 'Mesa', 'Cadeira', 'Cama', 'Armário'],
    'Beleza': ['Shampoo', 'Condicionador', 'Sabonete', 'Perfume', 'Hidratante']
}
regioes = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']
estados = {
    'Norte': ['AM', 'PA', 'RO', 'RR', 'AC'],
    'Nordeste': ['BA', 'PE', 'CE', 'MA', 'PB'],
    'Centro-Oeste': ['DF', 'GO', 'MT', 'MS'],
    'Sudeste': ['SP', 'RJ', 'MG', 'ES'],
    'Sul': ['PR', 'SC', 'RS']
}
canais = ['Online', 'Loja Física', 'Aplicativo', 'Telefone']

# Gerando 1000 registros aleatórios
n_registros = 1000
data_vendas = []

for _ in range(n_registros):
    data = np.random.choice(datas)
    categoria = np.random.choice(categorias)
    produto = np.random.choice(produtos[categoria])
    regiao = np.random.choice(regioes)
    estado = np.random.choice(estados[regiao])
    canal = np.random.choice(canais)
    valor = round(np.random.uniform(10, 5000), 2)  # Valor entre R$10 e R$5000
    quantidade = np.random.randint(1, 10)  # Entre 1 e 9 itens
    avaliacao = np.random.randint(1, 6)  # Avaliação de 1 a 5 estrelas
    
    data_vendas.append({
        'data': data,
        'categoria': categoria,
        'produto': produto,
        'regiao': regiao,
        'estado': estado,
        'canal_venda': canal,
        'valor_venda': valor,
        'quantidade': quantidade,
        'avaliacao': avaliacao
    })

# Criando o DataFrame
df_vendas = pd.DataFrame(data_vendas)
df_vendas['data'] = df_vendas['data'].astype('object')

# Salvando como CSV para uso futuro
df_vendas.to_csv('dados_vendas.csv', index=False)

# Visualizando as primeiras linhas
df_vendas.head()