import pandas as pd

# Carregar os dados
df = pd.read_csv("data/data.csv", encoding="latin1")

# Verificar informações gerais sobre os dados
print("📌 Informações gerais do dataset:")
print(df.info())

# Verificar a quantidade de valores nulos por coluna
print("\n🔍 Valores nulos por coluna:")
print(df.isnull().sum())

# Verificar a quantidade de registros duplicados
print("\n🔍 Registros duplicados no dataset:")
print(df.duplicated().sum())


print(df.head())  # Verifica se os dados foram carregados corretamente
print(df.info())  # Confirma se a coluna Revenue existe




