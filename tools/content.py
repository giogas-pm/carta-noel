# -*- coding: utf-8 -*-
APP = "/carta-noel/?src=seo"
LAB = {
  "resposta-do-papai-noel": "modelos de resposta do Papai Noel",
  "carta-do-papai-noel-para-imprimir": "carta do Papai Noel para imprimir",
  "modelo-de-carta-do-papai-noel": "modelo de carta para o Papai Noel",
  "carta-do-papai-noel-primeiro-natal": "carta do Papai Noel para bebê",
  "certificado-de-bom-comportamento": "certificado de bom comportamento",
  "ideias-magia-do-natal": "ideias pra manter a magia do Natal",
}
def L(slug, text=None):
    return f'<a href="/carta-noel/{slug}/">{text or LAB[slug]}</a>'

_n = [0]
def modelo(titulo, sub, paras):
    _n[0] += 1
    body = "".join(f"<p>{p}</p>" for p in paras)
    return f'''<article class="modelo" id="modelo-{_n[0]}">
  <div class="mh"><div><h3>{titulo}</h3><span class="sub">{sub}</span></div><button class="copy" type="button">Copiar texto</button></div>
  <div class="txt">{body}</div>
</article>
'''

def cta(kind, titulo, texto, botao):
    return f'''<aside class="cta cta-{kind}">
  <p class="ct">{titulo}</p>
  <p>{texto}</p>
  <a class="btn btn-red" href="{APP}" data-cta="{kind}">{botao}</a>
  <p class="price">Prévia grátis na tela · R$9,90 uma vez pra imprimir sem marca d'água · Pix ou cartão</p>
</aside>
'''

def reset(): _n[0] = 0

CONTENT = []

# =====================================================================
# 1. RESPOSTA DO PAPAI NOEL
# =====================================================================
reset()
b = cta("top", "Prefere pular a parte de adaptar o texto?",
  "No Carta do Noel você digita o nome do seu filho, o que ele pediu e o que fez de bom no ano, e a resposta sai pronta em pergaminho A4, com certificado de bom comportamento.",
  "Criar a resposta com o nome do meu filho")
b += """
<div class="toc"><b>Modelos nesta página</b><ol>
<li><a href="#modelo-1">Para crianças de 2 a 4 anos</a></li>
<li><a href="#modelo-2">Para crianças de 5 a 7 anos</a></li>
<li><a href="#modelo-3">Para crianças de 8 a 10 anos</a></li>
<li><a href="#modelo-4">Para quem se comportou muito bem</a></li>
<li><a href="#modelo-5">Para quem precisa melhorar (com carinho)</a></li>
<li><a href="#modelo-6">Para quem pediu algo que não vai ganhar</a></li>
<li><a href="#modelo-7">Para irmãos, numa carta só</a></li>
<li><a href="#modelo-8">Para quem teve um ano de muitas mudanças</a></li>
<li><a href="#modelo-9">Natal no calor: o Noel comenta o verão brasileiro</a></li>
</ol></div>

<h2>Como usar estes modelos</h2>
<p>Copie o texto, troque o que está entre [colchetes] e acrescente pelo menos um detalhe que só a sua família sabe: o nome do cachorro, a viagem pra praia, o dente que caiu em outubro. É esse detalhe que faz a criança arregalar o olho e perguntar "como ele sabe disso?". Sem ele, qualquer carta parece genérica, até pra uma criança de cinco anos.</p>
<p>Se for escrever à mão, use uma letra diferente da sua de sempre (ou peça pra outro adulto da casa). Se for imprimir, dá pra montar o texto no editor do celular ou do computador; na página da ${imprimir} tem as dicas de papel e envelope.</p>

<h2>Resposta do Papai Noel por idade</h2>
"""
b = b.replace("${imprimir}", L("carta-do-papai-noel-para-imprimir"))
b += modelo("Para crianças de 2 a 4 anos", "Frases curtas, pra ler em voz alta devagar", [
 "Oi, [Nome]!",
 "Aqui é o Papai Noel. Eu moro bem longe, num lugar cheio de neve, e recebi o seu recado!",
 "Eu sei que você tem [idade] anos e que já sabe fazer um monte de coisas sozinho: [comer sozinho / guardar os brinquedos / dar tchau pros amigos]. Que orgulho!",
 "As minhas renas mandaram um beijo. A mais pequenininha se chama Estrelinha e adora criança que dá abraço apertado.",
 "Na noite de Natal eu vou passar bem de mansinho, enquanto você dorme. Durma bem cedinho, tá bom?",
 "Um abraço bem grandão,<br>Papai Noel",
])
b += modelo("Para crianças de 5 a 7 anos", "A idade em que a magia é mais forte: capriche nos detalhes", [
 "Querido(a) [Nome],",
 "Sua carta chegou aqui no Polo Norte numa terça-feira de muito vento. O duende Bartolomeu, que cuida do correio, entrou correndo na oficina gritando o seu nome. Ele disse que a sua letra (ou o seu desenho!) estava caprichada demais pra esperar.",
 "Li tudo com atenção. Fiquei sabendo que este ano você [aprendeu a ler / começou na escola nova / aprendeu a andar de bicicleta sem rodinha]. Anotei no meu livro grande, aquele de capa vermelha, na página das coisas corajosas.",
 "Sobre o seu pedido, [presente]: os duendes estão trabalhando, e eu vou fazer o possível pra ele caber no trenó. Uma coisa eu garanto: não esqueci de você nem por um dia.",
 "Na noite do dia 24, lembre de deixar a luz de fora acesa. O Rudolfo enxerga bem com o nariz dele, mas ajuda saber qual casa é a sua.",
 "Com carinho e um pouquinho de farelo de biscoito na barba,<br>Papai Noel",
])
b += modelo("Para crianças de 8 a 10 anos", "Mais madura, sem tratar a criança como bebê", [
 "Olá, [Nome],",
 "Você está crescendo, e eu percebo isso pelas cartas. Elas estão mais curtas nos pedidos e mais longas nas perguntas. Gosto disso: quem pergunta muito costuma pensar bem.",
 "Este ano eu reparei em algumas coisas que talvez ninguém tenha comentado com você: [quando você ajudou um colega / quando teve paciência com o irmão menor / quando continuou treinando mesmo perdendo]. Isso é o tipo de coisa que diz quem a pessoa é de verdade.",
 "Você me pediu [presente]. Pedido anotado. E aproveito pra te fazer um pedido também: continue sendo alguém que cuida dos outros. O Natal existe muito por causa de gente assim.",
 "Tem gente que acha que, com [idade] anos, a magia acaba. Eu acho que ela só muda de lugar. Um dia você vai entender o que eu quero dizer, e vai ser uma das pessoas que faz o Natal acontecer para os pequenos.",
 "Até breve,<br>Papai Noel",
])
b += "<h2>Resposta do Papai Noel conforme o ano da criança</h2>\n"
b += modelo("Para quem se comportou muito bem", "Pra celebrar sem exagero, citando conquistas reais", [
 "Querido(a) [Nome],",
 "Tenho uma notícia oficial: o seu nome foi escrito com tinta dourada na Lista dos Bem-Comportados deste ano. Isso não acontece com qualquer um, e os duendes fizeram até uma pequena festa quando viram.",
 "Não foi sorte, não. Foi porque você [dividiu os brinquedos com os primos / ajudou a arrumar a mesa todo dia / estudou para a prova mesmo querendo brincar]. Cada vez que isso acontecia, uma estrelinha acendia no mapa do Polo Norte bem em cima da sua casa.",
 "Continue assim, mas sem pressão: ninguém precisa ser perfeito. O que eu admiro é o esforço de todo dia.",
 "Um abraço orgulhoso,<br>Papai Noel",
 "P.S.: a Mamãe Noel pediu pra dizer que o seu sorriso aparece de longe.",
])
b += modelo("Para quem precisa melhorar (com carinho)", "Sem ameaça e sem \"o Noel não vem\": reconhece o bom e combina o próximo passo", [
 "Querido(a) [Nome],",
 "Recebi sua cartinha e quero te contar uma coisa: eu não tenho lista de crianças más. Tenho só a lista de crianças que ainda estão aprendendo, e todo mundo já esteve nela, até eu, quando era pequeno.",
 "Este ano teve dias difíceis, não teve? Dias de [brigar com o irmão / não querer fazer a lição / responder alto pra mamãe]. Eu sei. E também sei que teve dias lindos, como quando você [exemplo real e positivo].",
 "Então vamos fazer um combinado só nosso: no ano que vem, você tenta [um combinado simples e concreto, como escovar os dentes sem reclamar]. Um só. Eu vou estar torcendo daqui, e os duendes vão marcar cada tentativa, não só os acertos.",
 "O Natal chega pra você do mesmo jeito, porque eu acredito em você.",
 "Com muito carinho,<br>Papai Noel",
])
b += cta("mid", "Quer que o Noel cite as conquistas reais do seu filho?",
  "No app você marca o que ele fez de bom (aprendeu a nadar, largou a chupeta, cuidou do irmão…), escolhe um combinado pro ano que vem e vê a carta montada na hora. A prévia é grátis.",
  "Montar a carta agora")
