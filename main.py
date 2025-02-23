import pandas as pd

df = pd.read_csv("data/data.csv", encoding="latin1")  # ou "ISO-8859-1"
print(df.head())  # Para testar se o carregamento funcionou

print(df.info())  # Ver estrutura e tipos de dados
print(df.describe())  # Estatísticas gerais das colunas numéricas
print(df.isnull().sum())  # Verificar valores nulos



