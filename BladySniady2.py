import streamlit as st
import streamlit.components.v1 as components
import base64

# --- KONFIGURACJA STRONY ---
st.set_page_config(
    page_title="Arena | Bladysniady Esports",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- LOGIKA UKRYTEGO PANELU ADMINA ---
# Dostęp: dopisz ?admin=true na końcu adresu URL
is_admin = st.query_params.get("admin") == "true"

if 'fols' not in st.session_state: st.session_state.fols = "250K+"
if 'wins' not in st.session_state: st.session_state.wins = "1,200+"
if 'hours' not in st.session_state: st.session_state.hours = "5,000+"

if is_admin:
    with st.sidebar:
        st.title("🛠️ Panel Admina")
        st.session_state.fols = st.text_input("Followers", st.session_state.fols)
        st.session_state.wins = st.text_input("Wins", st.session_state.wins)
        st.session_state.hours = st.text_input("Hours", st.session_state.hours)
        st.info("Zmień wartości i odśwież widok.")
else:
    st.markdown("<style>section[data-testid='stSidebar'] {display: none;}</style>", unsafe_allow_html=True)

# --- UKRYWANIE ELEMENTÓW STREAMLIT ---
st.markdown("<style>#MainMenu, footer, header {visibility: hidden;} .block-container {padding: 0px !important;}</style>", unsafe_allow_html=True)

# --- TWÓJ KOD HTML (Zdekodowany, by uniknąć błędów cudzysłowów) ---
# Używamy prostego łączenia stringów, aby uniknąć problemów z potrójnym cudzysłowem
h = "<!DOCTYPE html><html lang='pl'><head><meta charset='UTF-8'>"
h += "<link href='https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap' rel='stylesheet'>"
h += "<style>"
h += "*{margin:0;padding:0;box-sizing:border-box;scroll-behavior:smooth;}"
h += "body{font-family:'Orbitron',sans-serif;background:#050507;color:white;overflow-x:hidden;}"
h += "#particles{position:fixed;width:100%;height:100%;top:0;left:0;z-index:-1;background:#050507;}"
h += "nav{position:fixed;width:100%;top:0;display:flex;justify-content:space-between;align-items:center;padding:20px 10%;background:rgba(0,0,0,0.6);backdrop-filter:blur(10px);z-index:1000;}"
h += "nav h1{color:#ff2e2e;letter-spacing:3px;}"
h += ".navbar-links{display:flex;gap:30px;}"
h += ".navbar-links a{color:white