b += modelo("Para quem pediu algo que não vai ganhar", "Para presentes caros demais, impossíveis ou que a família decidiu não dar", [
 "Querido(a) [Nome],",
 "Li o seu pedido com muita atenção: [presente]. Levei a carta até a oficina e reuni os duendes mais experientes para conversar sobre ele.",
 "Vou ser sincero com você, porque sinceridade é uma regra aqui no Polo Norte: esse presente não vai caber no trenó deste ano. Às vezes é porque ele ainda não é para a sua idade, às vezes porque o trenó tem limite de peso, às vezes porque os duendes acham que existe uma surpresa que vai combinar mais com você agora.",
 "Mas não fique triste. Eu escolhi com cuidado uma coisa que tem muito a ver com o seu jeito, e acho que você vai gostar. E guarde esse sonho: sonhos grandes não somem, eles só esperam a hora certa.",
 "Um abraço de urso polar,<br>Papai Noel",
])
b += modelo("Para irmãos, numa carta só", "Cada criança ganha o seu parágrafo; ninguém é comparado", [
 "Queridos [Nome 1] e [Nome 2],",
 "Desta vez resolvi escrever uma carta só pra vocês dois, porque as cartas chegaram juntinhas, uma grudada na outra, como irmãos de verdade.",
 "[Nome 1], eu vi que este ano você [conquista da criança 1]. Fiquei muito feliz, e a rena Corisco pediu pra te dar os parabéns pessoalmente.",
 "[Nome 2], eu soube que você [conquista da criança 2]. Os duendes ficaram impressionados e colaram um adesivo de estrela no seu nome.",
 "Tenho um pedido para os dois: cuidem um do outro. Irmão é o primeiro amigo que a gente ganha, e dura a vida inteira. Quando um estiver triste, o outro já sabe o que fazer.",
 "Com carinho em dobro,<br>Papai Noel",
])
b += modelo("Para quem teve um ano de muitas mudanças", "Casa nova, escola nova, chegada de um irmãozinho, pais separados", [
 "Querido(a) [Nome],",
 "Este ano foi cheio de novidades pra você, não foi? [Uma casa nova / uma escola nova / um irmãozinho que chegou / duas casas pra morar]. Mudança dá um friozinho na barriga, até nas renas: a Dançarina passou uma semana escondida no celeiro quando trocamos o estábulo de lugar.",
 "Quero que você saiba de duas coisas. A primeira: eu sei direitinho onde você está, então pode ficar tranquilo(a), o trenó vai te achar. A segunda: você foi muito mais corajoso(a) do que imagina.",
 "Os duendes me contaram que, mesmo com tudo diferente, você [fez um amigo novo / ajudou a arrumar as caixas / deu muito carinho ao bebê]. Isso é coisa de gente grande.",
 "Feliz Natal, no seu cantinho novo ou no de sempre.<br>Papai Noel",
])
b += modelo("Natal no calor: o Noel comenta o verão brasileiro", "Divertida, pra criança que pergunta como o Noel aguenta o calor", [
 "Querido(a) [Nome],",
 "Preciso te contar uma coisa: todo ano, quando entro no céu do Brasil, eu tiro o casaco. Isso mesmo! Enquanto aqui no Polo Norte faz 30 graus negativos, aí na sua cidade faz 30 graus positivos, e a minha barba quase derrete.",
 "Por isso tenho um pedido especial: em vez de leite quente, deixe um copo de água geladinha pra mim e uma vasilha de água pras renas. Elas voam a noite inteira e chegam no Brasil com a língua de fora, igual cachorro depois de brincar.",
 "Fiquei sabendo que este ano você [aprendeu a nadar / foi à praia pela primeira vez / fez uma coleção de conchas]. Eu adoraria ter visto!",
 "Até a noite de Natal. Vou chegar de gorro, mas de bermuda por baixo, é segredo.",
 "Papai Noel",
])
b += """
<h2>O que evitar na resposta do Papai Noel</h2>
<ul class="tips">
<li><b>Prometer o que não vai chegar.</b> Se o presente não está garantido, use o modelo de "vou fazer o possível" ou o de presente que não cabe no trenó. Frustração com promessa quebrada pesa mais do que um "não" carinhoso.</li>
<li><b>Usar o Noel como ameaça.</b> "Se não obedecer, o Papai Noel não vem" até funciona por uma semana, mas transforma a magia em castigo. O modelo de quem precisa melhorar mostra outro caminho.</li>
<li><b>Comparar irmãos.</b> Numa carta conjunta, cada um recebe elogio próprio, do mesmo tamanho.</li>
<li><b>Exagerar no texto.</b> Para crianças pequenas, meia página é suficiente. Carta longa demais cansa quem está ouvindo.</li>
<li><b>Esquecer a data e o remetente.</b> "Polo Norte, 24 de dezembro" no topo e a assinatura no fim fazem diferença.</li>
</ul>

<h2>Quando entregar a resposta</h2>
<p>Há dois jeitos que funcionam bem. O primeiro é responder no começo de dezembro, como se o Noel tivesse acabado de receber a cartinha: dá tempo de a criança ler várias vezes e contar pra todo mundo. O segundo é deixar a resposta na manhã do dia 25, junto dos presentes, como prova de que ele passou por ali. Se a criança ainda vai escrever a carta dela, veja os """ + L("modelo-de-carta-do-papai-noel", "modelos de carta pra criança escrever pro Noel") + """. E, se quiser caprichar na entrega, a página de """ + L("ideias-magia-do-natal") + """ tem pegadas, biscoitos e outros truques.</p>
"""
b += cta("end", "A resposta pronta, com o nome dele, em 1 minuto",
  "Os modelos acima são de graça e funcionam. Se você quer uma carta única, com as conquistas do seu filho, o presente que ele pediu e um recado secreto seu, num pergaminho com moldura dourada e selo do Polo Norte, mais o Certificado de Bom Comportamento, o app faz isso na hora. Os dados da criança ficam só no seu aparelho, e há garantia de 7 dias.",
  "Criar a carta do meu filho")
