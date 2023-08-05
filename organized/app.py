from dash import Dash, html, dcc, Input, Output, callback
from charts import *
from callback import *
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc



app = Dash(__name__, 
           external_stylesheets=[dbc.themes.BOOTSTRAP])

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="Exploring Global Terrorism",
    brand_href="#",
    color="dark",
    dark=True,
)

# App layout
app.layout = html.Div(children=[
    navbar,
    dbc.Container([
           dbc.Row([
                dbc.Card([
                    dbc.CardHeader('Number of Attacks by Terrorist Groups'),
                    dbc.CardBody([
                        dcc.Slider(id="birth-year-slider",
                            min=years_attack.min(),
                            max=years_attack.max(),
                            marks=years_options,
                            step=1,
                        ),
                        dcc.Loading([dcc.Graph(id="scatter-map", figure=fig_map)]),
                    ])  
                ], style={
                    "padding": 0,
                    }) # Card
            ], style={
                "padding": 15,
                }
            ), # Row
            dbc.Row([
            
            ])
        ]
    ) 
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)