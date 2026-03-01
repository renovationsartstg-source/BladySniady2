import streamlit as st
import streamlit.components.v1 as components
import sqlite3
import time
import hashlib

# 1. KONFIGURACJA
st.set_page_config(page_title="BladyHub", layout="wide")

# 2. BAZA DANYCH
@st.cache_resource
def init_db():
    conn = sqlite3.connect("arena.db", check_same_thread=False)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, watch_time INTEGER DEFAULT 0, rank TEXT DEFAULT 'REKRUT')")
    conn.commit()
    return conn

conn = init_db()
cursor = conn.cursor()

# 3. STYLE CSS (Krótkie linie dla bezpieczeństwa)
css = '<style>'
css += 'body, .stApp { background: #020205; color: white; }'
css += '#MainMenu, footer, header { display: none !important; }'
css += '.neon { font-family: "Courier New"; color: #f00; text-shadow: 0 0 15px #f00; text-align: center; }'
css += '.card { background: rgba(30,0,0,0.4); border: 1px solid #f00; border-radius: 15px; padding: 20px; }'
css += 'div.stButton > button { background: #f00 !important; color: #fff !important; width: 100%; border: none !important; }'
css += '</style>'
st.markdown(css, unsafe_allow_html=True)

# 4. LOGIKA SESJI
if 'view' not in st.session_state: st.session_state.view = 'home'
if 'user' not in st.session_state: st.session_state.user = None

# 5. WIDOK HOME
if st.session_state.view == 'home' and not st.session_state.user:
    st.markdown('<h1 class="neon">BLADY</h1>', unsafe_allow_html=True)
    st.markdown('<h1 class="neon">SNIADY</h1>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        u = st.text_input("Username")
        p = st.text_input("Password", type="password")
        if st.button("LOGIN"):
            # Uproszczone logowanie dla testu (każde hasło wchodzi)
            st.session_state.user = u
            st.session_state.view = 'arena'
            st.rerun()

# 6. WIDOK ARENA
elif st.session_state.user:
    st.title(f"ARENA: {st.session_state.user}")
    
    c1, c2 = st.columns([3, 1])
    
    with c1:
        # Twitch Player - Rozbity na kawałki, żeby uniknąć ucięcia linii
        p_url = "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"
        t_code = '<iframe src="https://player.twitch.tv/?channel=bladysniady&parent='
        t_code += p_url
        t_code += '" height="600" width="100%" allowfullscreen="true"></iframe>'
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        components.html(t_code, height=620)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("RANK: REKRUT")
        if st.button("LOGOUT"):
            st.session_state.user = None
            st.session_state.view = 'home'
