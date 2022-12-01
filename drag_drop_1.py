import base64 # for decoding the file
import io #for saving the file

from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
#import plotly.express as px
#import dash_table

import pandas as pd

app = Dash(__name__)

app.layout = html.Div([
    dcc.Upload(
        id='upload-data', #to target it in our callback
        children=html.Div([
            'Drag and Drop',
            html.A('Upload Data') # clickable link to add the file
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        multiple=False #to upload just one file

    ),
    html.Div(id='output-data-upload') #for showing visualizations
])


@app.callback(
    Output('output-data-upload', 'children'),
    [Input('upload-data', 'contents')]
)
def update_output(contents):
    df = pd.DataFrame()
    if contents is not None:
        _, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))

        return df.to_csv('kiva.csv', index=False)


if __name__ == ('__main__'):

    app.run_server(debug=True)
