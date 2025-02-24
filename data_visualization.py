import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset limpo
df = pd.read_csv("data/dataecommerce_cleaned.csv")

# Definir estilo dos gráficos
sns.set_style("whitegrid")

# 📌 1️⃣ Distribuição de Preços dos Produtos
plt.figure(figsize=(10, 5))
sns.histplot(df["UnitPrice"], bins=50, kde=True)
plt.xlim(0, df["UnitPrice"].quantile(0.95))  # Limita outliers
plt.xlabel("Preço Unitário")
plt.ylabel("Frequência")
plt.title("Distribuição de Preços dos Produtos")
plt.subplots_adjust(left=0.3)
plt.show()

# 📌 2️⃣ Top 10 Produtos Mais Vendidos
top_products = df["Description"].value_counts().head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=top_products.values, y=top_products.index, palette="viridis")
plt.xlabel("Quantidade Vendida")
plt.ylabel("Produto")
plt.title("Top 10 Produtos Mais Vendidos")
plt.subplots_adjust(left=0.3)
plt.show()

# 📌 3️⃣ Faturamento por País (Excluindo Reino Unido, pois domina os dados)
df["Total"] = df["Quantity"] * df["UnitPrice"]
country_revenue = df.groupby("Country")["Total"].sum().sort_values(ascending=False)
top_countries = country_revenue.drop("United Kingdom").head(10)  # Remove UK para visualização

plt.figure(figsize=(10, 5))
sns.barplot(x=top_countries.values, y=top_countries.index, palette="coolwarm")
plt.xlabel("Faturamento Total")
plt.ylabel("País")
plt.title("Top 10 Países em Faturamento (excluindo UK)")
plt.subplots_adjust(left=0.3)
plt.show()




