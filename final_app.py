import dash
from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc

# Initialize Dash application
app = Dash(__name__, 
           use_pages=True,
           external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    # Bootstrap navbar 
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink(f"{page['name']}", href=page["relative_path"]))
            for page in dash.page_registry.values()
        ],
        brand="Global Terrorism",
        brand_href="#",
        color="dark",
        dark=True,
        style={
            'margin-bottom': '1em'
        }
    ),
	dash.page_container
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)