import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output, State

# Datos de ejemplo
data = {
    "Categoría": ["A", "B", "C", "D"],
    "Valor1": [10, 15, 8, 12],
    "Valor2": [5, 7, 9, 6],
}

df = pd.DataFrame(data)

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.MATERIA, dbc.icons.FONT_AWESOME])

# Define el contenido del sidebar
sidebar = html.Div(
    [
        html.Div(
            [html.H2("Auto ML", style={"color": "white"})],
            className="sidebar-header",
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [html.I(className="fas fa-home me-2"), html.Span("Dashboard")],
                    href="/",
                    active="exact",
                ),
                dbc.NavLink(
                    [html.I(className="fas fa-calendar-alt me-2"), html.Span("Projects")],
                    href="/projects",
                    active="exact",
                ),
                dbc.NavLink(
                    [html.I(className="fas fa-envelope-open-text me-2"), html.Span("Datasets")],
                    href="/datasets",
                    active="exact",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar",
    id="sidebar"  # Aseguramos que el sidebar tenga un id
)

# Define el diseño general de la aplicación
app.layout = html.Div(
    [
        # Botón de menú para dispositivos móviles
        dbc.Button(
            html.I(className="fas fa-bars"),
            id="menu-button",
            className="menu-button",
            n_clicks=0
        ),
        sidebar,
        html.Div(
            [
                html.H1("Gráficos de ejemplo"),
                dcc.Graph(
                    id="bar-chart1",
                    figure=px.bar(df, x="Categoría", y=["Valor1", "Valor2"], title="Gráfico de barras"),
                ),
                dcc.Graph(
                    id="bar-chart2",
                    figure=px.bar(df, x="Categoría", y="Valor1", title="Otro gráfico de barras"),
                ),
                dcc.Graph(
                    id="pie-chart",
                    figure=px.pie(df, names="Categoría", values="Valor2", title="Gráfico de círculo"),
                ),
            ],
            className="content",
        ),
    ],
    className="app-container"
)

# Callback para mostrar/ocultar el sidebar en dispositivos móviles
@app.callback(
    Output("sidebar", "className"),
    [Input("menu-button", "n_clicks")],
    [State("sidebar", "className")]
)
def toggle_sidebar(n_clicks, sidebar_class):
    if n_clicks:
        if "collapsed" in sidebar_class:
             # Si el sidebar está colapsado, expandirlo
            return sidebar_class.replace(" collapsed", "")
        else:
            # Si el sidebar está expandido, colapsarlo
            return sidebar_class + " collapsed"
    return sidebar_class

if __name__ == "__main__":
    app.run_server(debug=True,port=8052)
