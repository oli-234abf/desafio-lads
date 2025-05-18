import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


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
print(df_vendas.head())

#ultimas linhas do dataframe:
print('últimas 5 linhas data frame: ')
print(df_vendas.tail(5))

#verificando o formato do DataFrame
print(f"Formato do data frame: {df_vendas.shape}")
print(f"Número de linhas: {df_vendas.shape[0]}")
print(f"Número de colunas: {df_vendas.shape[1]}")
print("Nomes das colunas:")
print(df_vendas.columns.tolist())

#Para obter informações detalhadas em estaticas do data frame:

#Verificando informaçõs do data frame com info()

print("Informações do data frame: ")
print(df_vendas.info())

#Estatisticas descritivas com describe:
print("Estatísticas descritivas:")
print(df_vendas.describe())

#Contagem de valores númericos com nunique()
print("Contagem numérica:")
print(df_vendas.nunique())

#Verificação de valores unicos e nulos:

#Valores únicos em uma coluna categoria:
print("Categorias únicas:")
print(df_vendas['regiao'].unique())

#Contando ocorrencias de cada valor
print("Contagem a cada categoria:")
print(df_vendas['categoria'].value_counts())
print("Valores nulos em cada coluna:")
print(df_vendas.isnull().sum())

#Exercicio:

#1_Usar head() para mostrar as 10 primeiras linhas do data frame

print("1O primeiras linhas do data frame:")
print(df_vendas.head(10))

#2_Use shape para verificar quant linhas e quantas colunas tem no data frame:

print("Quantidade de linhas e colunas do data frame")
print(f"Número de linhas: {df_vendas.shape[0]}")
print(f"Número de colunas: {df_vendas.shape[1]}")

#3_Use o metodo unique() para listar todas as regiões do data frame:

print("Todas as regiões no data frame:")
print(df_vendas['regiao'].unique())

#4_Use o metodo value_counts() para contar qantas vendas existem por canal venda:

print("Quantas vendas existem por canal:")
print(df_vendas['canal_venda'].value_counts())

#5_Use o mtodo describe() para obter estatisica da coluna 'valor_venda':

print("Estatistica da coluna 'valor_venda:")
print(df_vendas['valor_venda'].describe())

#Seleção de filtragem de dados:

#Maneiras de selecionar colunas em um data frame:

#Coluna unica (retorna uma serie)

valores_venda = df_vendas['valor_venda']
print("Cinco primeiros valores da coluna 'valor_venda':")
print(valores_venda.head(5))
print(f"tipos de dados: {type(valores_venda)}")

#Multiplas colunas retorna um data frame:
selecao = df_vendas[['produto','valor_venda','quantidade']]

print("cinco primeiras linhas das coluna selecionadas:")
print(selecao.head(5))
print(f"tipos de dados: {type(selecao)}")

#Condicinais:

#Básica:
vendas_altas = df_vendas[df_vendas['valor_venda'] > 1000]
print(f"Número de vendas com valores acima de R$1000,00: {len(vendas_altas)}")

print("Cinco primeiras vendas com valores acima de R$1000,00:")
print(vendas_altas.head(5))

#Múltiplas condições com & e |:

#&:
vendas_eletronicos_sul = df_vendas[(df_vendas['categoria'] == 'Eletrônicos') & 
                                   (df_vendas['regiao'] == 'Sul')]
print(f"Número de vendas de Eletrônicos na região Sul: {len(vendas_eletronicos_sul)}")

print("Primeiras 5 vendas de Eletrônicos na região Sul:")
print(vendas_eletronicos_sul.head(5))

#|:
# Vendas muito altas (>3000) ou com avaliação máxima (5)
vendas_premium = df_vendas[(df_vendas['valor_venda'] > 3000) | 
                          (df_vendas['avaliacao'] == 5)]

print(f"Número de vendas premium: {len(vendas_premium)}")

print("Primeiras 5 vendas premium:")
print(vendas_premium.head(5))

#isin() e between()

# Usando isin() para filtrar com uma lista de valores

