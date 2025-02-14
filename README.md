# Análise da Variação de Preços da Gasolina na Cidade de São Paulo (Julho de 2021) ⛽📊


## Introdução 🌟

O preço da gasolina ⛽ é um dos principais indicadores econômicos que afetam diretamente a vida cotidiana das pessoas. Suas flutuações podem ter implicações significativas sobre os custos de transporte 🚗, a inflação 📈 e o comportamento de consumo das famílias 💸. Nesse contexto, a análise da variação do preço da gasolina ao longo de um período específico se torna uma ferramenta importante para entender como esses fatores impactam a economia local 🌍. Este relatório visa analisar as variações de preço da gasolina na cidade de São Paulo durante os primeiros 10 dias de julho de 2021. O objetivo é observar o comportamento diário dos preços e identificar tendências ou padrões que possam fornecer insights relevantes para os consumidores e o mercado.

##Metodologia 🔍

Para a realização desta análise, os dados de preços da gasolina foram coletados de um posto de combustível localizado na cidade de São Paulo 🏙️. As informações foram registradas ao longo de 10 dias consecutivos, com os preços sendo registrados uma vez por dia 📅. O conjunto de dados foi organizado em um arquivo CSV 📊, onde cada linha representa a data de coleta e o valor do preço da gasolina registrado.

A análise foi conduzida utilizando a linguagem Python 🐍 e suas bibliotecas poderosas, como:

Pandas 🐼: Para manipulação e limpeza dos dados, além de facilitar a análise estatística.
Seaborn 🌊: Para criação de visualizações gráficas e análise exploratória dos dados.
Matplotlib 📈: Para personalizar gráficos e aprimorar a visualização dos resultados.
Através dessas ferramentas, foi possível criar um gráfico de linha 📉 para visualizar a evolução do preço da gasolina ao longo do período de 10 dias. No gráfico, o eixo X representa as datas de coleta e o eixo Y representa os valores dos preços da gasolina. Com isso, foi possível identificar as flutuações diárias e analisar o comportamento do preço durante o período de análise.



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

## Resultados 📊

O gráfico gerado revela uma variação significativa no preço da gasolina ⛽ ao longo dos 10 dias analisados. É possível observar que, em determinados dias, o preço apresentou quedas repentinas 📉, enquanto em outros momentos houve um aumento considerável 📈. No entanto, ao final do período observado, o preço se estabilizou, apresentando uma leve tendência de manutenção sem grandes oscilações.

Essas flutuações diárias indicam que o preço da gasolina não segue uma trajetória linear, e sim que está sujeito a influências variáveis, como fatores econômicos locais, políticas de precificação dos postos e até mesmo a demanda por combustíveis ao longo do tempo.

A partir dessa análise, concluímos que é fundamental acompanhar de perto essas variações de preço 🧐 para realizar compras mais vantajosas e evitar custos elevados em períodos de alta. Esse tipo de monitoramento diário pode oferecer insights valiosos para os consumidores que buscam otimizar seus gastos com combustíveis 🚗💡.

# Grafico:
![Grafico.JPG](https://github.com/Rafae1040/da-projeto-ebac/blob/main/gasolina.png)


## Conclusão 📝

Este relatório demonstrou que o preço da gasolina ⛽ pode variar significativamente em um curto período de tempo, o que reforça a importância de monitorar essas flutuações constantemente. A análise revelou que, apesar de os preços sofrerem oscilações diárias 📉📈, é possível identificar padrões que podem ajudar os consumidores a tomar decisões mais informadas sobre quando abastecer.

Ficar atento às variações de preço é essencial para garantir uma compra mais vantajosa 💰 e evitar prejuízos com aumentos inesperados no custo do combustível. Além disso, recomenda-se que essa análise seja realizada com maior frequência 📅, permitindo uma visão mais abrangente do mercado. Com essa abordagem contínua, os consumidores podem ter acesso a informações mais precisas e, assim, tomar decisões mais estratégicas e conscientes.

A compreensão dessas flutuações diárias não apenas beneficia os motoristas, mas também pode contribuir para um comportamento mais inteligente em relação ao consumo de combustível e à economia familiar 🚗💡.

## Resolução de Negócio 💼
Com base nos dados coletados, uma solução simples e sem custos seria criar uma comunidade de consumidores que compartilham informações sobre preços de gasolina em grupos de WhatsApp, Telegram ou redes sociais. Isso permitiria que os consumidores atualizassem os preços em tempo real, ajudando todos a aproveitar as melhores ofertas.

Outra alternativa seria utilizar aplicativos gratuitos de comparação de preços, que já oferecem dados sobre as variações nos postos de combustível. Assim, os consumidores podem monitorar os preços de forma prática e sem custos.

Para os donos de postos de gasolina, uma solução seria observar os preços da concorrência e ajustar suas estratégias de vendas com base nas flutuações de mercado. Isso poderia ser feito sem precisar de investimentos em ferramentas caras.

Essas soluções simples e de baixo custo podem beneficiar tanto consumidores quanto empresários, proporcionando uma gestão mais eficiente dos preços e uma experiência vantajosa para todos. 🚗💡
