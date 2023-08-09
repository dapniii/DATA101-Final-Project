import dash
from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc


# Initialize Dash application
app = Dash(__name__, 
           use_pages=True,
           external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    # Change to bootstrap navbar
    html.Div(
        [
            html.Div(
                dcc.Link(
                    f"{page['name']} - {page['path']}", href=page["relative_path"]
                )
            )
            for page in dash.page_registry.values()
        ]
    ),
	dash.page_container
])

# Run the app
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)