CONTENT.append(dict(slug="resposta-do-papai-noel",
  title="Resposta do Papai Noel: 9 modelos de carta para copiar",
  desc="Modelos grátis de resposta do Papai Noel por idade, pra quem se comportou, pra quem precisa melhorar e pra irmãos. É só copiar e trocar o nome.",
  h1="Resposta do <em>Papai Noel</em>: 9 modelos de carta para copiar",
  lead='<p class="lead">Seu filho escreveu pro Papai Noel e agora está esperando a resposta. Aqui estão 9 cartas completas e diferentes entre si, separadas por idade e pela situação da criança. Copie, troque os detalhes e entregue.</p>',
  crumb="Resposta do Papai Noel", body=b))

# =====================================================================
# 2. PARA IMPRIMIR
# =====================================================================
reset()
b = cta("top", "Quer a carta já diagramada pra imprimir?",
  "O app gera a carta em A4 com moldura dourada, selo do Polo Norte e assinatura do Noel, com o nome e as conquistas do seu filho. É só imprimir ou salvar em PDF.",
  "Gerar a carta pronta pra imprimir")
b += """
<p>Uma carta do Papai Noel impressa numa folha branca comum até funciona, mas alguns cuidados baratos mudam completamente o efeito. Abaixo está o passo a passo que a gente usa, do papel até o jeito de a carta "aparecer" na casa.</p>

<h2>1. Escolha o papel</h2>
<ul class="tips">
<li><b>Sulfite comum (75 g):</b> serve, mas fica fino e transparente. Se for o único que você tem, imprima e passe a carta pro envelope logo, pra não amassar.</li>
<li><b>Sulfite 90 g ou 120 g:</b> já dá outra sensação na mão, e a maioria das impressoras de casa aceita sem problema.</li>
<li><b>Papel pólen ou marfim:</b> é levemente amarelado e fica com cara de carta antiga. Vende em papelaria, por folha ou em bloco.</li>
<li><b>Papel kraft:</b> marrom e rústico, combina com cartas "vindas da oficina". Prefira kraft claro, porque no escuro a tinta preta some.</li>
<li><b>Papel vergê:</b> tem textura de linhas finas, parece papel de carta formal. Ótimo pra um certificado.</li>
</ul>
<p class="note">Truque caseiro de papel envelhecido: passe um saquinho de chá preto frio (bem espremido) sobre a folha já impressa, deixe secar esticada sobre um pano e depois coloque sob livros pesados por algumas horas pra desempenar. Teste antes numa folha de rascunho, porque tinta de jato pode borrar.</p>

<h2>2. Acerte a impressão</h2>
<ol class="tips">
<li>Escolha <b>A4</b> como tamanho de papel e <b>retrato</b> como orientação.</li>
<li>Deixe a escala em <b>100% / tamanho real</b>. "Ajustar à página" costuma encolher o texto e deixar margens tortas.</li>
<li>Se a carta tem moldura ou fundo colorido, ative a opção de <b>imprimir gráficos/cores de fundo</b> do navegador.</li>
<li>Use qualidade <b>normal ou alta</b>, nunca rascunho: o rascunho deixa os dourados acinzentados.</li>
<li>Não tem impressora? Salve em <b>PDF</b> e imprima numa papelaria ou gráfica rápida. Muitas imprimem em papel especial por poucos reais a folha.</li>
</ol>

<h2>3. Monte o envelope</h2>
<p>O envelope é metade da magia. Algumas ideias que não exigem nada além do que você tem em casa:</p>
<ul class="tips">
<li><b>Destinatário completo:</b> "Para: [Nome], [rua e número], [cidade]". Criança adora ver o próprio endereço escrito por outra pessoa.</li>
<li><b>Remetente misterioso:</b> "De: Oficina do Papai Noel, Polo Norte". Quer caprichar? Escreva "Correio dos Duendes, entrega expressa".</li>
<li><b>Selo:</b> desenhe um selo com uma rena ou uma árvore num quadradinho com borda serrilhada. Um adesivo dourado de papelaria vira o "lacre oficial".</li>
<li><b>Carimbo de viagem:</b> um círculo com "Polo Norte, 24 DEZ" feito à caneta, meio torto, parece carimbo de verdade.</li>
<li><b>Sem envelope?</b> Dobre a carta em três, amarre com barbante ou fita vermelha e prenda um raminho da árvore de Natal.</li>
</ul>

<h2>4. A "entrega mágica"</h2>
<p>Onde a carta aparece conta tanto quanto o que está escrito. Opções que funcionam:</p>
<ul class="tips">
<li>Pendurada num galho da árvore de Natal, com prendedor de roupa.</li>
<li>Ao lado do prato de biscoitos (agora só com farelos) na manhã do dia 25.</li>
<li>Presa na janela, como se o Noel tivesse deixado do lado de fora.</li>
<li>Dentro da caixa de correio da casa, com o envelope um pouco amassado "da viagem".</li>
<li>Dentro do sapato ou da meia pendurada, pra quem tem esse costume.</li>
</ul>
<p>Mais ideias pra essa noite estão em """ + L("ideias-magia-do-natal", "como manter a magia do Natal") + """.</p>
"""
b += cta("mid", "Papel bonito pede carta bonita",
  "Em vez de montar a diagramação no Word, gere a carta com o nome do seu filho já no formato A4, com moldura, selo e certificado. Veja a prévia antes de pagar.",
  "Ver a prévia da carta")
