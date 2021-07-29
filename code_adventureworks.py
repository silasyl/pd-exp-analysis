import os
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn")
df = pd.read_excel(os.path.join("datasets", "AdventureWorks.xlsx"))
print(df.head())
print()
print("Linhas e colunas: ", df.shape)
print("Tipos de dados:\n", df.dtypes)
print("Receita total: ", df["Valor Venda"].sum(), "\n")
df["custo"] = df["Custo Unitário"].mul(df["Quantidade"])    # Coluna custo
print(df.head(1))
print("Custo Total: ", round(df["custo"].sum(), 2), "\n")
df["lucro"] = df["Valor Venda"] - df["custo"]
print(df.head(1))
print("Total Lucro: ", round(df["lucro"].sum(), 2), "\n")

df["Tempo_envio"] = df["Data Envio"] - df["Data Venda"]
print(df.head(1))
df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days
print(df.head(1))
print("Tipo Tempo_envio: ", df["Tempo_envio"].dtype)
print("Media de tempo por marca: ", df.groupby("Marca")["Tempo_envio"].mean())

print("Dados faltantes: ", df.isnull().sum())

print("Agrupar lucro por ano e marca:\n", df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum())
pd.options.display.float_format = '{:20,.2f}'.format
print("Agrupar lucro por ano e marca:\n", df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum())
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"]).sum().reset_index()
print(lucro_ano)
print("Total de produtos vendidos:\n", df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False))

df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title="Total Produtos Vendidos")
plt.show()
plt.xlabel("Total")
plt.ylabel("Produto")

df.groupby(df["Data Venda"].dt.year)["lucro"].sum().plot.bar(title="Lucro x Ano")
plt.show()
plt.xlabel("Ano")
plt.ylabel("Receita")

df_2009 = df[df["Data Venda"].dt.year == 2009]
print(df_2009.head())
df_2009.groupby(df_2009["Data Venda"].dt.month)["lucro"].sum().plot(title="Lucro x Mes")
plt.show()
plt.xlabel("Mes")
plt.ylabel("Lucro")

df_2009.groupby("Marca")["lucro"].sum().plot.bar(title="Lucro x Marca")
plt.show()
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal')

df_2009.groupby("Classe")["lucro"].sum().plot.bar(title="Lucro x Classe")
plt.show()
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal')

print("Describe:\n", df["Tempo_envio"].describe())
plt.boxplot(df["Tempo_envio"])     # Grafico de boxplot
plt.show()
plt.hist(df["Tempo_envio"])         # Histograma
plt.show()
print("Tempo minimo de envio: ", df["Tempo_envio"].min())
print("Tempo maximo de envio: ", df["Tempo_envio"].max())
print("Outlier: ", df[df["Tempo_envio"] == 20])

df.to_csv("df_vendas_novo.csv", index=False)