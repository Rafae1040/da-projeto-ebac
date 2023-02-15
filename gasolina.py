import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./gasolina.csv')

grafico = sns.lineplot(data=df,x='dia', y='venda')
plt.title("Media de Preço da Gasolina por Dia")
plt.xlabel("Dia")
plt.ylabel("Preço")
plt.savefig('gasolina.png')
