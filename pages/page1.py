# Import necessary libraries 
from dash import html
import dash_bootstrap_components as dbc

card = dbc.Card(
    [
        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
        dbc.CardBody(
            [
                html.H4("Weight Loss", className="card-title"),
                html.P(
                    "Get some food ideas for weight loss",
                    className="card-text",
                ),
                dbc.Button("View More >", color="primary"),
            ]
        ),
    ],
    style={"width": "18rem"},
)
card2 = dbc.Card(
    [
        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
        dbc.CardBody(
            [
                html.H4("Muscle Gain", className="card-title"),
                html.P(
                    "Suggestions for Muscle Gain",
                    className="card-text",
                ),
                dbc.Button("View More >", color="primary"),
            ]
        ),
    ],
    style={"width": "18rem"},
)

card3 = dbc.Card(
    [
        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
        dbc.CardBody(
            [
                html.H4("Diabetic", className="card-title"),
                html.P(
                    "Suggestions for sugar free items",
                    className="card-text",
                ),
                dbc.Button("View More >", color="primary"),
            ]
        ),
    ],
    style={"width": "18rem"},
)

card4 = dbc.Card(
    [
        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
        dbc.CardBody(
            [
                html.H4("Pregnancy", className="card-title"),
                html.P(
                    "Suggestions for baby health",
                    className="card-text",
                ),
                dbc.Button("View More >", color="primary"),
            ]
        ),
    ],
    style={"width": "18rem"},
)

# Define the page layout
layout = dbc.Container([
    dbc.Row([card,card2,card3,card4])
    ],
    className="mt-4"

)
