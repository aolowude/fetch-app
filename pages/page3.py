import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

profileCard = dbc.Card(
    [
        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
        dbc.CardBody(
            [
                html.H4("First Name", className="card-title"),
                html.H6("Last Name", className="card-title"),
                html.H6("Age", className="card-title"),
                html.H6("Gender", className="card-title"),
                html.H6("Food allergies", className="card-title"),
                
                dbc.Button("Edit>", color="primary"),
            ]
        ),
    ],
    style={"width": "18rem"},
)

layout = dbc.Container([
html.Div(
        [
            html.H1("Edit Your Profile"),
            html.Hr(),
            html.P(f"Share more about yourself to get better results"),
            profileCard,
        ],
        className="p-3 bg-light rounded-3",
    )
])