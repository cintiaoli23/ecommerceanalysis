import pandas as pd

df = pd.read_csv("data/dataecommerce_cleaned.csv")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"]) # Converter InvoiceDate para formato de data
df["Revenue"] = df["UnitPrice"] * df["Quantity"] # Para criar uma coluna de Faturamento (UnitPrice * Quantity)

faturamento_total = df["Revenue"].sum()
clientes_unicos = df["CustomerID"].nunique() # Numero de clientes
pedidos_totais = df["InvoiceNo"].nunique()
ticket_medio = faturamento_total / pedidos_totais
produtos_mais_vendidos = df.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head(10)
produtos_mais_rentaveis = df.groupby("Description")["Revenue"].sum().sort_values(ascending=False).head(10)

print(f" Faturamento Total: £{faturamento_total:,.2f}")
print(f" Número total de clientes únicos: {clientes_unicos}")
print(f" Número total de pedidos: {pedidos_totais}")
print(f" Ticket médio: £{ticket_medio:,.2f}")
print("\n Top 10 Produtos Mais Vendidos:")
print(produtos_mais_vendidos)
print("\n Top 10 Produtos Mais Rentáveis:")
print(produtos_mais_rentaveis)
