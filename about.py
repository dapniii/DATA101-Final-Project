from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("About", href="#")),
        dbc.NavItem(dbc.NavLink("Home", href="/terror_app")),
    ],
    brand="Global Terrorism",
    brand_href="#",
    color="dark",
    dark=True,
    style={
        'margin-bottom': '1em'
    }
)

# Initialize Dash application
app = Dash(__name__, 
           external_stylesheets=[dbc.themes.BOOTSTRAP])

# App layout
app.layout = html.Div(children=[
    navbar,
    dbc.Container([
        # Description
        dbc.Card([
            dbc.CardHeader([
                html.H3('Mapping Global Terrorism: Examining Patterns and Hotspots'),
            ]),
            dbc.CardBody([
                html.Div([
                    html.Img(src='assets/sdg16-color.png'),
                    html.P('Created through an open-source database chronicling terrorist attacks spanning 1970 to 2017, featuring over 200,000 incidents from domestic unrest to international crises. Delve into a wealth of information encompassing attack specifics, weapon details, victim insights, and perpetrator identities, including affiliations with terrorist groups. Our platform empowers researchers, policymakers, and global citizens with comprehensive insights to comprehend and address the multifaceted challenges of terrorism, all within an easily accessible interface.')
                ], style={
                'display': 'flex',
                'gap': '1.5em'
                })
            ], style={
                'display': 'flex',
                'flex-direction': 'column',
                'gap': '2em'
            }),        
        ]),
        # Motivators
        dbc.Card([
            dbc.CardHeader([
                html.H5('Motivations of the Study'),
            ]),
            dbc.CardBody([
                dbc.Row([
                    dbc.Col([
                        html.Img(
                            src='assets/awareness.png',
                            style={
                                'width': '50%',
                                'height': '50%',
                                'object-fit': 'contain'
                            }
                        ),
                        html.H5('Provide Awareness'),
                    ], style={
                        'display': 'flex',
                        'flex-direction': 'column',
                        'align-items': 'center',
                        'justify-content': 'center',
                        'text-align': 'center',
                        'gap': '1em'
                    }),
                    dbc.Col([
                        html.Img(
                            src='assets/trend.png',
                            style={
                                'width': '50%',
                                'height': '50%',
                                'object-fit': 'contain'
                            }
                        ),
                        html.H5('Analyze Trends and Patterns'),
                    ], style={
                        'display': 'flex',
                        'flex-direction': 'column',
                        'align-items': 'center',
                        'justify-content': 'center',
                        'text-align': 'center',
                        'gap': '1em'
                    }),
                    dbc.Col([
                        html.Img(
                            src='assets/lack-summary.png',
                            style={
                                'width': '50%',
                                'height': '50%',
                                'object-fit': 'contain'
                            }
                        ),
                        html.H5('Lack of Collated Summary'),
                    ], style={
                        'display': 'flex',
                        'flex-direction': 'column',
                        'align-items': 'center',
                        'justify-content': 'center',
                        'text-align': 'center',
                        'gap': '1em'
                    }),
                    dbc.Col([
                        html.Img(
                            src='assets/dashboard.png',
                            style={
                                'width': '50%',
                                'height': '50%',
                                'object-fit': 'contain'
                            }
                        ),
                        html.H5('Limited Availability of Dashboards'),
                    ], style={
                        'display': 'flex',
                        'flex-direction': 'column',
                        'align-items': 'center',
                        'justify-content': 'center',
                        'text-align': 'center',
                        'gap': '1em'
                    }),
                    dbc.Col([
                        html.Img(
                            src='assets/terrorism.png',
                            style={
                                'width': '50%',
                                'height': '50%',
                                'object-fit': 'contain'
                            }
                        ),
                        html.H5('Ongoing Presence of Terrorism'),
                    ], style={
                        'display': 'flex',
                        'flex-direction': 'column',
                        'align-items': 'center',
                        'justify-content': 'center',
                        'text-align': 'center',
                        'gap': '1em'
                    }),
                ], style={
                    'gap': '1em'
                })
            ])
        ]),
        # Target Audience
        dbc.Card([
            dbc.CardHeader([
                html.H5('Target Audience'),
            ]),
            dbc.Row([
                dbc.Col([
                    html.Img(
                        src='assets/government.png',
                        style={
                            'width': '50%',
                            'height': '50%',
                            'object-fit': 'contain'
                        }
                    ),
                    html.H5('Government'),
                ], style={
                    'display': 'flex',
                    'flex-direction': 'column',
                    'align-items': 'center',
                    'justify-content': 'center',
                    'text-align': 'center',
                    'gap': '1em'
                }),
                dbc.Col([
                    html.Img(
                        src='assets/ngo.png',
                        style={
                            'width': '50%',
                            'height': '50%',
                            'object-fit': 'contain'
                        }
                    ),
                    html.H5('International Non-Profit Organizations'),
                ], style={
                    'display': 'flex',
                    'flex-direction': 'column',
                    'align-items': 'center',
                    'justify-content': 'center',
                    'text-align': 'center',
                    'gap': '1em'
                }),
                dbc.Col([
                    html.Img(
                        src='assets/reporter.png',
                        style={
                            'width': '50%',
                            'height': '50%',
                            'object-fit': 'contain'
                        }
                    ),
                    html.H5('Media'),
                ], style={
                    'display': 'flex',
                    'flex-direction': 'column',
                    'align-items': 'center',
                    'justify-content': 'center',
                    'text-align': 'center',
                    'gap': '1em'
                }),
                dbc.Col([
                    html.Img(
                        src='assets/people.png',
                        style={
                            'width': '50%',
                            'height': '50%',
                            'object-fit': 'contain'
                        }
                    ),
                    html.H5('General Public'),
                ], style={
                    'display': 'flex',
                    'flex-direction': 'column',
                    'align-items': 'center',
                    'justify-content': 'center',
                    'text-align': 'center',
                    'gap': '1em',
                }),
            ], style={
                    'gap': '1em'
            })  
        ]),
    ], style={
        'display':'flex',
        'flex-direction': 'column',
        'gap': '1em',
        'padding-bottom': '1em'
    }),
])

    

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

