# -*- coding: utf-8 -*-
import os, json, html, re
ROOT = r"C:\Users\ggasp\OneDrive\Desktop\ficar-rico\apps\carta-noel"
BASE = "https://giogas-pm.github.io/carta-noel/"
APP = "/carta-noel/?src=seo"

PAGES = [
  ("resposta-do-papai-noel", "Modelos de resposta do Papai Noel"),
  ("carta-do-papai-noel-para-imprimir", "Carta do Papai Noel para imprimir"),
  ("modelo-de-carta-do-papai-noel", "Modelo de carta para o Papai Noel"),
  ("carta-do-papai-noel-primeiro-natal", "Carta do Papai Noel para bebê"),
  ("certificado-de-bom-comportamento", "Certificado de bom comportamento"),
  ("ideias-magia-do-natal", "Ideias pra manter a magia do Natal"),
]

def L(slug, text=None):
    lab = dict(PAGES)[slug]
    return f'<a href="/carta-noel/{slug}/">{text or lab}</a>'

def modelo(titulo, sub, paras, n):
    body = "".join(f"<p>{p}</p>" for p in paras)
    return f'''<article class="modelo" id="modelo-{n}">
  <div class="mh"><div><h3>{titulo}</h3><span class="sub">{sub}</span></div><button class="copy" type="button">Copiar texto</button></div>
  <div class="txt">{body}</div>
</article>'''

def cta(kind, titulo, texto, botao):
    return f'''<aside class="cta cta-{kind}">
  <p class="ct">{titulo}</p>
  <p>{texto}</p>
  <a class="btn btn-red" href="{APP}" data-cta="{kind}">{botao}</a>
  <p class="price">Prévia grátis na tela · R$9,90 uma vez pra imprimir sem marca d'água · Pix ou cartão</p>
</aside>'''

CSS = """
  :root{--red:#b3262d;--red2:#8f1d22;--green:#1f5e3b;--gold:#c79a3b;--ink:#3b2616;--paper:#fbf4e4;--bg:#fff9f0;--muted:#7b6a5c;--line:#eadfce}
  *{box-sizing:border-box}
  html{-webkit-text-size-adjust:100%}
  body{margin:0;font-family:Nunito,system-ui,sans-serif;background:var(--bg);color:#2a211b;line-height:1.65;font-size:17px}
  a{color:var(--red)}
  header{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:6px;padding:14px 16px;max-width:1100px;margin:0 auto}
  .logo{font-weight:800;font-size:19px;color:var(--red);text-decoration:none}
  .trust{font-size:13px;color:var(--green);font-weight:600}
  .wrap{max-width:780px;margin:0 auto;padding:0 16px}
  .crumbs{font-size:13px;color:var(--muted);margin:4px 0 0}
  .crumbs a{color:var(--muted)}
  h1{font-family:'Cormorant Garamond',serif;font-size:clamp(32px,7vw,48px);line-height:1.08;margin:10px 0 12px}
  h1 em{color:var(--red);font-style:italic}
  .lead{font-size:18px;color:#4a3b30}
  h2{font-family:'Cormorant Garamond',serif;font-size:clamp(26px,5vw,32px);line-height:1.15;margin:38px 0 8px}
  h3{font-size:18px;margin:0}
  .toc{background:#fff;border:1px solid var(--line);border-radius:16px;padding:12px 18px;margin:18px 0;font-size:15.5px}
  .toc b{display:block;margin-bottom:4px}
  .toc ol{margin:0;padding-left:20px}
  .card{background:#fff;border:1px solid var(--line);border-radius:16px;padding:14px 18px;margin:12px 0}
  ul.tips,ol.tips{padding-left:20px}
  ul.tips li,ol.tips li{margin:6px 0}
  .modelo{background:var(--paper);border:1px solid #e3cf9f;border-radius:16px;margin:18px 0;overflow:hidden;box-shadow:0 6px 18px rgba(60,40,20,.07)}
  .mh{display:flex;align-items:flex-start;justify-content:space-between;gap:10px;padding:14px 16px 10px;border-bottom:1px dashed rgba(199,154,59,.7)}
  .mh .sub{font-size:13.5px;color:var(--muted)}
  .copy{flex:none;border:1px solid #dccfbd;background:#fff;border-radius:999px;padding:8px 13px;font:700 13.5px Nunito,sans-serif;cursor:pointer;color:var(--green)}
  .copy.ok{background:var(--green);color:#fff;border-color:var(--green)}
  .txt{padding:12px 18px 6px;color:var(--ink);font:500 19.5px/1.55 'Cormorant Garamond',serif}
  .txt p{margin:0 0 11px}
  .txt p:first-child{font-family:'Great Vibes',cursive;font-size:30px;color:var(--red2);line-height:1.2}
  .btn{display:inline-block;border:0;border-radius:14px;padding:14px 20px;font:800 16px Nunito,sans-serif;cursor:pointer;text-decoration:none;text-align:center}
  .btn-red{background:linear-gradient(180deg,#c9333a,var(--red2));color:#fff;box-shadow:0 8px 18px rgba(179,38,45,.25)}
  .cta{background:#fff;border:2px solid var(--gold);border-radius:18px;padding:18px;margin:26px 0;text-align:center}
  .cta .ct{font-family:'Cormorant Garamond',serif;font-size:25px;font-weight:600;line-height:1.2;margin:0 0 6px;color:var(--ink)}
  .cta p{margin:0 0 12px}
  .cta .btn{width:100%;max-width:420px}
  .cta-top{margin-top:16px}
  .cta-end{background:var(--paper)}
  .price{font-size:13px;color:var(--muted);margin:10px 0 0!important}
  .note{font-size:14.5px;color:var(--muted)}
  .rel{margin:40px 0 10px}
  .rel ul{list-style:none;padding:0;margin:0;display:grid;gap:8px}
  .rel li a{display:block;background:#fff;border:1px solid var(--line);border-radius:12px;padding:11px 14px;text-decoration:none;font-weight:600}
  footer{text-align:center;color:var(--muted);font-size:13px;padding:30px 16px 40px}
  footer nav{display:flex;flex-wrap:wrap;justify-content:center;gap:6px 14px;margin-bottom:10px}
  footer nav a{color:var(--muted)}
  .toast{position:fixed;left:50%;bottom:22px;transform:translateX(-50%);background:#2a211b;color:#fff;padding:10px 16px;border-radius:12px;font-size:14px;opacity:0;transition:.25s;pointer-events:none;z-index:9;max-width:90vw;text-align:center}
  .toast.show{opacity:1}
"""

