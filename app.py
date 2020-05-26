import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import os
import pandas as pd




external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#dash_app = dash.Dash(__name__,
 #                    external_stylesheets=external_stylesheets)
#server = dash_app.server

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

APP_PATH=os.path.dirname(os.path.abspath(__file__))

pop = pd.read_csv(os.path.join(APP_PATH, os.path.join("data", "population.csv")),index_col=False)


app.layout = html.Div([

    html.H1("Population Dashboard ", style={"text-align":"center"}),

    html.Div(
        [
            dcc.Input(
                placeholder="Enter a year",
                id="input",
                style={"width":"60%"},type='number'
                ),
            html.Button(id='submit-button', n_clicks=0, children='Submit'),
            html.Div(id='dummy'),
            
        ]
        , style={"text-align":"center", "width":"100%", "columnCount":2}),

    html.Table(
        [
            html.Tbody([
                html.Tr([
                    html.Td(pop.iloc[i][col]) for col in pop.columns
                ]) for i in range(min(len(pop), 5))
            ], id="table1")
        ], style={"width": "100%"}
    ),


    dcc.Graph(
        id='graph-1',
        figure={
            'data': [
                {'x':pop['Year'],'y':pop['Total Population']}],
            'layout': dict(
                xaxis={'title': 'Year'},
                yaxis={'title': 'Total Population'})


        }),
    html.H2("Population-Years", style={"text-align": "center"}),


    dcc.Graph(
        id='graph-2',
        figure={
            'data': [
                {'x':pop['Year'],'y':pop['Births']}],
            'layout': dict(
                xaxis={'title': 'Year'},
                yaxis={'title': 'Births'})

        }),
    html.H2("Births-Years", style={"text-align": "center"}),


    dcc.Graph(
        id='graph-3',
        figure={
            'data': [
                {'x': pop['Year'], 'y': pop['Deaths']}],
            'layout': dict(
                xaxis={'title': 'Year'},
                yaxis={'title': 'Deaths'})

        }),

    html.H2("Deths-Years", style={"text-align": "center"}),


    dcc.Graph(
        id='graph-4',
        figure={
            'data': [
                {'x': pop['Year'], 'y': pop['Natural change (per 1000)']}],
            'layout': dict(
                xaxis={'title': 'Year'},
                yaxis={'title': 'Natural change (per 1000)'})

        }),
    html.H2("Natural change (per 1000)-Years", style={"text-align": "center"})

])


# ------------------------------- CALLBACKS ---------------------------------------- #



@app.callback(Output('table1','children'),
              [Input('submit-button', 'n_clicks')],
              [State('input', 'value')])


def update_output(n_clicks,x):
    i=0
    mshmsh = pop.iloc[80:, :]
    for i in range(0,pop.shape[0],1):
        if pop.loc[i,'Year']==x:
            mshmsh= pop.iloc[i:i+1,:]
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in mshmsh.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(mshmsh.iloc[i][col]) for col in mshmsh.columns
            ]) for i in range(min(len(mshmsh), 5))
        ])
    ])

if __name__ == '__main__':
    app.run_server(debug=True)



