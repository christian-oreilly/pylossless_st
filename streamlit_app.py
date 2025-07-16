import streamlit as st
import streamlit.components.v1 as components
import subprocess
import threading
from dash import Dash, html
from pylossless.dash.app import get_app

def run_dash_app():

    app = get_app()#kind="jupyter")
    app.run_server(port=8502)#mode="inline")

    #app = Dash()
    #app.layout = html.Div("This is the Dash app inside the Streamlit app!")
    #app.run_server(debug=True, port=8502) # Run Dash on a different port than Streamlit

if __name__ == '__main__':
    threading.Thread(target=run_dash_app, daemon=True).start()
    st.set_page_config(layout="wide")    
    st.title("")
    components.iframe("http://localhost:8502", #width=700, 
                      height=1000, 
                      scrolling=False)