SCRIPT = """<script>
/* Copiar modelos de texto. Os CTAs são links simples para /carta-noel/?src=seo:
   o próprio app registra o evento seo_land ao abrir, então nada extra é feito aqui. */
(function(){
  var t=document.getElementById('toast');
  function toast(m){t.textContent=m;t.classList.add('show');clearTimeout(toast._t);toast._t=setTimeout(function(){t.classList.remove('show')},3000)}
  function fallback(s){var a=document.createElement('textarea');a.value=s;a.setAttribute('readonly','');a.style.position='fixed';a.style.opacity='0';document.body.appendChild(a);a.select();try{document.execCommand('copy')}catch(_){}document.body.removeChild(a)}
  document.addEventListener('click',function(e){
    var b=e.target.closest&&e.target.closest('.copy');if(!b)return;
    var s=Array.prototype.map.call(b.closest('.modelo').querySelectorAll('.txt p'),function(p){return p.innerText.trim()}).join('\\n\\n');
    var done=function(){b.classList.add('ok');b.textContent='Copiado ✓';toast('Texto copiado! Troque o que está entre [colchetes].');setTimeout(function(){b.classList.remove('ok');b.textContent='Copiar texto'},2500)};
    if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(s).then(done,function(){fallback(s);done()})}else{fallback(s);done()}
  });
})();
</script>"""

def page(slug, title, desc, h1, lead, body, crumb):
    assert len(title) <= 60, (slug, len(title), title)
    assert len(desc) <= 155, (slug, len(desc), desc)
    url = BASE + slug + "/"
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Carta do Noel", "item": BASE},
        {"@type": "ListItem", "position": 2, "name": crumb, "item": url}]}
    rel = "".join(f'<li><a href="/carta-noel/{s}/">{lab}</a></li>' for s, lab in PAGES if s != slug)
    rel += f'<li><a href="{APP}">Criar a carta personalizada do meu filho</a></li>'
    foot = "".join(f'<a href="/carta-noel/{s}/">{lab}</a>' for s, lab in PAGES)
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title, quote=False)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="article">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="pt_BR">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E🎅%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Great+Vibes&family=Nunito:wght@400;600;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<header><a class="logo" href="/carta-noel/">🎅 Carta do Noel</a><span class="trust">✓ dados da criança não saem do seu celular</span></header>
<main class="wrap">
<nav class="crumbs" aria-label="Você está em"><a href="/carta-noel/">Carta do Noel</a> › {crumb}</nav>
<h1>{h1}</h1>
{lead}
{body}
<section class="rel"><h2>Continue lendo</h2><ul>{rel}</ul></section>
</main>
<footer><nav aria-label="Guias de Natal"><a href="/carta-noel/">Carta do Noel (início)</a>{foot}</nav>Carta do Noel · feita com carinho no Brasil · <a href="{APP}">criar a carta do meu filho</a></footer>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
{SCRIPT}
</body>
</html>
"""

from content import CONTENT
counts = {}
for c in CONTENT:
    body = c["body"]
    counts[c["slug"]] = body.count('class="modelo"')
    d = os.path.join(ROOT, c["slug"]); os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(page(c["slug"], c["title"], c["desc"], c["h1"], c["lead"], body, c["crumb"]))
    print(c["slug"], len(c["title"]), len(c["desc"]), "modelos:", counts[c["slug"]], "ctas:", body.count('class="cta '))
