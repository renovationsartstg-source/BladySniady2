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
.arena-section:hover{transform:scale(1.02);border-color:#ff2e2e;box-shadow:0 0 30px red;}
.btn{padding:15px 40px;border:2px solid #ff2e2e;border-radius:10px;color:white;text-decoration:none;transition:0.3s;font-weight:bold;}
.btn:hover{background:#ff2e2e;box-shadow:0 0 30px red;transform:translateY(-5px);}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:40px;}
.stat{background:#111;padding:40px;border-radius:15px;border:1px solid #222;transition:0.3s;}
.stat:hover{transform:scale(1.05);border-color:#ff2e2e;box-shadow:0 0 30px red;}
.stat h4{font-size:40px;margin-bottom:10px;color:#ff2e2e;}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:30px;}
.card{padding:50px;background:#111;border-radius:15px;border:1px solid #222;transition:0.4s;}
.card:hover{transform:translateY(-10px) scale(1.05);border-color:#ff2e2e;box-shadow:0 0 30px red;}
footer{padding:40px;background:black;color:#666;text-align:center;}
.reveal{opacity:0;transform:translateY(40px);transition:1s ease;}
.reveal.active{opacity:1;transform:translateY(0);}
</style>
</head>
<body>
<canvas id="particles"></canvas>
<nav>
<h1>BLADYSNIADY ARENA</h1>
<div class="navbar-links">
<a href="#home">Home</a>
<a href="#stats">Stats</a>
<a href="#games">Games</a>
</div>
</nav>
<section id="home" class="arena-section reveal">
<h3>Welcome to the Arena</h3>
<p>Here you can see all matches, player stats, and live updates!</p>
<br>
<a href="#" class="btn">Enter Arena</a>
</section>
<section id="stats" class="arena-section reveal">
<h3>Player Stats</h3>
<div class="stats">
<div class="stat"><h4>STAT_FOLS</h4><p>Followers</p></div>
<div class="stat"><h4>STAT_WINS</h4><p>Wins</p></div>
<div class="stat"><h4>STAT_HOURS</h4><p>Hours Streamed</p></div>
</div>
</section>
<section id="games" class="arena-section reveal">
<h3>Main Games</h3>
<div class="grid">
<div class="card">Fortnite</div>
<div class="card">Counter-Strike 2</div>
<div class="card">Call of Duty</div>
<div class="card">Metin2</div>
</div>
</section>
<footer>© 2026 Bladysniady | Full Esports Mode</footer>
<script>
window.addEventListener('scroll',()=>{
document.querySelectorAll('.reveal').forEach(el=>{
const top=el.getBoundingClientRect().top;
if(top<window.innerHeight-100){el.classList.add('active');}
});
});
const canvas=document.getElementById('particles');
const ctx=canvas.getContext('2d');
canvas.width=window.innerWidth;
canvas.height=window.innerHeight;
let particles=[];
for(let i=0;i<80;i++){
particles.push({x:Math.random()*canvas.width,y:Math.random()*canvas.height,r:Math.random()*2,d:Math.random()*1});
}
function draw(){
ctx.clearRect(0,0,canvas.width,canvas.height);
ctx.fillStyle="red";
particles.forEach(p=>{
ctx.beginPath();
ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
ctx.fill();
p.y+=p.d;
if(p.y>canvas.height){p.y=0;}
});
requestAnimationFrame(draw);
}
draw();
window.addEventListener('resize',()=>{
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
});
setTimeout(()=>{ window.dispatchEvent(new Event('scroll')); }, 500);
</script>
</body>
</html>
"""

# --- PODMIANA STATYSTYK I KODOWANIE ---
final_html = html_template.replace("STAT_FOLS", st.session_state.fols) \
                          .replace("STAT_WINS", st.session_state.wins) \
                          .replace("STAT_HOURS", st.session_state.hours)

b64_html = base64.b64encode(final_html.encode()).decode()

# --- WYŚWIETLENIE ---
components.html(
    f'<iframe src="data:text/html;base64,{b64_html}" width="100%" height="2000" style="border:none;"></iframe>',
    height=2000
)
