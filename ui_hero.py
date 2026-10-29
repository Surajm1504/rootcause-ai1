"""UI-only hero section for RootCause AI.

Pure presentation: renders an HTML/CSS/JS hero inside a Streamlit component.
It does not import or call any analysis, storage or integration code.
"""
import streamlit.components.v1 as components

ART_VIDEO = "https://d2ol7oe51mr4n9.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/435a4fe7-e43b-4e7c-af78-0be083e73569.mp4"
ART_STILL = "https://d2ol7oe51mr4n9.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/782a4a52-4c1e-4471-bb0c-aa232927f4a6.webp"

HERO_HTML = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,300..700&family=Inter:wght@300..600&display=swap');
:root{
  --u:.55px; --f:clamp(.55px,.449px + .0284vw,.76px);
  --ink:#fff; --nav:#b9b8bb; --muted:#d3d3d7; --word:#bdbdc1; --ai:#9ff0ec; --kick:#bdf7ee; --logo:#bcbcbf;
  --glass:rgba(255,255,255,.02); --hair:rgba(255,255,255,.16);
  --vio:linear-gradient(135deg,#4d19b1,#6f5adc);
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;background:transparent;overflow:hidden;color:var(--ink);font-family:'Inter',system-ui,sans-serif;font-weight:350;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none;cursor:pointer}
.glass{background:var(--glass);border:1px solid var(--hair);backdrop-filter:blur(8px) brightness(1.15) saturate(.8);-webkit-backdrop-filter:blur(8px) brightness(1.15) saturate(.8);box-shadow:inset 0 0 calc(var(--u)*30) rgba(255,255,255,.035)}
.cv{position:absolute;left:50%;top:0;width:calc(var(--u)*2048);height:calc(var(--u)*1455);transform:translateX(-50%)}
.hdr{position:absolute;left:0;right:0;top:0;height:calc(var(--u)*148);display:flex;align-items:center;padding:0 calc(var(--u)*150)}
.brand{display:flex;align-items:center;gap:calc(var(--u)*18)}
.tile{width:calc(var(--u)*70);height:calc(var(--u)*69);border-radius:calc(var(--u)*17);background:var(--vio);display:grid;place-items:center;font:700 calc(var(--u)*40)/1 'DM Sans',sans-serif;box-shadow:0 0 calc(var(--u)*34) rgba(111,90,220,.55)}
.word{font:500 calc(var(--u)*42)/1 'Inter',sans-serif;color:var(--word);letter-spacing:-.01em;position:relative}
.word sup{position:absolute;right:calc(var(--u)*-6);top:calc(var(--u)*-16);font-size:calc(var(--u)*19);font-weight:600;color:var(--ai);letter-spacing:.04em}
.word{padding-right:calc(var(--u)*34)}
.nav{position:absolute;left:50%;transform:translateX(-50%);display:flex;gap:calc(var(--u)*48);font-size:calc(var(--u)*26);color:var(--nav);white-space:nowrap}
.nav a:hover{color:#fff}
.hr{margin-left:auto;display:flex;align-items:center}
.pill{height:calc(var(--u)*63);padding:0 calc(var(--u)*34);display:flex;align-items:center;border-radius:999px;font-size:calc(var(--u)*26);font-weight:450;color:#fff}
.pill:hover{border-color:rgba(255,255,255,.4)}
.menu{display:none}
.left{position:absolute;left:calc(var(--u)*150);top:calc(var(--u)*290);width:calc(var(--u)*880)}
h1{font-family:'DM Sans',sans-serif;font-weight:380;font-size:calc(var(--u)*104);line-height:calc(var(--u)*122);letter-spacing:-.02em}
h1 .ln{display:block;overflow:hidden;white-space:nowrap}
h1 .ln span{display:inline-block;background:linear-gradient(90deg,#fff 58%,#a7a6ae);-webkit-background-clip:text;background-clip:text;color:transparent;padding-right:.05em}
.sub{margin-top:calc(var(--u)*56);width:calc(var(--u)*760);font-size:calc(var(--u)*29.5);line-height:1.5;color:var(--muted)}
.btns{margin-top:calc(var(--u)*56);display:flex;gap:calc(var(--u)*22)}
.btn{height:calc(var(--u)*85);padding:0 calc(var(--u)*46);border-radius:999px;display:flex;align-items:center;font-size:calc(var(--u)*28);font-weight:500;color:#fff}
.btn.p{background:var(--vio);box-shadow:0 calc(var(--u)*10) calc(var(--u)*40) rgba(95,60,200,.38)}
.btn.g{background:rgba(255,255,255,.05);border:1px solid var(--hair)}
.stats{margin-top:calc(var(--u)*100);display:flex;align-items:center}
.stat{display:flex;align-items:baseline;gap:calc(var(--u)*14);padding:0 calc(var(--u)*34);border-left:1px solid var(--hair)}
.stat:first-child{padding-left:0;border-left:0}
.stat b{font:380 calc(var(--u)*50)/1 'DM Sans',sans-serif}
.stat span{font-size:calc(var(--u)*25);color:var(--nav)}
.artwrap{position:absolute;left:calc(var(--u)*990);top:calc(var(--u)*230);width:calc(var(--u)*1120);height:calc(var(--u)*1120)}
.art{position:absolute;inset:0;-webkit-mask-image:radial-gradient(closest-side,#000 62%,transparent 100%);mask-image:radial-gradient(closest-side,#000 62%,transparent 100%)}
.art>*{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.art .m{opacity:0;transition:opacity .6s}
.art .m.on{opacity:1}
.slab{animation:bob 7s ease-in-out infinite;transform-box:fill-box}
.slab.s1{animation-delay:-1.8s}.slab.s2{animation-delay:-3.6s}.slab.s3{animation-delay:-5.4s}
@keyframes bob{0%,100%{transform:translate(0,0)}50%{transform:translate(8px,-9px)}}
.wave{stroke-dasharray:16 12;animation:flow 3s linear infinite}
@keyframes flow{to{stroke-dashoffset:-56}}
.px{animation:flick 2.4s steps(2,end) infinite}
@keyframes flick{0%,100%{opacity:.15}50%{opacity:.85}}
.card{position:absolute;width:calc(var(--u)*451);height:calc(var(--u)*201);border-radius:calc(var(--u)*18);padding:calc(var(--u)*22);display:flex;gap:calc(var(--u)*20);align-items:flex-start}
.c1{left:calc(var(--u)*10);top:calc(var(--u)*130)}
.c2{left:calc(var(--u)*510);top:calc(var(--u)*780)}
.ico{flex:none;width:calc(var(--u)*63);height:calc(var(--u)*63);border-radius:calc(var(--u)*16);display:grid;place-items:center;background:rgba(159,240,236,.07);border:1px solid rgba(159,240,236,.25)}
.ico svg{width:58%;height:58%}
.kick{font-size:calc(var(--u)*23);color:var(--kick);font-weight:500;letter-spacing:.02em;margin-top:calc(var(--u)*2)}
.ttl{margin-top:calc(var(--u)*10);font-size:calc(var(--u)*29);line-height:1.28;color:#fff;font-weight:450}
.logos{position:absolute;left:0;right:0;top:calc(var(--u)*1345);display:flex;justify-content:center;align-items:center;gap:calc(var(--u)*92);color:var(--logo);font-family:'DM Sans',sans-serif;font-size:calc(var(--u)*34)}
.logos i{font-style:normal}
.logos .a{font-weight:700;letter-spacing:.01em}
.logos .b{font-weight:400;letter-spacing:.18em;text-transform:uppercase;font-size:calc(var(--u)*28)}
@media (prefers-reduced-motion:reduce){.slab,.wave,.px{animation:none}}
/* ---------- smaller screens: one centred column ---------- */
@media (max-width:820px){
  html,body{overflow:auto;height:auto}
  .cv{position:static;transform:none;width:auto;height:auto;padding:0 clamp(16px,5vw,40px) 48px}
  .hdr{position:relative;padding:18px 0;height:auto}
  .tile{width:calc(var(--f)*70);height:calc(var(--f)*69);font-size:calc(var(--f)*40)}
  .word{font-size:calc(var(--f)*42)}.word sup{font-size:calc(var(--f)*19);top:calc(var(--f)*-16)}
  .hr{display:none}
  .menu{display:grid;margin-left:auto;width:42px;height:42px;border-radius:50%;place-items:center;font-size:18px;color:#fff;cursor:pointer}
  .nav{display:none;position:absolute;left:auto;right:0;top:68px;transform:none;flex-direction:column;gap:14px;padding:18px 22px;border-radius:18px;font-size:15px;z-index:5;background:rgba(20,18,28,.88);border:1px solid var(--hair);backdrop-filter:blur(8px)}
  .nav.open{display:flex}
  .left{position:static;width:auto;margin-top:14px;text-align:center}
  h1{font-size:calc(var(--f)*88);line-height:calc(var(--f)*104)}
  h1 .ln{text-align:center}
  .sub{width:auto;margin:calc(var(--f)*34) auto 0;font-size:calc(var(--f)*30);max-width:560px}
  .btns{justify-content:center;margin-top:calc(var(--f)*40);flex-wrap:wrap}
  .btn{height:calc(var(--f)*85);padding:0 calc(var(--f)*46);font-size:calc(var(--f)*28)}
  .stats{justify-content:center;margin-top:calc(var(--f)*56);flex-wrap:wrap;row-gap:10px}
  .stat{padding:0 calc(var(--f)*28);gap:calc(var(--f)*10)}.stat b{font-size:calc(var(--f)*50)}.stat span{font-size:calc(var(--f)*25)}
  .artwrap{position:relative;left:auto;top:auto;width:100%;height:auto;aspect-ratio:1;max-width:620px;margin:calc(var(--f)*30) auto 0}
  .card{width:calc(var(--f)*451);height:auto;min-height:calc(var(--f)*201);padding:calc(var(--f)*22);border-radius:calc(var(--f)*18);gap:calc(var(--f)*18)}
  .c1{left:0;top:4%}.c2{left:auto;right:0;top:auto;bottom:4%}
  .ico{width:calc(var(--f)*63);height:calc(var(--f)*63)}
  .kick{font-size:calc(var(--f)*23)}.ttl{font-size:calc(var(--f)*29)}
  .logos{position:static;flex-wrap:wrap;gap:12px 28px;margin-top:28px;font-size:calc(var(--f)*34)}
  .logos .b{font-size:calc(var(--f)*28)}
}
</style></head>
<body>
<div class="cv" id="cv">
  <header class="hdr">
    <div class="brand" data-a="h"><div class="tile">R</div><div class="word">RootCause<sup>AI</sup></div></div>
    <nav class="nav" id="nav">
      <a data-a="h" data-tab="0">Ranked causes</a><a data-a="h" data-tab="1">Timeline</a><a data-a="h" data-tab="2">Evidence</a>
      <a data-a="h" data-tab="4">Memory</a><a data-a="h" data-tab="5">Graph</a><a data-a="h" data-tab="6">Diagnostics</a>
    </nav>
    <div class="hr"><a class="pill glass" data-a="h" data-go="work">Investigate</a></div>
    <div class="menu glass" id="menu" aria-label="Menu">&#9776;</div>
  </header>

  <section class="left">
    <h1><span class="ln"><span data-a="l">Evidence-linked</span></span><span class="ln"><span data-a="l">root causes you</span></span><span class="ln"><span data-a="l">can verify.</span></span></h1>
    <p class="sub" data-a="s">RootCause AI correlates logs, metrics, traces and change events into ranked, inspectable hypotheses. Read-only analysis, with a human making every decision.</p>
    <div class="btns">
      <a class="btn p" data-a="b" data-go="work">Investigate incident</a>
      <a class="btn g" data-a="b" data-go="modules">Explore modules</a>
    </div>
    <div class="stats">
      <div class="stat" data-a="t"><b>6</b><span>modules</span></div>
      <div class="stat" data-a="t"><b>3</b><span>data sources</span></div>
      <div class="stat" data-a="t"><b>0</b><span>actions executed</span></div>
    </div>
  </section>

  <div class="artwrap">
    <div class="art" id="art">
      <svg id="fallback" viewBox="0 0 1000 1000" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
        <defs>
          <linearGradient id="sg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#9ff0ec"/><stop offset="1" stop-color="#7a5cf0"/></linearGradient>
          <radialGradient id="haze"><stop offset="0" stop-color="#7a5cf0" stop-opacity=".55"/><stop offset="1" stop-color="#7a5cf0" stop-opacity="0"/></radialGradient>
        </defs>
        <g id="slabs"></g>
      </svg>
      <img class="m" id="still" alt="" src="__STILL__" onload="this.classList.add('on')" onerror="this.remove()">
      <video class="m" id="vid" muted loop playsinline autoplay preload="auto" poster="__STILL__" src="__VIDEO__"></video>
    </div>
    <article class="card glass c1" data-a="c"><div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="#9ff0ec" stroke-width="1.6" stroke-linecap="round"><circle cx="5" cy="6" r="2"/><circle cx="19" cy="6" r="2"/><circle cx="12" cy="18" r="2"/><circle cx="12" cy="11" r="1.6"/><path d="M6.8 7l4 3M17.2 7l-4 3M12 12.6V16"/></svg></div><div><div class="kick">Hypotheses</div><div class="ttl">Ranked causes with<br>inspectable evidence.</div></div></article>
    <article class="card glass c2" data-a="c"><div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="#9ff0ec" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7 3v5c0 4.5-3 8-7 10-4-2-7-5.500-7-10V6z"/><rect x="9" y="10.500" width="6" height="5" rx="1"/><path d="M10.500 10.500V9a1.500 1.500 0 013 0v1.500"/></svg></div><div><div class="kick">Read-only</div><div class="ttl">Diagnostic tests,<br>no executed fixes.</div></div></article>
  </div>

  <div class="logos" aria-label="Supported evidence">
    <i class="a" data-a="g" style="font-style:italic">Logs</i><i class="a" data-a="g" style="font-style:italic">Metrics</i><i data-a="g" style="letter-spacing:.14em">Traces</i><i class="a b" data-a="g">Changes</i>
  </div>
</div>

<script>
(function(){
  var root=document.documentElement, rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
  function setU(){var u=Math.max(.468,Math.min(innerHeight/1455,innerWidth/2048*1.12));root.style.setProperty('--u',u+'px');}
  setU(); addEventListener('resize',function(){setU();reportH();});

  /* ----- fallback artwork: four glass slabs, drawn in SVG ----- */
  var NS='http://www.w3.org/2000/svg', g=document.getElementById('slabs'), h='';
  function iso(cy,a,b,s){return [500+(a-b)*s, cy+(a+b-8)*s*.42];}
  for(var i=0;i<4;i++){
    var cy=250+i*170, W=330, H=140, T=28;
    h+='<g class="slab s'+i+'">';
    h+='<polygon points="'+(500-W)+','+cy+' 500,'+(cy+H)+' 500,'+(cy+H+T)+' '+(500-W)+','+(cy+T)+'" fill="rgba(122,92,240,.10)" stroke="url(#sg)" stroke-opacity=".5"/>';
    h+='<polygon points="500,'+(cy+H)+' '+(500+W)+','+cy+' '+(500+W)+','+(cy+T)+' 500,'+(cy+H+T)+'" fill="rgba(159,240,236,.07)" stroke="url(#sg)" stroke-opacity=".5"/>';
    h+='<polygon points="'+(500-W)+','+cy+' 500,'+(cy-H)+' '+(500+W)+','+cy+' 500,'+(cy+H)+'" fill="rgba(255,255,255,.045)" stroke="url(#sg)" stroke-width="1.6" stroke-opacity=".9"/>';
    if(i===0){for(var a=0;a<9;a++)for(var b=0;b<9;b++){var p=iso(cy,a,b,34);h+='<circle cx="'+p[0].toFixed(1)+'" cy="'+p[1].toFixed(1)+'" r="2.6" fill="#9ff0ec" opacity=".7"/>';}
      for(var k=0;k<5;k++){var s0=iso(cy,k*2,0,34),s1=iso(cy,k*2,8,34);h+='<circle r="4.5" fill="#fff"><animateMotion dur="'+(3+k*.6)+'s" repeatCount="indefinite" begin="-'+k+'s" path="M'+s0[0]+' '+s0[1]+' L'+s1[0]+' '+s1[1]+'"/></circle>';}}
    if(i===1){for(var w=1;w<=5;w++){var d='';for(var t=0;t<=16;t++){var aa=t*.5,bb=w*1.3+Math.sin(t*.6+w)*.9,p=iso(cy,Math.min(8,Math.max(0,bb)),aa,34);d+=(t?'L':'M')+p[0].toFixed(1)+' '+p[1].toFixed(1);}h+='<path class="wave" d="'+d+'" fill="none" stroke="url(#sg)" stroke-width="2" style="animation-delay:-'+w*.5+'s"/>';}}
    if(i===2){var sd=7;for(var n=0;n<40;n++){sd=(sd*1103515245+12345)%2147483648;var a2=(sd>>8)%8;sd=(sd*1103515245+12345)%2147483648;var b2=(sd>>8)%8,q=iso(cy,a2+.5,b2+.5,34);h+='<polygon class="px" style="animation-delay:-'+((n*.37)%2.4).toFixed(2)+'s" points="'+q[0]+','+(q[1]-9)+' '+(q[0]+20)+','+q[1]+' '+q[0]+','+(q[1]+9)+' '+(q[0]-20)+','+q[1]+'" fill="#7a5cf0"/>';}}
    if(i===3){h+='<ellipse cx="500" cy="'+cy+'" rx="300" ry="120" fill="url(#haze)"/>';}
    h+='</g>';
  }
  g.innerHTML=h;
  if(rm){try{document.getElementById('fallback').pauseAnimations();}catch(e){}}

  /* ----- artwork loop: video when allowed, still otherwise ----- */
  var v=document.getElementById('vid');
  if(rm){v.remove();}
  else{v.addEventListener('playing',function(){v.classList.add('on');});v.addEventListener('error',function(){v.remove();});
       var pr=v.play(); if(pr&&pr.catch)pr.catch(function(){});}

  /* ----- links: drive the Streamlit page that hosts this hero ----- */
  function P(){try{return window.parent.document;}catch(e){return null;}}
  document.addEventListener('click',function(e){
    var t=e.target.closest('[data-tab],[data-go]'); if(!t)return; var d=P(); if(!d)return;
    if(t.dataset.tab!==undefined){var tabs=d.querySelectorAll('button[role="tab"]'),el=tabs[+t.dataset.tab];if(el){el.click();el.scrollIntoView({behavior:'smooth',block:'center'});}}
    else{var el2=t.dataset.go==='work'?d.getElementById('investigation-workspace'):d.getElementById('rc-modules');if(el2)el2.scrollIntoView({behavior:'smooth',block:'start'});}
    document.getElementById('nav').classList.remove('open');
  });
  document.getElementById('menu').addEventListener('click',function(){document.getElementById('nav').classList.toggle('open');});

  /* ----- one entrance timeline, then static ----- */
  function reportH(){if(matchMedia('(max-width:820px)').matches){window.parent.postMessage({isStreamlitMessage:true,type:'streamlit:setFrameHeight',height:document.documentElement.scrollHeight},'*');}}
  addEventListener('load',reportH); setTimeout(reportH,600);
  if(rm)return;
  function go(sel,start,step,kf,dur){document.querySelectorAll(sel).forEach(function(el,i){el.animate(kf,{duration:dur||750,delay:(start+i*step)*1000,easing:'cubic-bezier(.2,.7,.2,1)',fill:'backwards'});});}
  var rise=[{opacity:0,transform:'translateY(22px)'},{opacity:1,transform:'none'}];
  go('[data-a="h"]',.05,.07,rise);
  go('[data-a="l"]',.35,.12,[{transform:'translateY(105%)'},{transform:'none'}],900);
  go('[data-a="s"]',.85,0,rise);
  go('.btn.g',1.06,0,rise);
  document.querySelector('.btn.p').animate([{opacity:0,transform:'translateY(20px) scale(.985)'},{opacity:1,transform:'none'}],{duration:800,delay:980,easing:'cubic-bezier(.2,.7,.2,1)',fill:'backwards'});
  go('[data-a="t"]',1.2,.1,rise);
  go('[data-a="c"]',1.7,.15,[{opacity:0,transform:'translateY(30px)'},{opacity:1,transform:'none'}],900);
  go('[data-a="g"]',2.0,.08,[{opacity:0},{opacity:1}],700);
})();
</script>
</body></html>'''


def render_hero(height: int = 800) -> None:
    """Render the hero. Purely visual; no data is read or written."""
    html = HERO_HTML.replace("__VIDEO__", ART_VIDEO).replace("__STILL__", ART_STILL)
    components.html(html, height=height, scrolling=False)