b += """
<h2>5 modelos curtos para imprimir</h2>
<p>Estes textos são mais curtos que uma resposta completa e servem pra momentos diferentes do mês de dezembro. Para cartas longas, veja os """ + L("resposta-do-papai-noel", "9 modelos de resposta do Papai Noel") + """.</p>
"""
b += modelo("Aviso de recebimento", "Para o comecinho de dezembro, logo depois que a criança manda a carta", [
 "Olá, [Nome]!",
 "Passando rapidinho pra avisar: sua carta chegou inteira, sem nenhum amassado. O duende do correio carimbou e guardou na gaveta das cartas especiais.",
 "Agora é comigo. Até o Natal!<br>Papai Noel",
])
b += modelo("Obrigado pelos biscoitos", "Para deixar junto do prato vazio na manhã do dia 25", [
 "[Nome],",
 "Os biscoitos estavam uma delícia, comi três e guardei um pro Rudolfo. A água gelada salvou a noite: o Brasil estava muito quente!",
 "Obrigado por lembrar de mim.<br>Papai Noel",
])
b += modelo("Bilhete que acompanha o presente", "Para colar no embrulho do presente principal", [
 "Para [Nome],",
 "Os duendes embrulharam este aqui com um cuidado especial, porque sabiam que era pra você. Espero que traga muita alegria.",
 "Feliz Natal!<br>Papai Noel",
])
b += modelo("Passei por aqui", "Para a criança que queria acordar e ver o Noel", [
 "Oi, [Nome]!",
 "Eu vim, mas você estava num sono tão gostoso que não tive coragem de acordar. Dei uma espiadinha e fui embora na ponta dos pés.",
 "Quem sabe no ano que vem?<br>Papai Noel",
])
b += modelo("Até o ano que vem", "Bilhete de despedida para o fim das festas", [
 "Querido(a) [Nome],",
 "O trenó já voltou pro Polo Norte e as renas estão dormindo. Foi um Natal lindo.",
 "Aproveite as férias, brinque bastante e continue sendo essa criança incrível. Estarei de olho!<br>Papai Noel",
])
b += """
<h2>E o certificado?</h2>
<p>Uma segunda folha com o Certificado de Bom Comportamento completa o kit e costuma ir parar na porta da geladeira. Veja o texto modelo e como usar em """ + L("certificado-de-bom-comportamento", "certificado de bom comportamento do Papai Noel") + """.</p>
"""
b += cta("end", "Pronto pra imprimir em 1 minuto",
  "Nome, idade, o que pediu e o que fez de bom: o Carta do Noel monta a carta única e o certificado, em A4, sem marca d'água depois de liberar. Pagamento único de R$9,90 por Pix ou cartão, e você pode imprimir de novo quantas vezes quiser.",
  "Criar e imprimir a carta")
CONTENT.append(dict(slug="carta-do-papai-noel-para-imprimir",
  title="Carta do Papai Noel para Imprimir: guia e 5 modelos",
  desc="Como imprimir a carta do Papai Noel bonita: papel, configurações, envelope com selo e a entrega mágica. Com 5 modelos curtos prontos para copiar.",
  h1="Carta do <em>Papai Noel</em> para imprimir (e deixar com cara de mágica)",
  lead='<p class="lead">Papel certo, impressão sem margens tortas, envelope com selo do Polo Norte e um lugar surpresa pra carta aparecer. Tudo o que você precisa pra transformar uma folha A4 numa carta que a criança vai guardar.</p>',
  crumb="Carta do Papai Noel para imprimir", body=b))

# =====================================================================
# 3. MODELO DE CARTA (CRIANÇA -> NOEL)
# =====================================================================
reset()
b = cta("top", "A criança já escreveu? Falta a resposta!",
  "Quando a cartinha do seu filho estiver pronta, o Noel pode responder com o nome dele e o que ele pediu. A prévia sai na hora e é grátis.",
  "Criar a resposta do Noel")
