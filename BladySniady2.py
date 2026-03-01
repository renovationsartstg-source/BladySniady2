import streamlit as st
import sqlite3
import time
import hashlib

# 1. SETUP
st.set_page_config(page_title="BladySniady | Arena", layout="wide")

# 2. DATABASE (Używamy st.cache_resource, żeby nie otwierać połączenia co sekundę)
@st.cache_resource
def get_connection():
    conn = sqlite3.connect("arena.db", check_same_thread=False)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, watch_time INTEGER DEFAULT 0, rank TEXT DEFAULT 'REKRUT')")
    conn.commit()
    return conn

conn = get_connection()
c = conn.cursor()

# 3. RANK SYSTEM
RANKS = [
    (0, "REKRUT"), (60, "WIDZ"), (300, "ELITA"), 
    (900, "WETERAN"), (1800, "LEGENDARNY"), (3600, "ARENA MASTER")
]

def get_rank(seconds):
    current = "REKRUT"
    for threshold, name in RANKS:
        if seconds >= threshold: current = name
    return current

# 4. SESSION INIT
if "user" not in st.session_state: st.session_state.user = None
if "last_update" not in st.session_state: st.session_state.last_update = time.time()

# 5. AUTH FUNCTIONS
def hash_pass(password): return hashlib.sha256(password.encode()).hexdigest()

def register(u, p):
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (u, hash_pass(p)))
        conn.commit()
        return True
    except: return False

def login(u, p):
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (u, hash_pass(p)))
    return c.fetchone()

# 6. UI LOGIC
if not st.session_state.user:
    st.title("🛡️ BLADY SNIADY ARENA")
    t1, t2 = st.tabs(["Zaloguj", "Rejestracja"])
    with t1:
        u_l = st.text_input("Username")
        p_l = st.text_input("Password", type="password")
        if st.button("WEJDŹ DO GRY"):
            res = login(u_l, p_l)
            if res:
                st.session_state.user = u_l
                st.session_state.last_update = time.time()
                st.rerun()
            else: st.error("Błędne dane")
    with t2:
        u_r = st.text_input("Nowy Nick")
        p_r = st.text_input("Hasło", type="password")
        if st.button("STWÓRZ PROFIL"):
            if register(u_r, p_r): st.success("Konto utworzone!")
            else: st.error("Nick zajęty")

else:
    # AKTUALIZACJA CZASU (Tylko przy interakcji, bez pętli rerun)
    user = st.session_state.user
    now = time.time()
    delta = int(now - st.session_state.last_update)
    
    c.execute("SELECT watch_time, rank FROM users WHERE username=?", (user,))
    data = c.fetchone()
    current_time = data[0] + delta
    new_rank = get_rank(current_time)
    
    # Zapis i odświeżenie sesji
    c.execute("UPDATE users SET watch_time=?, rank=? WHERE username=?", (current_time, new_rank, user))
    conn.commit()
    st.session_state.last_update = now

    # UI ARENY
    st.title(f"Witaj w Arenie, {user}! ⚔️")
    col_main, col_side = st.columns([3, 1])

    with col_main:
        # TWITCH PLAYER (Poprawiony parent)
        # UWAGA: parent musi zawierać domenę Twojej apki (np. bladysniady.streamlit.app)
        parent = "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"
        st.markdown(f"""
        <iframe src="https://player.twitch.tv/?channel=bladysniady&parent={parent}" 
        height="600" width="100%" allowfullscreen="true"></iframe>
        """, unsafe_allow_html=True)
        
        st.info("Czas nalicza się przy każdym odświeżeniu strony lub kliknięciu przycisku.")

    with col_side:
        st.metric("Twoja Ranga", new_rank)
        st.metric("Czas w Arenie", f"{current_time // 60} min")
        
        if st.button("Odśwież Rangę"): st.rerun()
        
        st.markdown("---")
        st.subheader("🏆 TOP 10 ARENY")
        c.execute("SELECT username, watch_time, rank FROM users ORDER BY watch_time DESC LIMIT 10")
        for i, (u, t, r) in enumerate(c.fetchall(), 1):
            st.write(f"{i}. **{u}** - {t//60}m ({r})")

        if st.button("Wyloguj"):
            st.session_state.user = None
            st.rerun()
