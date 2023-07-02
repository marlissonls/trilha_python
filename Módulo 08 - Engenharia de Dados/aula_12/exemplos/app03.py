from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
df = pd.read_csv('gapminder2007.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='My First App with Data and a Graph'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    # dcc.Graph(figure=px.histogram(df, x='continent', y='gdpPercap', histfunc='avg'))
    # dcc.Graph(figure=px.histogram(df, x='continent', y='pop', histfunc='sum'))
    dcc.Graph(figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg'))
    # https://www.datasciencemadesimple.com/get-unique-values-rows-dataframe-python-pandas/
    # https://stackoverflow.com/questions/21402485/pandas-how-to-filter-a-df-to-get-unique-entries
    # grouped = df.groupby('continent').agg({'gdpPercap': max}).reset_index()
    # grouped = grouped.set_index(['continent','gdpPercap'])
    # second = grouped.join(df.set_index(['continent', 'gdpPercap']))
])

if __name__ == '__main__':
    app.run_server(debug=True)