b += """
<h2>Como ajudar, de acordo com a idade</h2>
<div class="card"><b>Até 3 anos:</b> a criança ainda não escreve, e tudo bem. Ela desenha, você anota o que ela fala embaixo do desenho, do jeito que ela falou. "Quelo um cachorro de verdade" vale mais do que qualquer frase corrigida.</div>
<div class="card"><b>4 a 6 anos:</b> faça em forma de ditado. Você escreve, ela assina o nome (ou as letras que já conhece) e decora a folha. Pode deixar ela copiar uma palavra só, como "NATAL" ou o próprio nome, em letra grande.</div>
<div class="card"><b>7 anos ou mais:</b> ela escreve sozinha. Seu papel é dar um roteiro (abaixo) e resistir à vontade de corrigir tudo. Erro de ortografia numa carta pro Noel é charme, não problema.</div>

<h2>O roteiro da carta em 6 partes</h2>
<ol class="tips">
<li><b>Saudação:</b> "Querido Papai Noel".</li>
<li><b>Quem sou eu:</b> nome, idade, cidade. O Noel precisa saber pra onde ir.</li>
<li><b>Como foi meu ano:</b> uma ou duas coisas boas que a criança fez ou aprendeu.</li>
<li><b>O pedido:</b> um presente principal, e talvez um segundo "se der". Ajuda a conter a lista infinita.</li>
<li><b>Uma pergunta pro Noel:</b> "Qual é a rena mais rápida?". É isso que a resposta vai poder retomar.</li>
<li><b>Despedida e assinatura:</b> com desenho, se quiser.</li>
</ol>

<h2>6 modelos de carta para a criança escrever ao Papai Noel</h2>
"""
b += modelo("Para quem ainda não escreve (ditado + desenho)", "Você escreve o que a criança disser; os espaços em branco são pra ela desenhar", [
 "Querido Papai Noel,",
 "Meu nome é [Nome] e eu tenho [idade] anos. Eu moro em [cidade] com [quem mora na casa].",
 "Este ano eu aprendi a [o que a criança contar]. Aqui embaixo eu desenhei isso pra você: [espaço para desenho].",
 "Eu queria ganhar [presente, com as palavras da criança].",
 "Beijo,<br>[assinatura ou marca da mão da criança]",
])
b += modelo("De completar as lacunas", "Imprima e deixe a criança preencher as partes em branco", [
 "Querido Papai Noel,",
 "Meu nome é ______________ e eu tenho ____ anos.",
 "A coisa mais legal que eu fiz este ano foi ______________________.",
 "Eu também ajudei em casa quando ______________________.",
 "De presente, eu gostaria de ______________________.",
 "Eu tenho uma pergunta: ______________________ ?",
 "Um abraço de ______________",
])
b += modelo("Criança de 6 a 7 anos", "Frases simples, que ela mesma consegue copiar", [
 "Querido Papai Noel,",
 "Eu sou [Nome], tenho [idade] anos e estou no [ano da escola].",
 "Este ano eu fui bem na escola e aprendi a [ler / fazer conta / amarrar o tênis]. Às vezes eu brigo com [irmão], mas eu estou tentando melhorar.",
 "Eu queria ganhar [presente]. Se não der, pode ser uma surpresa.",
 "Como estão as renas? Qual é a mais rápida?",
 "Beijos,<br>[Nome]",
])
b += modelo("Criança de 9 a 10 anos", "Para quem já escreve bem e gosta de caprichar", [
 "Querido Papai Noel,",
 "Espero que esteja tudo bem aí no Polo Norte e que a oficina não esteja muito corrida. Aqui em [cidade] está um calor enorme, então se quiser tirar o casaco, pode.",
 "Queria te contar que este ano [conquista: passei de ano com notas boas / entrei no time de futsal / aprendi a tocar violão]. Também tentei [algo em que se esforçou], e acho que fui melhorando.",
 "Meu pedido é [presente]. Sei que você tem muitas casas pra visitar, então se não der, eu entendo.",
 "Tenho uma curiosidade: como você consegue passar em todas as casas numa noite só?",
 "Um abraço,<br>[Nome]",
])
b += modelo("Pedindo algo para outra pessoa", "Para a criança que quer um presente pro irmão, os avós ou alguém da família", [
 "Querido Papai Noel,",
 "Meu nome é [Nome]. Este ano eu não quero pedir só pra mim.",
 "Eu queria pedir [algo] para [pessoa], porque [motivo com as palavras da criança: \"a vovó anda triste\", \"meu irmão quebrou o dele\"].",
 "Pra mim, se sobrar espaço no trenó, eu gostaria de [presente].",
 "Obrigado por ler minha carta,<br>[Nome]",
])
b += modelo("Carta de irmãos", "Uma folha, dois ou mais pedidos, todo mundo assina", [
 "Querido Papai Noel,",
 "Nós somos [Nome 1] e [Nome 2] e moramos juntos em [cidade].",
 "[Nome 1] tem [idade] anos e este ano [conquista]. Ele(a) queria ganhar [presente].",
 "[Nome 2] tem [idade] anos e este ano [conquista]. Ele(a) queria ganhar [presente].",
 "A gente promete brigar menos no ano que vem (a gente vai tentar!).",
 "Beijos dos dois,<br>[assinaturas]",
])
b += cta("mid", "Guarde o que ele pediu: o Noel vai responder",
  "Anote o pedido e as coisas boas que a criança contou na carta. No app, esses detalhes entram na resposta do Papai Noel, que sai em pergaminho pronto pra imprimir.",
  "Fazer a resposta do Noel")
b += """
<h2>Onde a criança "envia" a carta</h2>
<p>Cada família tem um ritual. Alguns que funcionam bem: colocar a carta num galho da árvore e fazê-la sumir durante a noite; deixar na janela pro vento "levar"; ou colocar na caixa de correio da casa com um selo desenhado. O importante é que a carta suma de verdade (guarde-a numa pasta, porque ela vira lembrança preciosa daqui a alguns anos) e que a criança perceba que ela foi recebida.</p>

<h2>Depois: a resposta do Papai Noel</h2>
<p>Uma carta enviada pede resposta. Você pode escrever uma a partir dos """ + L("resposta-do-papai-noel", "modelos de resposta do Papai Noel") + """, retomando a pergunta que a criança fez (é o detalhe que mais impressiona). Pra entregar com envelope e selo, veja a """ + L("carta-do-papai-noel-para-imprimir") + """.</p>
"""
b += cta("end", "Seu filho escreveu pro Noel. Agora o Noel responde.",
  "Digite o nome, o que ele pediu e o que fez de bom no ano. O Carta do Noel monta uma resposta única, mais o Certificado de Bom Comportamento, pronta pra imprimir em casa. Os dados não saem do seu aparelho.",
  "Criar a resposta do Papai Noel")
CONTENT.append(dict(slug="modelo-de-carta-do-papai-noel",
  title="Modelo de Carta para o Papai Noel: 6 modelos para crianças",
  desc="Modelos de carta para o Papai Noel pra criança escrever com ajuda dos pais: por idade, de completar lacunas, de irmãos e pedindo para outra pessoa.",
  h1="Modelo de carta para o <em>Papai Noel</em>, pra criança escrever",
  lead='<p class="lead">A carta que a criança manda pro Papai Noel é o começo de tudo e, anos depois, uma das lembranças mais fofas da infância. Aqui estão um roteiro simples e 6 modelos pra ajudar seu filho a escrever, do bebê que só desenha até a criança de 10 anos.</p>',
  crumb="Modelo de carta para o Papai Noel", body=b))

# =====================================================================
# 4. PRIMEIRO NATAL
# =====================================================================
reset()
b = cta("top", "Uma lembrança com o nome do bebê, em pergaminho",
  "No app, coloque o nome do bebê e escreva no recado dos pais o detalhe que vocês querem guardar. A carta do Papai Noel sai em A4, com moldura dourada, pronta pra imprimir e guardar.",
  "Criar a carta do primeiro Natal")
