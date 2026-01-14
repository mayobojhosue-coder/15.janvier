from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Joyeux anniversaire Méléa</title>

<style>
body{
    margin:0;
    background: linear-gradient(135deg,#fff0f6,#f5f0ff);
    font-family: "Georgia", serif;
    display:flex;
    justify-content:center;
    align-items:center;
    min-height:100vh;
    overflow:hidden;
}

.heart{
    position:absolute;
    color:#ff6fa5;
    font-size:20px;
    animation: float 8s linear infinite;
    opacity:0.6;
}

@keyframes float{
    0%{transform:translateY(100vh); opacity:0;}
    10%{opacity:1;}
    100%{transform:translateY(-10vh); opacity:0;}
}

.card{
    background:white;
    max-width:700px;
    padding:40px;
    border-radius:25px;
    box-shadow:0 15px 40px rgba(0,0,0,0.15);
    text-align:center;
    animation: appear 2s ease;
    z-index:2;
}

@keyframes appear{
    from{opacity:0; transform:scale(0.8);}
    to{opacity:1; transform:scale(1);}
}

h1{
    color:#c27ba0;
    font-size:40px;
    animation: glow 3s infinite alternate;
}

@keyframes glow{
    from{text-shadow:0 0 5px #f2a1c7;}
    to{text-shadow:0 0 20px #ff8fcf;}
}

.subtitle{
    color:#777;
    font-style:italic;
    margin-bottom:20px;
}

.poem{
    font-size:18px;
    color:#333;
    line-height:1.8;
    white-space:pre-line;
}

.music-btn{
    margin-top:20px;
    padding:10px 25px;
    border:none;
    border-radius:30px;
    background:#ff8fcf;
    color:white;
    font-size:16px;
    cursor:pointer;
}
</style>
</head>

<body>

<div class="card">

<h1>🎂 Joyeux anniversaire Méléa 🎂</h1>

<div class="subtitle">
Que cette journée soit aussi belle que ton âme ✨
</div>

<div class="poem">
Méléa,

Tu es une lumière douce dans notre église,
Une force tranquille, un esprit paisible.
Tu avances avec grâce,
Portée par l’amour de Dieu et la beauté de ton cœur.

Tu es jolie, mais surtout belle à l’intérieur,
Forte sans être dure,
Douce sans être faible,
Et remplie d’une foi qui inspire.

Même si nous ne sommes pas très proches,
Je te souhaite sincèrement
Une année remplie de paix,
De sourires, de bénédictions et d’amour.

Que Dieu éclaire ton chemin,
Qu’Il protège ton cœur,
Et qu’Il fasse briller ta vie
Encore plus fort chaque jour.

Joyeux anniversaire, Méléa 🌸
</div>

<button class="music-btn" onclick="playMusic()">🎵 Activer la musique</button>

</div>

<audio id="bgMusic" loop>
<source src="https://cdn.pixabay.com/download/audio/2022/03/15/audio_7c61c6e7c3.mp3?filename=soft-piano-ambient-11157.mp3" type="audio/mpeg">
</audio>

<script>
function playMusic(){
    document.getElementById("bgMusic").play();
}

function createHeart(){
    const heart=document.createElement("div");
    heart.className="heart";
    heart.innerHTML="❤";
    heart.style.left=Math.random()*100+"vw";
    heart.style.fontSize=(15+Math.random()*20)+"px";
    heart.style.animationDuration=(6+Math.random()*5)+"s";
    document.body.appendChild(heart);
    setTimeout(()=>heart.remove(),9000);
}
setInterval(createHeart,400);
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
