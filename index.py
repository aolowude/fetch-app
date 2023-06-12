# Import necessary libraries 
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

# Connect to main app.py file
from app import app

# Connect to your app pages
from pages import page1, page2, page3

# Connect the navbar to the index
from components import navbar
import openai
import time
    # Set the model engine and your OpenAI API key
model_engine = "text-davinci-003"
openai.api_key = "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" #follow step 4 to get a secret_key

# define the navbar
nav = navbar.Navbar()

# Define the index page layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav, 
    html.Div(id='page-content', children=[]), 
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page1':
        return page1.layout
    if pathname == '/page2':
        return page2.layout
    if pathname == '/page3':
        return page3.layout
    else:
        return "404 Page Error! Please choose a link"


@app.callback(
    Output('chat-output', 'children'),
    [Input('send-button', 'n_clicks')],
    [State('user-input', 'value'), State('chat-output', 'children')]
)
def generate_response(n_clicks, user_message, chat_output):
    if n_clicks and user_message:
        if chat_output is None:
            chat_output = []
      
        api_key = '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'
        openai.api_key = api_key
        print("before request")
        model_engine = "text-davinci-003"

        response = openai.Completion.create(
            engine = model_engine,
              prompt = user_message,
              max_tokens = 1024,
              n = 1,
              temperature = 0.5,
                  )
        prompt = 'Once upon a time'
        print("before response")
        print(response)
        print("after response")
        # if response.status_code == 200:
        bot_reply = response['choices'][0]['text']
        chat_output.append(dbc.ListGroupItem("You: " + user_message))
        chat_output.append(dbc.ListGroupItem("Fetch: " + bot_reply))
        # else:
            # chat_output.append(dbc.ListGroupItem("Error: Failed to get a response from the API"))
        print('chat_output')
        print(chat_output)
        return chat_output

    return chat_output

# Run the app on localhost:8050
if __name__ == '__main__':
    app.run_server(debug=True)
