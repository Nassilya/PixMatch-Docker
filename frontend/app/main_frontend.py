import streamlit as st
from streamlit_option_menu import option_menu
import os

st.set_page_config(page_title="PixMatcher App", layout="wide")

st.markdown("""
    <style>
        /* Global background and text */
        [data-testid="stAppViewContainer"] {
            background-color: #0e1117;
            color: #e6edf3;
        }
        [data-testid="stHeader"] {
            background-color: #0e1117;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #161b22;
        }
        [data-testid="stSidebarNav"] { display: none; }

        /* All headings */
        h1, h2, h3, h4, h5, h6 {
            color: #e6edf3 !important;
        }

        /* Main title styling */
        .main-title {
            font-size: 2.8rem;
            font-weight: 800;
            background: linear-gradient(90deg, #7b61ff, #a78bfa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.2rem;
        }
        .main-subtitle {
            color: #8b949e;
            font-size: 1rem;
            margin-bottom: 2rem;
        }

        /* Buttons */
        .stButton > button {
            background: linear-gradient(90deg, #7b61ff, #a78bfa);
            color: white !important;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 2rem;
            font-weight: 600;
            transition: opacity 0.2s;
        }
        .stButton > button:hover {
            opacity: 0.85;
        }

        /* Radio buttons */
        .stRadio label { color: #e6edf3 !important; }

        /* Text input */
        .stTextInput input {
            background-color: #1c2128 !important;
            color: #e6edf3 !important;
            border: 1px solid #30363d !important;
            border-radius: 8px !important;
        }

        /* File uploader */
        [data-testid="stFileUploader"] {
            background-color: #1c2128;
            border: 1px dashed #7b61ff;
            border-radius: 10px;
            padding: 1rem;
        }

        /* Captions and small text */
        .stCaption, caption { color: #8b949e !important; }

        /* Divider */
        hr { border-color: #30363d; }

        /* Spinner */
        .stSpinner > div { border-top-color: #7b61ff !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">PixMatcher</p>', unsafe_allow_html=True)
st.markdown('<p class="main-subtitle">AI-powered image similarity search</p>', unsafe_allow_html=True)
st.divider()

with st.sidebar:
    page = option_menu(
        menu_title="Navigation",
        options=["Search via Image", "Search via Text", "Visualization"],
        icons=["bi-image", "bi-chat-right-text", "bar-chart"],
        menu_icon="list",
        default_index=0,
        styles={
            "container": {"background-color": "#161b22"},
            "menu-title": {"color": "#a78bfa", "font-weight": "700"},
            "icon": {"color": "#7b61ff"},
            "nav-link": {"color": "#e6edf3", "font-size": "15px"},
            "nav-link-selected": {"background-color": "#7b61ff", "color": "white"},
        }
    )

if page == "Search via Image":
    import research
    research.main()
elif page == "Search via Text":
    import clip_research
    clip_research.main()
elif page == "Visualization":
    import visualization
    visualization.main()
