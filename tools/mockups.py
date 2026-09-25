# -*- coding: utf-8 -*-
"""Gera og.png (1200x630) e pins (1000x1500) da Carta do Noel fotografando a carta real com Chrome headless.
Rodar de apps/carta-noel: python tools/mockups.py"""
import os, subprocess
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Great+Vibes&family=Nunito:wght@400;700;800;900&display=swap" rel="stylesheet">'
CSS = open(os.path.join(HERE, "letter.css"), encoding="utf-8").read()
LETTER = open(os.path.join(HERE, "letter.html"), encoding="utf-8").read()
PAGE1, PAGE2 = LETTER.split("<!--P2-->")
BASE = """body{margin:0;font-family:Nunito,sans-serif;overflow:hidden}
.bg{position:absolute;inset:0;background:radial-gradient(circle at 30% 20%,#c9333a,#7d161b 70%)}
.snow{position:absolute;inset:0;background-image:radial-gradient(#fff 1.5px,transparent 2px),radial-gradient(#fff 1px,transparent 1.5px);background-size:60px 60px,34px 34px;background-position:0 0,17px 22px;opacity:.35}
.hl{position:absolute;color:#fff;font-weight:900;line-height:1.05;text-shadow:0 3px 12px rgba(0,0,0,.25)}
.hl em{font-family:'Great Vibes',cursive;font-weight:400;font-style:normal;color:#ffe3a3}
.pill{position:absolute;background:#ffe3a3;color:#7d161b;font-weight:900;border-radius:999px;padding:12px 26px}
.shot{position:absolute;transform-origin:top left;box-shadow:0 30px 60px rgba(0,0,0,.35)}"""

def html(w, h, body):
    return f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}\n{BASE}</style></head><body style="width:{w}px;height:{h}px;position:relative">{body}</body></html>'

def shot(name, w, h, body):
    src = os.path.join(HERE, "_" + name + ".html"); out = os.path.join(ROOT, name + ".png")
    open(src, "w", encoding="utf-8").write(html(w, h, body))
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--window-size={w},{h}",
                    "--virtual-time-budget=6000", f"--screenshot={out}", "file:///" + src.replace("\\", "/")], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    os.remove(src); print("ok", out)

def page(html_, x, y, s, rot=0):
    return f'<div class="shot" style="left:{x}px;top:{y}px;transform:rotate({rot}deg) scale({s})">{html_}</div>'

# compartilhamento (WhatsApp/Facebook)
shot("og", 1200, 630, '<div class="bg"></div><div class="snow"></div>'
     '<div class="hl" style="left:60px;top:90px;font-size:62px;width:560px">Carta do <em>Papai Noel</em><br>com o nome do seu filho</div>'
     '<div class="hl" style="left:62px;top:330px;font-size:26px;font-weight:700;width:520px;opacity:.95">Pronta pra imprimir em 1 minuto,<br>com certificado de bom comportamento.</div>'
     '<div class="pill" style="left:60px;top:470px;font-size:26px">Veja a prévia grátis ✨</div>'
     + page(PAGE2, 900, 70, .42, 6) + page(PAGE1, 640, 40, .5, -4))

# pins verticais do Pinterest
PINS = [
    ("pin-carta-personalizada", "Carta do <em>Papai Noel</em><br>personalizada", "com o nome, a idade e as conquistas do ano"),
    ("pin-manha-de-natal", "A carta que o <em>Noel</em><br>deixou na árvore", "pra criança achar na manhã do dia 25 🎄"),
    ("pin-certificado", "Certificado de<br><em>Bom Comportamento</em>", "junto com a resposta do Papai Noel — imprima em casa"),
]
for name, t1, t2 in PINS:
    shot(name, 1000, 1500, '<div class="bg"></div><div class="snow"></div>'
         f'<div class="hl" style="left:60px;top:70px;font-size:76px;width:880px;text-align:center">{t1}</div>'
         f'<div class="hl" style="left:80px;top:300px;font-size:32px;font-weight:700;width:840px;text-align:center">{t2}</div>'
         + (page(PAGE2, 150, 420, .8, -3) if "certificado" in name else page(PAGE1, 160, 400, .84, -2))
         + '<div class="pill" style="left:50%;transform:translateX(-50%);bottom:60px;font-size:34px;white-space:nowrap">Prévia grátis · imprima em casa</div>')