b += """
<h2>Pra que serve uma carta do Papai Noel pra quem ainda não lê?</h2>
<p>Pra quase nada agora, e pra muita coisa daqui a dez anos. A carta do primeiro Natal não é escrita pro bebê de hoje: é pra criança que vai achar essa folha numa caixa de lembranças e descobrir como ela era aos quatro meses, quem estava na ceia, qual era o apelido. É um registro de família com o charme do Polo Norte.</p>

<h2>O que vale a pena registrar</h2>
<ul class="tips">
<li>Idade em meses no Natal, e se já sentava, engatinhava ou dava os primeiros passos.</li>
<li>Apelidos da casa ("Pitoco", "Bolinha", "Nenê").</li>
<li>A primeira risada alta, o primeiro dente, a primeira papinha que amou (ou cuspiu).</li>
<li>Onde e com quem passou o Natal: na casa da avó, na praia, no apartamento pequeno.</li>
<li>O calor que fez, a roupinha de Natal, o presente que mais chamou atenção (normalmente a caixa, não o brinquedo).</li>
</ul>

<h2>4 modelos de carta do Papai Noel para bebê</h2>
"""
b += modelo("Recém-nascido (até 3 meses)", "Para o bebê que chegou pertinho do Natal", [
 "Querido(a) [Nome],",
 "Você chegou ao mundo em [data de nascimento] e, poucas semanas depois, já está vivendo o seu primeiro Natal. Aqui no Polo Norte os duendes acrescentaram uma estrela nova no mapa, bem em cima de [cidade], e ela brilha forte.",
 "Neste Natal você não vai lembrar das luzes nem da ceia. Mas as pessoas ao seu redor vão lembrar de tudo: de você dormindo no colo de [pessoa], do barulhinho que você faz quando está com fome, do tanto que você foi esperado(a).",
 "O meu presente pra você este ano é esta carta. Os seus pais vão guardá-la, e um dia você vai ler e saber que o seu primeiro Natal foi cheio de amor.",
 "Seja bem-vindo(a) ao mundo,<br>Papai Noel",
])
b += modelo("Bebê de 6 a 12 meses", "Para quem já senta, engatinha ou está quase andando", [
 "Querido(a) [Nome],",
 "Os duendes me contaram que você já [senta sozinho(a) / engatinha pela casa inteira / anda segurando nos móveis] e que tem [número] dentinhos. Que velocidade!",
 "Também fiquei sabendo que a sua comida preferida é [papinha] e que você dá a risada mais gostosa do mundo quando [situação]. Aqui na oficina ninguém resistiu e todos riram junto.",
 "Neste Natal, desconfio que você vai se divertir mais com o papel de presente do que com o presente. Tudo bem: eu fazia a mesma coisa.",
 "Feliz primeiro Natal, [apelido]!<br>Papai Noel",
])
b += modelo("Primeiro Natal da família nova", "Para bebês que chegaram por adoção ou para a família que acabou de se formar", [
 "Querido(a) [Nome],",
 "Este é um Natal especial. É o primeiro que você passa com [nomes da família], e eu sei o quanto esse encontro foi desejado.",
 "Cada família tem um jeito de nascer. A de vocês nasceu de muita espera, muito preparo e muito amor, e isso aparece de longe aqui do Polo Norte.",
 "Espero que este seja o primeiro de muitos Natais juntos, com mesa cheia, bagunça na sala e fotos tortas de todo mundo sorrindo.",
 "Com todo o carinho,<br>Papai Noel",
])
b += modelo("Carta para abrir quando crescer", "Estilo cápsula do tempo: lacre o envelope e escreva \"abrir aos 10 anos\"", [
 "Querido(a) [Nome], agora com [idade futura] anos,",
 "Se você está lendo isto, é porque os seus pais guardaram esta carta desde o seu primeiro Natal, em [ano]. Naquele dia você tinha [meses] meses, usava [roupinha] e passou a noite [dormindo no colo de alguém / acordado(a) olhando as luzes].",
 "Naquele ano, todo mundo que estava na [casa / cidade] parou pra olhar pra você. Você era a grande novidade da família.",
 "Não sei do que você gosta hoje, que música ouve, qual é o seu time. Mas sei que foi muito amado(a) desde o primeiro minuto. Isso não muda com o tempo.",
 "Um abraço do passado,<br>Papai Noel",
])
b += cta("mid", "Transforme o texto numa lembrança pra guardar",
  "O app coloca o nome do bebê num pergaminho A4 com moldura, selo e assinatura do Papai Noel. Use o campo de recado dos pais pra incluir um detalhe do primeiro Natal.",
  "Ver a prévia com o nome do bebê")
b += """
<h2>Como guardar a carta do primeiro Natal</h2>
<ul class="tips">
<li><b>Caixa de memórias:</b> junto da pulseirinha da maternidade, da primeira roupinha de Natal e de uma foto impressa da noite.</li>
<li><b>Envelope lacrado:</b> escreva a data de abertura na frente ("abrir no Natal dos 10 anos") e guarde num lugar seco, longe do sol.</li>
<li><b>Com o pezinho:</b> carimbe o pé do bebê com tinta atóxica no verso da carta. Daqui a alguns anos, a diferença de tamanho emociona.</li>
<li><b>Papel que dura:</b> prefira papel mais grosso e sem ácido (vergê ou papel para arquivo) e guarde dentro de uma pasta plástica. As dicas de papel estão na página de """ + L("carta-do-papai-noel-para-imprimir") + """.</li>
<li><b>Uma carta por ano:</b> se virar tradição, no quinto Natal você terá uma pequena coleção contando como a criança cresceu.</li>
</ul>

<h2>E nos próximos Natais</h2>
<p>A partir dos 2 ou 3 anos a criança já entende a brincadeira e a carta passa a ser pra ela. Nessa fase, vale ler os """ + L("resposta-do-papai-noel", "modelos de resposta do Papai Noel por idade") + """ e, quando ela começar a pedir presentes, ajudar com o """ + L("modelo-de-carta-do-papai-noel") + """. Um """ + L("certificado-de-bom-comportamento") + """ também costuma virar sucesso com os pequenos.</p>
"""
b += cta("end", "O primeiro Natal acontece uma vez só",
  "Faça a carta do Papai Noel com o nome do bebê e guarde pra sempre. A prévia é grátis; pra imprimir sem marca d'água são R$9,90, pagamento único, e vem junto o certificado. Nenhum dado do bebê sai do seu aparelho.",
  "Criar a carta do primeiro Natal")
CONTENT.append(dict(slug="carta-do-papai-noel-primeiro-natal",
  title="Carta do Papai Noel para Bebê: textos do Primeiro Natal",
  desc="Textos de carta do Papai Noel para bebê no primeiro Natal: recém-nascido, até 1 ano, família nova e cápsula do tempo. Com dicas de como guardar.",
  h1="Carta do <em>Papai Noel</em> para bebê no primeiro Natal",
  lead='<p class="lead">O bebê não vai ler agora, mas vai adorar ler daqui a alguns anos. Aqui estão 4 textos de carta do Papai Noel pro primeiro Natal, escritos pros pais guardarem como lembrança, e ideias do que registrar antes que a gente esqueça.</p>',
  crumb="Carta do Papai Noel para bebê", body=b))

# =====================================================================
# 5. CERTIFICADO
# =====================================================================
reset()
b = cta("top", "O certificado já vem com a carta",
  "No Carta do Noel, o Certificado de Bom Comportamento sai com o nome da criança e os motivos que você marcou, numa segunda folha A4, junto da carta do Papai Noel.",
  "Criar carta + certificado")
