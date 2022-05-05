import dash
from dash import dcc
from dash import html
import plotly.express as px
import quandl

df = quandl.get("WIKI/TSLA.4", start_date="2017-1-1", end_date="2018-3-31")

figura = px.line(df, title="Cotización de Tesla: ENERO 2017 - Marzo 2018")

app = dash.Dash()
app.layout = html.Div(children=[html.H1(children="APLICACIÓN CON DASH PARA OBSERVAR Y ANALIZAR MERCADOS FINANCIEROS"),
                        dcc.Graph(figure=figura)])

if __name__ == "__main__":
    app.run_server(debug=True)
