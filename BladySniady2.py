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
query_params = st.query_params
is_admin = query_params.get("admin") == "true"

# Inicjalizacja statystyk w pamięci sesji
if 'fols' not in st.session_state: st.session_state.fols = "250K+"
if 'wins' not in st.session_state: st.session_state.wins = "1,200+"
if 'hours' not in st.session_state: st.session_state.hours = "5,000+"

if is_admin:
    with st.sidebar:
        st.title("🛠️ Panel Admina")
        st.session_state.fols = st.text_input("Followers", st.session_state.fols)
        st.session_state.wins = st.text_input("Wins", st.session_state.wins)
        st.session_state.hours = st.text_input("Hours", st.session_state.hours)
        st.info("Zmienione wartości pojawią się na stronie głównej.")
else:
    st.markdown("<style>section[data-testid='stSidebar'] {display: none;}</style>", unsafe_allow_html=True)

# --- UKRYWANIE ELEMENTÓW STREAMLIT ---
st.markdown("<style>#MainMenu, footer, header {visibility: hidden;} .block-container {padding: 0px !important;} iframe {border: none;}</style>", unsafe_allow_html=True)

# --- SZABLON HTML (Zwykły string bez 'f' na początku - chroni przed SyntaxError) ---
html_template = """
<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box;scroll-behavior:smooth;}
body{font-family:'Orbitron',sans-serif;background:#050507;color:white;overflow-x:hidden;}
#particles{position:fixed;width:100%;height:100%;top:0;left:0;z-index:-1;background:#050507;}
nav{position:fixed;width:100%;top:0;display:flex;justify-content:space-between;align-items:center;padding:20px 10%;background:rgba(0,0,0,0.6);backdrop-filter:blur(10px);z-index:1000;}
nav h1{color:#ff2e2e;letter-spacing:3px;}
.navbar-links{display:flex;gap:30px;}
.navbar-links a{color:white;text-decoration:none;transition:0.3s;}
.navbar-links a:hover{color:#ff2e2e;}
section{padding:120px 10%;text-align:center;}
h3{font-size:34px;margin-bottom:40px;color:#ff2e2e;}
.arena-section{background:#111;padding:60px;border-radius:15px;margin-bottom:40px;border:1px solid #222;transition:0.3s;}
.arena-section:hover{transform:scale(1.02);border-
