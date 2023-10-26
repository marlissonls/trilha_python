import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("./gapminder2007.csv")

# Calcule as médias do GDP per Capita por continente
continent_means = data.groupby('continent')['gdpPercap'].mean()

# Crie um gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(continent_means.index, continent_means.values, color='skyblue', width=.5)
# continent_means.plot(kind='bar', color='skyblue')
plt.title('Média do GDP per Capita por Continente')
plt.xlabel('Continente')
plt.ylabel('Média do GDP per Capita')
plt.xticks(rotation=45)
plt.show()