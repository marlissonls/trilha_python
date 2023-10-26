from dash import Dash, html, dash_table
import pandas as pd

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
df = pd.read_csv('gapminder2007.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='My First App with Data'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=20)
])

if __name__ == '__main__':
    app.run_server(debug=True)