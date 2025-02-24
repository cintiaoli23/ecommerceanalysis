import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset limpo
df = pd.read_csv("data/dataecommerce_cleaned.csv")

# Converter InvoiceDate para datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Criar uma coluna de faturamento
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# Gráfico 1: Faturamento por País
plt.figure(figsize=(12,6))
revenue_by_country = df.groupby('Country')['Revenue'].sum().sort_values(ascending=False)[:10]
sns.barplot(x=revenue_by_country.values, y=revenue_by_country.index, palette="viridis")
plt.xlabel("Faturamento (£)")
plt.ylabel("País")
plt.title("Faturamento por País")
plt.show()

# Gráfico 2: Top 10 Produtos Mais Vendidos
plt.figure(figsize=(12,6))
top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False)[:10]
sns.barplot(x=top_products.values, y=top_products.index, palette="coolwarm")
plt.xlabel("Quantidade Vendida")
plt.ylabel("Produto")
plt.title("Top 10 Produtos Mais Vendidos")
plt.subplots_adjust(left=0.3)
plt.show()

# Gráfico 3: Top 10 Produtos Mais Rentáveis
plt.figure(figsize=(10,6))
top_revenue_products = df.groupby('Description')['Revenue'].sum().sort_values(ascending=False)[:10]
sns.barplot(x=top_revenue_products.values, y=top_revenue_products.index, palette="magma")
plt.xlabel("Faturamento (£)")
plt.ylabel("Produto")
plt.title("Top 10 Produtos Mais Rentáveis")
plt.subplots_adjust(left=0.3)
plt.show()

# Gráfico 4: Faturamento ao Longo do Tempo
plt.figure(figsize=(12,6))
revenue_by_date = df.groupby(df['InvoiceDate'].dt.to_period("M"))['Revenue'].sum()
revenue_by_date.plot(kind='line', marker='o', color='b')
plt.xlabel("Data")
plt.ylabel("Faturamento (£)")
plt.title("Faturamento ao Longo do Tempo")
plt.xticks(rotation=45)
plt.grid()
plt.show()