b += """
<h2>O que é o certificado de bom comportamento</h2>
<p>É um "documento oficial" do Polo Norte dizendo que a criança está na Lista dos Bem-Comportados daquele ano. Parece só uma folha a mais, mas pra criança tem peso de diploma: tem nome dela em letra grande, assinatura do Papai Noel e, de preferência, o motivo. Normalmente acompanha a carta-resposta e acaba pendurado na geladeira ou na parede do quarto até o Carnaval.</p>

<h2>Como usar sem virar chantagem</h2>
<p>O certificado funciona melhor como <b>reconhecimento</b> do que como ameaça. Algumas orientações:</p>
<ul class="tips">
<li><b>Cite o motivo concreto.</b> "Por ter largado a chupeta" vale muito mais que "por ter se comportado". A criança entende exatamente o que fez de bom.</li>
<li><b>Não condicione o Natal ao certificado.</b> Evite "se não se comportar, não ganha". O certificado celebra o que já aconteceu.</li>
<li><b>Todo mundo pode ganhar.</b> Em casa com irmãos, cada um recebe o seu, com motivos diferentes. Comparação estraga a festa.</li>
<li><b>Entregue com cerimônia.</b> Leia em voz alta, como se fosse uma formatura. Pode até ter aplauso.</li>
</ul>

<h2>Quando entregar</h2>
<p>Há dois momentos clássicos: <b>na manhã do dia 25</b>, junto da carta e dos presentes, como parte da prova de que o Noel passou; ou <b>no começo de dezembro</b>, como uma "carta de aprovação" que chega antes da noite de Natal e deixa a expectativa lá em cima.</p>

<h2>Textos modelo do certificado</h2>
"""
b += modelo("Certificado clássico", "Serve pra qualquer idade", [
 "Certificado de Bom Comportamento",
 "O Papai Noel e o Conselho dos Duendes do Polo Norte certificam que <b>[Nome]</b> está oficialmente na Lista dos Bem-Comportados do Natal de [ano], por [motivo concreto: ter ajudado em casa e cuidado com carinho do irmãozinho].",
 "Polo Norte, [data].",
 "Papai Noel · Duende Chefe da Oficina",
])
b += modelo("Certificado de conquista especial", "Para um marco do ano: largar a fralda, a chupeta, aprender a ler, a nadar", [
 "Certificado de Coragem e Esforço",
 "Fica registrado no Livro Dourado do Polo Norte que <b>[Nome]</b>, aos [idade] anos, conseguiu [a conquista: largar a chupeta de vez / dormir no próprio quarto / aprender a nadar sem boia].",
 "Por essa conquista, recebe o título de Criança Corajosa do Ano e o direito de contar isso pra quem quiser ouvir.",
 "Assinam: Papai Noel e as Renas do Trenó",
])
b += modelo("Certificado de Ajudante Oficial", "Para irmãos mais velhos ou para quem ajudou muito em casa", [
 "Certificado de Ajudante Oficial do Papai Noel",
 "O Polo Norte reconhece que <b>[Nome]</b> foi um(a) ajudante incrível em [ano], [ajudando a cuidar de (irmão) / colaborando nas tarefas de casa / sendo paciente com os menores].",
 "Com este certificado, [Nome] passa a ser Ajudante Oficial do Papai Noel e pode, no próximo Natal, ajudar a arrumar a árvore e escolher onde fica a estrela.",
 "Papai Noel · Chefe dos Duendes",
])
b += cta("mid", "Carta e certificado com o mesmo nome e os mesmos motivos",
  "Marque no app o que seu filho fez de bom. A carta do Noel comenta essas conquistas e o certificado cita os motivos, os dois no mesmo visual de pergaminho.",
  "Montar carta e certificado")
b += """
<h2>Motivos pra colocar no certificado</h2>
<p>Se estiver sem ideia, escolha um ou dois desta lista, sempre algo que realmente aconteceu:</p>
<ul class="tips">
<li>ajudou a guardar os brinquedos sem precisar pedir duas vezes;</li>
<li>foi corajoso(a) na vacina ou no dentista;</li>
<li>comeu legumes que antes não comia;</li>
<li>emprestou o brinquedo preferido pro primo;</li>
<li>fez amigos na escola nova;</li>
<li>aprendeu a ler, a escrever o nome ou a andar de bicicleta;</li>
<li>cuidou do bichinho de estimação;</li>
<li>pediu desculpas depois de uma briga;</li>
<li>foi paciente com o irmãozinho recém-chegado;</li>
<li>largou a chupeta, a mamadeira ou a fralda.</li>
</ul>

<h2>Como imprimir o certificado</h2>
<p>Use papel mais grosso (180 g ou mais) ou vergê, em A4 na horizontal ou retrato. Uma borda dourada, um selo de adesivo e a assinatura em letra cursiva completam o visual. Se a ideia é emoldurar, uma moldura A4 simples de loja de utilidades resolve. As dicas de papel e impressora estão no guia de """ + L("carta-do-papai-noel-para-imprimir") + """; se quiser ideias de entrega, veja """ + L("ideias-magia-do-natal") + """.</p>
<p>O certificado combina com uma carta-resposta: pegue um dos """ + L("resposta-do-papai-noel", "modelos de resposta do Papai Noel") + """ e entregue os dois juntos.</p>
"""
b += cta("end", "Carta do Noel + Certificado de Bom Comportamento",
  "Em 1 minuto você tem as duas folhas prontas, com o nome do seu filho e as conquistas dele, sem marca d'água depois de liberar. R$9,90 uma vez, por Pix ou cartão, com garantia de 7 dias.",
  "Criar carta e certificado")
CONTENT.append(dict(slug="certificado-de-bom-comportamento",
  title="Certificado de Bom Comportamento do Papai Noel: modelos",
  desc="O que é o certificado de bom comportamento do Papai Noel, como usar sem virar chantagem e 3 textos modelo pra imprimir. Com lista de motivos.",
  h1="Certificado de <em>bom comportamento</em> do Papai Noel",
  lead='<p class="lead">O "diploma" do Polo Norte que toda criança quer pendurar na parede. Veja como usar o certificado de bom comportamento pra celebrar conquistas reais, com 3 textos modelo e uma lista de motivos pra escolher.</p>',
  crumb="Certificado de bom comportamento", body=b))

# =====================================================================
# 6. IDEIAS MAGIA
# =====================================================================
reset()
b = cta("top", "Toda magia precisa de uma prova",
  "A mais forte é uma carta do Papai Noel com o nome da criança e coisas que só ele saberia. O app monta essa carta em 1 minuto.",
  "Criar a carta do Noel")
