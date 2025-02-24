import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Carregar dataset limpo
df = pd.read_csv("data/dataecommerce_cleaned.csv")

# Converter a coluna de data para formato datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Criar coluna de faturamento
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# Agrupar por mês
df_weekly = df.resample('W', on='InvoiceDate').sum()

# Plotar faturamento ao longo do tempo
plt.figure(figsize=(12,6))
plt.plot(df_weekly.index, df_weekly['Revenue'], marker='o', linestyle='-')
plt.xlabel("Data")
plt.ylabel("Faturamento (£)")
plt.title("Faturamento ao Longo do Tempo")
plt.xticks(rotation=45)
plt.grid()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Carregar os dados
df = pd.read_csv("data/dataecommerce_cleaned.csv", parse_dates=["InvoiceDate"])
df.set_index("InvoiceDate", inplace=True)
df['Revenue'] = df['Quantity'] * df['UnitPrice']


# Agrupar faturamento por mês
revenue_by_date = df.resample('W').sum()['Revenue']

# Aplicar decomposição da série temporal
decomposed = seasonal_decompose(revenue_by_date, model='additive', period=12)

# Plotar os componentes
plt.figure(figsize=(12, 8))

plt.subplot(411)
plt.plot(revenue_by_date, label='Original', color='blue')
plt.legend(loc='upper left')

plt.subplot(412)
plt.plot(decomposed.trend, label='Tendência', color='red')
plt.legend(loc='upper left')

plt.subplot(413)
plt.plot(decomposed.seasonal, label='Sazonalidade', color='green')
plt.legend(loc='upper left')

plt.subplot(414)
plt.plot(decomposed.resid, label='Resíduo', color='gray')
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()
