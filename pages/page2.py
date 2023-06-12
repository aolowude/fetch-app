# Import necessary libraries 
import dash
from dash import html
import dash_bootstrap_components as dbc

# Define the final page layout
layout = dbc.Container(
    [
        html.H1("Fetch Chat"),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader("Ask anything"),
                                dbc.CardBody(id='chat-output', className="chat-output")
                            ],
                            className="mb-3"
                        ),
                        dbc.Input(id='user-input', type='text', placeholder='Enter your message...'),
                        dbc.Button("Fetch",id='send-button', color="primary")

                    ],
                    width=10
                )
               
            ]
        )
    ],
    className="mt-4"
)
