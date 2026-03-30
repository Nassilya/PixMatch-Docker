import streamlit as st
from streamlit_option_menu import option_menu
import os

# Configuration de base
st.set_page_config(page_title="PixMatcher App", layout="wide")

st.markdown(
    """
    <style>
        h1 { color: black !important; font-weight: bold; }
        [data-testid="stSidebarNav"] { display: none; }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Welcome to the PixMatcher app")

# Menu de navigation
with st.sidebar:
    page = option_menu(
        menu_title="Navigation",
        options=["Search via Image", "Search via Text", "Visualization", "About"],
        icons=["bi-image", "bi-chat-right-text", "bar-chart", "info-circle"],
        menu_icon="list",
        default_index=0,
    )

# Chargement dynamique des pages
# Comme tous les fichiers sont dans le même dossier 'app', l'import est direct
if page == "Search via Image":
    import research
    research.main()
elif page == "Search via Text":
    import clip_research
    clip_research.main()
elif page == "Visualization":
    import visualization
    visualization.main()
elif page == "About":
    import about
    about.main()