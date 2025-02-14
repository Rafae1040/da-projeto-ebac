### Preço medio de venda da gasolina na cidade de São Paulo nos 10 primeiros dias primeiros dias de Julho de 2021.
Projeto será feito em linguagem python

### Introdução:
O objetivo deste relatório é analisar as variações de preço da gasolina em um determinado período de 10 dias. O preço da gasolina é um fator importante na economia e pode afetar o custo de vida das pessoas, por isso é importante entender como ele muda ao longo do tempo.

### Metodologia:
Os dados foram coletados de uma determinado posto de combustivel e registrados diariamente durante 10 dias. Utilizei o codigo python, bibliotecas como pandas,searborn e mmatplotlib para criar o gráfico de linhas através de um arquivo.csv, onde representei no eixo X as datas e no eixo Y os valores dos preços.

### Dados:

``` python
%%writefile gasolina.csv

dia, venda

1, 5.11

2, 4.99

3, 5.02

4, 5.21

5, 5.07

6, 5.09

7, 5.13

8, 5.12

9, 4.94

10, 5.03
```

## Código usado para criar o gráfico

```python
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./gasolina.csv') #lendo os dados do arquivo CSV e armazenando em uma variavel chamada "df" 

grafico = sns.lineplot(data=df,x='dia', y='venda') #criando uma grafico de linha usando os dados do "df" e usando "dia" como "x" e "venda" como "y"

plt.title("Preço da gasolina por dia") #Adicionando titulo ao grafico
plt.xlabel("Dia") #Adicionando rótulo ao eixo x
plt.ylabel("Preço") #Adicionando rótulo ao eixo y
plt.savefig('gasolina.png') #Salvando o grafico como imagem "gasolina.png"
```

Resultados:
O gráfico mostra que o preço da gasolina varia de maneira significativa durante os 10 dias. É possível observar que em determinado dia o preço teve uma queda e outro dia teve uma alta, mas ao final do período observado, o preço manteve-se estável. A partir desses dados, concluímos que é importante ficar atento as variações de preço para fazer uma compra mais vantajosa.

# Grafico:
![Grafico.JPG](https://github.com/Rafae1040/da-projeto-ebac/blob/main/gasolina.png)


## Conclusão:
Este relatório mostrou que o preço da gasolina varia significativamente em um curto período de tempo. É importante ficar atento as variações de preço para fazer uma compra mais vantajosa e não se prejudicar com o alto valor do combustivel. Pode-se sugerir que essa análise seja feita com maior frequencia para ter uma visão mais ampla do mercado e assim poder tomar decisões mais informadas.

