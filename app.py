import streamlit as st
import streamlit.components.v1 as components

# 1. Set the page to wide mode so your map has plenty of room
st.set_page_config(page_title="Snowmelt Model", layout="wide")

st.title("Interactive Snowmelt Energy Balance Model")

# 2. Open and read your HTML file
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_source = f.read()
        
    # 3. Render the HTML using Streamlit Components
    # CRITICAL: You MUST set a height here, otherwise the 100vh in your CSS 
    # will cause the iframe to collapse into a blank/tiny screen.
    components.html(html_source, height=800, scrolling=True)

except FileNotFoundError:
    st.error("Could not find index.html. Make sure it is in the same directory as app.py.")
