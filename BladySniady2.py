import streamlit as st
import streamlit.components.v1 as components
import base64

# --- KONFIGURACJA STRONY ---
st.set_page_config(page_title="Arena | Bladysniady Esports", layout="wide", initial_sidebar_state="collapsed")

# --- LOGIKA UKRYTEGO PANELU ADMINA ---
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
else:
    st.markdown("<style>section[data-testid='stSidebar'] {display: none;}</style>", unsafe_allow_html=True)

# --- UKRYWANIE ELEMENTÓW STREAMLIT ---
st.markdown("<style>#MainMenu, footer, header {visibility: hidden;} .block-container {padding: 0px !important;}</style>", unsafe_allow_html=True)

# --- BUDOWANIE HTML (Metoda segmentowa - najbezpieczniejsza) ---
p = []
p.append("<!DOCTYPE html><html lang='pl'><head><meta charset='UTF-8'>")
p.append("<link href='https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap' rel='stylesheet'>")
p.append("<style>")
p.append("*{margin:0;padding:0;box-sizing:border-box;scroll-behavior:smooth;}")
p.append("body{font-family:'Orbitron',sans-serif;background:#050507;color:white;overflow-x:hidden;}")
p.append("#particles{position:fixed;width:100%;height:100%;top:0;left:0;z-index:-1;background:#050507;}")
p.append("nav{position:fixed;width:100%;top:0;display:flex;justify-content:space-between;align-items:center;padding:20px 10%;background:rgba(0,0,0,0.6);backdrop-filter:blur(10px);z-index:1000;}")
p.append("nav h1{color:#ff2e2e;letter-spacing:3px;}")
p.append(".navbar-links{display:flex;gap:30px;}.navbar-links a{color:white;text-decoration:none;transition:0.3s;}")
p.append(".navbar-links a:hover{color:#ff2e2e;}section{padding:120px 10%;text-align:center;}")
p.append("h3{font-size:34px;margin-bottom:40px;color:#ff2e2e;}")
p.append(".arena-section{background:#111;padding:60px;border-radius:15px;margin-bottom:40px;border:1px solid #222;transition:0.3s;}")
p.append(".arena-section:hover{transform:scale(1.02);border-color:#ff2e2e;box-shadow:0 0 30px red;}")
p.append(".btn{padding:15px 40px;border:2px solid #ff2e2e;border-radius:10px;color:white;text-decoration:none;transition:0.3s;font-weight:bold;}")
p.append(".btn:hover{background:#ff2e2e;box-shadow:0 0 30px red;transform:translateY(-5px);}")
p.append(".stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:40px;}")
p.append(".stat{background:#111;padding:40px;border-radius:15px;border:1px solid #222;transition:0.3s;}")
p.append(".stat:hover{transform:scale(1.05);border-color:#ff2e2e;box-shadow:0 0 30px red;}")
p.append(".stat h4{font-size:40px;margin-bottom:10px;color:#ff2e2e;}")
p.append(".grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:30px;}")
p.append(".card{padding:50px;background:#111;border-radius:15px;border:1px solid #222;transition:0.4s;}")
p.append(".card:hover{transform:translateY(-10px) scale(1.05);border-color:#ff2e2e;box-shadow:0 0 30px red;}")
p.append("footer{padding:40px;background:black;color:#666;text-align:center;}")
p.append(".reveal{opacity:0;transform:translateY(40px);transition:1s ease;}.reveal.active{opacity:1;transform:translateY(0);}")
p.append("</style></head><body><canvas id='particles'></canvas>")
p.append("<nav><h1>BLADYSNIADY ARENA</h1><div class='navbar-links'><a href='#home'>Home</a><a href='#stats'>Stats</a>
