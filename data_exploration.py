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

# Remover registros duplicados
df_cleaned = df.drop_duplicates()

# Verificar novamente se ainda existem duplicatas
print("\n✅ Registros duplicados após a limpeza:")
print(df_cleaned.duplicated().sum())

# Salvar o novo dataset limpo
df_cleaned.to_csv("data/dataecommerce_cleaned.csv", index=False)

print("\n💾 Dataset limpo salvo como 'dataecommerce_cleaned.csv'")

# Substituir valores nulos na coluna 'Description' por "Unknown"
df_cleaned.loc[:, 'Description'] = df_cleaned['Description'].fillna("Unknown")


# Remover linhas onde 'CustomerID' está vazio
df_cleaned = df_cleaned.dropna(subset=['CustomerID'])

# Converter 'CustomerID' para inteiro (pois antes tinha NaN)
df_cleaned['CustomerID'] = df_cleaned['CustomerID'].astype(int)

# Verificar novamente os valores nulos
print("\n🔍 Valores nulos após tratamento:")
print(df_cleaned.isnull().sum())

# Salvar o dataset limpo
df_cleaned.to_csv("data/dataecommerce_cleaned.csv", index=False)
print("\n💾 Dataset atualizado salvo como 'dataecommerce_cleaned.csv'")