# Vendas nas regiões Sul e Sudeste
regioes_sul_sudeste = ['Sul', 'Sudeste']
vendas_sul_sudeste = df_vendas[df_vendas['regiao'].isin(regioes_sul_sudeste)]

print(f"Número de vendas nas regiões Sul e Sudeste: {len(vendas_sul_sudeste)}")

print("Primeiras 5 vendas nas regiões Sul e Sudeste:")
print(vendas_sul_sudeste.head(5))

# Usando between() para filtrar valores em um intervalo

# Vendas com valor entre 1000 e 2000
vendas_1000_2000 = df_vendas[df_vendas['valor_venda'].between(1000, 2000)]

print(f"Número de vendas entre R$1000 e R$2000: {len(vendas_1000_2000)}")

print("Primeiras 5 vendas entre R$1000 e R$2000:")
print(vendas_1000_2000.head(5))

#Exercicio 2:

#1_Selecionar apenas 'data','produto' e 'valor_venda' do data frame:
selecao_produto = df_vendas[['produto','valor_venda','quantidade']]

print("Seleção das colunas 'produto','valor_venda' e 'quantidade':")
print(selecao_produto)
print(f"tipos de dados: {type(selecao_produto)}")

#2_Filtre o data frame para mostrar apenas as vendas do canal 'online':

selecao_online = df_vendas[df_vendas['canal_venda'] == 'Online']
print(f"Número de vendas do canal 'online': {len(selecao_online)}")

print("Vendas do canal online:")
print(selecao_online)
#quando identificar string as letras tem que estarc como no data frame(se estiver maiuscula tem que ser maiuscula)

# 3_Filtre para mostra 'roupas' acima de 500:

selecao_roupas = df_vendas[(df_vendas ['categoria'] == 'Roupas') &
                           (df_vendas['valor_venda'] > 500)]
print(f"Qunatidade de roupas vendidas acima de R$500,00: {len(selecao_roupas)}")


print("Venda de roupas acima de R$500,00: ")
print(selecao_roupas)

#use o metodo isin() vendas do produtos 'smatphones' e 'laptop'

smartphone_laptop = ['Smartphone', 'Laptop']
smartphone_laptop = df_vendas[df_vendas['produto'].isin(smartphone_laptop)]

print(f"Número de vendas nas regiões Sul e Sudeste: {len(smartphone_laptop)}")

print("Vendas de Smartphone e Laptop:")
print(smartphone_laptop)

#5_between( ) para encontrar vendas com quatidades entre 3 e 5 unidades:

vendas_3_5 = df_vendas[df_vendas['quantidade'].between(3, 5)]

print(f"Número de vendas entre 3 e 5 unidades: {len(vendas_3_5)}")

print("Vendas entre 3 e 5 unidades:")
print(vendas_3_5)

# # Ordenando por uma coluna em ordem crescente (padrão)
# df_ordenado_crescente = df_vendas.sort_values('valor_venda')

# print("5 vendas com os menores valores:")
# df_ordenado_crescente.head()

# # Ordenando por uma coluna em ordem decrescente
# df_ordenado_decrescente = df_vendas.sort_values('valor_venda', ascending=False)

# print("5 vendas com os maiores valores:")
# df_ordenado_decrescente.head()

# # Ordenando por múltiplas colunas

# # Primeiro por categoria (A-Z) e depois por valor_venda (maior para menor)
# df_ordenado_multi = df_vendas.sort_values(['categoria', 'valor_venda'], 
#                                          ascending=[True, False])

# print("Ordenação por categoria e depois por valor (decrescente):")
# df_ordenado_multi.head(10)

#3

# avaliacao 10 primeiras linhas

df_aval = df_vendas.sort_values('avaliacao')
print("10 primeiras avaliações de vendas:")
print(df_aval.head(10))

#regiao a- z valor venda maior menor

df_ordenado_regiao = df_vendas.sort_values(['regiao','valor_venda'], 
                                            ascending=[True, False])

print("Ordenação por região e depois por valo de venda(decrescente):")
print(df_ordenado_regiao.head(10))

df_produto = df_vendas.set_index('produto')

print("DataFrame com 'produto' como índice:")
print(df_produto.head(5))
