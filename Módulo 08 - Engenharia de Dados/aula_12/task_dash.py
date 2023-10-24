import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Carregue o dataset
data = pd.read_csv("./gapminder2007.csv")

# Calcule as médias do GDP per Capita, População e Expectativa de Vida por continente
continent_means = data.groupby('continent').agg({
    'gdpPercap': 'mean',
    'pop': 'mean',
    'lifeExp': 'mean'
}).reset_index()

# Crie um aplicativo Dash
app = dash.Dash(__name__)

# Defina as cores de fundo escuras
app.layout = html.Div(style={'backgroundColor': '#442233', 'text-align': 'center', 'padding-top': '2px'}, children=[
    html.H1("Dashboard de Dados Mundiais", style={'color': '#CFDBFA'}),
    
    # Gráfico de GDP per Capita (ocupando a largura da página)
    dcc.Graph(id='gdp-bar-chart', style={'background-color': 'darkgray'}),
    
    # Gráficos de População e Expectativa de Vida (lado a lado)
    html.Div(style={'display': 'flex'}, children=[
        dcc.Graph(id='pop-bar-chart', style={'width': '50%'}),
        dcc.Graph(id='lifeexp-bar-chart', style={'width': '50%'}),
    ]),
])

@app.callback(
    Output('gdp-bar-chart', 'figure'),
    Output('pop-bar-chart', 'figure'),
    Output('lifeexp-bar-chart', 'figure'),
    Input('gdp-bar-chart', 'relayoutData'),
)
def update_bar_charts(relayoutData):
    gdp_fig = px.bar(continent_means, x='continent', y='gdpPercap', color='continent')
    gdp_fig.update_layout(title='Média do GDP per Capita por Continente', xaxis_title='Continente', yaxis_title='Média do GDP per Capita')
    
    pop_fig = px.bar(continent_means, x='continent', y='pop', color='continent')
    pop_fig.update_layout(title='Média da População por Continente', xaxis_title='Continente', yaxis_title='Média da População')
    
    lifeexp_fig = px.bar(continent_means, x='continent', y='lifeExp', color='continent')
    lifeexp_fig.update_layout(title='Média da Expectativa de Vida por Continente', xaxis_title='Continente', yaxis_title='Média da Expectativa de Vida')
    
    return gdp_fig, pop_fig, lifeexp_fig

if __name__ == '__main__':
    app.run_server(debug=True)