b += """
<p>A magia do Natal é feita de pequenas provas: um farelo no prato, uma pegada no chão, um bilhete com letra diferente. Nenhuma dessas ideias exige gastar dinheiro, e todas funcionam no calor de dezembro.</p>

<h2>Antes da noite de Natal</h2>
<div class="card"><b>1. A cartinha na árvore.</b> A criança escreve (ou desenha) o pedido e pendura num galho. Uma noite, a carta desaparece: foi recolhida pelos duendes. Tem roteiro e modelos em """ + L("modelo-de-carta-do-papai-noel") + """.</div>
<div class="card"><b>2. O aviso de recebimento.</b> Alguns dias depois, chega um bilhete do Noel dizendo que a carta chegou bem. É o tipo de detalhe que prolonga a expectativa por semanas.</div>
<div class="card"><b>3. O duende visitante.</b> Um bonequinho de duende "chega" no começo de dezembro e, toda manhã, aparece num lugar diferente da casa: em cima da geladeira, dentro da fruteira, lendo um livro. A regra da brincadeira: se tocar, ele perde a magia. Dá trabalho só pros adultos lembrarem de mudar ele de lugar.</div>
<div class="card"><b>4. Calendário de contagem regressiva.</b> Envelopes numerados de 1 a 24 com pequenas tarefas ("fazer um desenho pro vovô", "dançar uma música de Natal") em vez de doces. Mantém o clima o mês inteiro.</div>

<h2>Na noite do dia 24</h2>
<div class="card"><b>5. Biscoitos e água gelada.</b> No Brasil, faz mais sentido deixar água gelada do que leite quente. Um biscoito mordido pela metade e farelos no prato são a prova mais clássica que existe.</div>
<div class="card"><b>6. Cenoura pras renas.</b> Deixe algumas cenouras no quintal, na varanda ou na janela. De manhã, apareçam só os cabinhos, meio roídos.</div>
<div class="card"><b>7. Pegadas de bota.</b> Recorte o formato de uma sola de bota grande num papelão, apoie no chão e polvilhe farinha de trigo ou talco em volta. Ao tirar o molde, fica a pegada perfeita, da porta até a árvore. Uma trilha de 4 ou 5 passos já impressiona.</div>
<div class="card"><b>8. Chave mágica.</b> Pra quem mora em apartamento ou em casa sem chaminé: uma chave velha com uma fita vermelha, pendurada na porta, "para o Noel conseguir entrar". Criança pequena adora ter essa pergunta resolvida.</div>
<div class="card"><b>9. Rastreando o trenó.</b> Todo ano, na noite do dia 24, o NORAD (um comando de defesa aérea dos Estados Unidos e do Canadá) mantém um site que "acompanha" a viagem do Papai Noel pelo mundo, com mapa e tudo. Olhar o trenó passando pelo Brasil antes de dormir ajuda muito na hora de ir pra cama.</div>
<div class="card"><b>10. O sininho.</b> Quando a criança já estiver deitada, um adulto toca um sino (ou um chaveiro de guizo) do lado de fora da janela. Depois, silêncio total. Ninguém esquece.</div>
"""
b += cta("mid", "A carta que o Noel deixa ao lado dos biscoitos",
  "Coloque o nome do seu filho, o que ele pediu e o que fez de bom no ano. A carta sai em pergaminho, com certificado, pronta pra aparecer na manhã do dia 25. Veja a prévia grátis.",
  "Ver a carta com o nome dele")
b += """
<h2>Na manhã do dia 25</h2>
<div class="card"><b>11. A carta-resposta.</b> Um envelope com o nome da criança, deixado ao lado do prato vazio ou pendurado na árvore. Se precisar de texto, há 9 opções em """ + L("resposta-do-papai-noel", "modelos de resposta do Papai Noel") + """; pra deixar bonita, veja """ + L("carta-do-papai-noel-para-imprimir", "como imprimir a carta do Papai Noel") + """.</div>
<div class="card"><b>12. O certificado.</b> Uma folha "oficial" dizendo que a criança está na Lista dos Bem-Comportados, com o motivo. Textos prontos em """ + L("certificado-de-bom-comportamento") + """.</div>
<div class="card"><b>13. Embrulho do Polo Norte.</b> Os presentes "do Noel" vêm num papel que não existe em casa (e que os pais nunca usam nos próprios presentes). Detalhe pequeno que evita perguntas incômodas.</div>
<div class="card"><b>14. Rastro de pó mágico.</b> Um pouco de purpurina biodegradável ou papel picado dourado perto da janela por onde o Noel entrou. Evite deixar fora de casa, pra não fazer mal aos passarinhos.</div>
<div class="card"><b>15. O bilhete esquecido.</b> Um recado curto do Noel "esquecido" no sofá, reclamando do calor: "Vocês não têm ventilador no Polo Norte, sabia?". Criança brasileira acha graça demais.</div>

<h2>Se for o primeiro Natal do bebê</h2>
<p>Ele não vai lembrar, mas vocês vão. Em vez de pegadas e biscoitos, vale registrar o momento numa carta pra guardar. Veja textos na página de """ + L("carta-do-papai-noel-primeiro-natal") + """.</p>

<h2>E quando a criança começa a desconfiar?</h2>
<p>Geralmente acontece entre os 7 e os 9 anos, e não precisa ser um drama. Muitas famílias devolvem a pergunta ("e você, o que acha?") e deixam a criança chegar à própria conclusão. Quando ela descobre, dá pra transformar isso em promoção: ela passa a ser "ajudante do Noel" e participa da magia dos irmãos menores. É um jeito bonito de a brincadeira continuar em vez de acabar.</p>
"""
b += cta("end", "Feche a noite com a prova mais forte de todas",
  "Uma carta do Papai Noel que fala o nome do seu filho, lembra o que ele fez de bom no ano e responde ao pedido dele. Pronta em 1 minuto, em A4, com Certificado de Bom Comportamento. R$9,90 uma vez, com garantia de 7 dias.",
  "Criar a carta do meu filho")
CONTENT.append(dict(slug="ideias-magia-do-natal",
  title="Ideias para Manter a Magia do Natal: 15 truques em casa",
  desc="15 ideias simples pra manter a magia do Natal: pegadas de bota, biscoitos, carta na árvore, rastreador do trenó, duende visitante e mais.",
  h1="Ideias pra manter a <em>magia do Natal</em>: 15 truques simples",
  lead='<p class="lead">Pegadas de bota com farinha, biscoito mordido, sininho na janela e uma carta do Noel esperando de manhã. Ideias baratas, testadas por famílias brasileiras, e adaptadas pro Natal de verão.</p>',
  crumb="Ideias pra manter a magia do Natal", body=b))
