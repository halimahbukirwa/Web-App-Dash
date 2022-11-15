import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

# create an instance of the dash app

app = dash.Dash(__name__)
# we pass in name so that our app will be able
# to know the correct path for items such as assets(css files)

df = pd.read_csv('kiva_el.csv')

fig = px.bar(df, x='sector', y='loan_amount')

app.layout = html.Div(
    children = (
        html.H1(children = ' Data Science Application'),
        dcc.Graph(id='bar-plot', figure=fig)

    )
)

if __name__ =='__main__':
    app.run_server(debug=True)
