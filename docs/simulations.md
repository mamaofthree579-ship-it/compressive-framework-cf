# Interactive Simulation — Harmonic Compression Visualizer

This interactive demo runs entirely in your browser.  
It demonstrates the simplified compressive-harmonic field used in CF:

\[
\Psi(x,t) = A \cdot \sin(k x - \omega t)\cdot e^{-\alpha x}
\]

Use the sliders to change parameters and observe both the 2D snapshot and a small 3D surface.

<!-- interactive-simulation-start -->
<div id="cf-sim-container" style="max-width:960px;margin:0 auto;">
  <div id="cf-controls" style="display:flex;flex-wrap:wrap;gap:10px;margin-bottom:8px;align-items:center;">
    <label style="font-size:0.9rem;">Amplitude (A)
      <input id="A" type="range" min="0" max="2" step="0.01" value="1" style="vertical-align:middle;">
      <span id="A-val">1.00</span>
    </label>

    <label style="font-size:0.9rem;">Wave number (k)
      <input id="k" type="range" min="0.5" max="4" step="0.01" value="1.256637" style="vertical-align:middle;">
      <span id="k-val">1.2566</span>
    </label>

    <label style="font-size:0.9rem;">Angular freq (ω)
      <input id="w" type="range" min="0.5" max="8" step="0.01" value="2.094395" style="vertical-align:middle;">
      <span id="w-val">2.0944</span>
    </label>

    <label style="font-size:0.9rem;">Damping (α)
      <input id="a" type="range" min="0" max="0.6" step="0.001" value="0.10" style="vertical-align:middle;">
      <span id="a-val">0.10</span>
    </label>

    <button id="export-btn" style="margin-left:8px;padding:6px 10px;">Export PNG</button>
  </div>

  <div id="plots" style="display:grid;grid-template-columns:1fr 380px;gap:10px;">
    <div id="line-plot" style="width:100%;height:380px;background:#fff;border-radius:6px;overflow:hidden;"></div>
    <div id="summary" class="card" style="padding:10px;background:#0f1720;color:#dbefff;border-radius:6px;">
      <h4 style="margin:0 0 8px 0;">Summary</h4>
      <div id="peak-val" style="font-weight:700;">Peak amplitude: —</div>
      <div style="margin-top:10px;color:#9fb0c5;font-size:0.9rem;">Change sliders to explore resonance and damping</div>
      <div style="margin-top:12px;">
        <div style="font-size:0.85rem;color:#9fb0c5;">Snapshot x-range</div>
        <div id="x-range" style="font-weight:600;">0 → 20</div>
      </div>
    </div>
  </div>

  <div id="surface-plot" style="width:100%;height:420px;margin-top:12px;border-radius:6px;overflow:hidden;background:#fff;"></div>
</div>

<!-- Load Plotly from CDN; if blocked it fails gracefully -->
<script src="https://cdn.plot.ly/plotly-2.24.1.min.js"></script>
<script>
// Lightweight CF visualizer (hybrid clean style)
// Default domain & sampling
const xMin = 0, xMax = 20, nX = 600;
const tMin = 0, tMax = 6, nT = 150;

function linspace(a,b,n){ const out=[]; for(let i=0;i<n;i++) out.push(a + (b-a)*i/(n-1)); return out; }
const x = linspace(xMin,xMax,nX);
const t = linspace(tMin,tMax,nT);

// psi function
function psi(xArr, tVal, A, k, w, a){
  const out = new Float64Array(xArr.length);
  for(let i=0;i<xArr.length;i++){
    const xv = xArr[i];
    out[i] = A * Math.sin(k*xv - w*tVal) * Math.exp(-a * xv);
  }
  return out;
}

// UI
const Aui = document.getElementById('A');
const Kui = document.getElementById('k');
const wui = document.getElementById('w');
const aui = document.getElementById('a');
const AVal = document.getElementById('A-val');
const kVal = document.getElementById('k-val');
const wVal = document.getElementById('w-val');
const aVal = document.getElementById('a-val');

function readParams(){
  const A = parseFloat(Aui.value);
  const k = parseFloat(Kui.value);
  const w = parseFloat(wui.value);
  const a = parseFloat(aui.value);
  return {A,k,w,a};
}

function updateLabels(){ const p = readParams(); AVal.textContent = p.A.toFixed(2); kVal.textContent = p.k.toFixed(4); wVal.textContent = p.w.toFixed(4); aVal.textContent = p.a.toFixed(3); }

Aui.addEventListener('input', ()=>{ updateAll(); });
Kui.addEventListener('input', ()=>{ updateAll(); });
wui.addEventListener('input', ()=>{ updateAll(); });
aui.addEventListener('input', ()=>{ updateAll(); });

// Plotly line snapshot and surface
const lineDiv = document.getElementById('line-plot');
const surfaceDiv = document.getElementById('surface-plot');

function drawSnapshot(){
  const {A,k,w,a} = readParams();
  const t0 = t[Math.floor(nT/3)];
  const y = Array.from(psi(x,t0,A,k,w,a));
  const trace = { x: x, y: y, mode:'lines', line:{width:2, color:'#0078d4'} };
  const layout = {
    margin:{l:40,r:12,t:24,b:40}, paper_bgcolor:'#ffffff', plot_bgcolor:'#ffffff',
    xaxis:{title:'x'}, yaxis:{title:'Ψ(x,t)'},
    title:`Snapshot t = ${t0.toFixed(2)}`
  };
  Plotly.react(lineDiv, [trace], layout, {displayModeBar:true});
  // summary stats
  const peak = Math.max(...y.map(Math.abs));
  document.getElementById('peak-val').textContent = 'Peak amplitude: ' + peak.toFixed(4);
}

function drawSurface(){
  const {A,k,w,a} = readParams();
  // build Y matrix (nT × nX) but keep it light: sample fewer t steps for surface
  const tSmall = linspace(tMin,tMax,60);
  const Z = [];
  for(let j=0;j<tSmall.length;j++){
    Z.push(Array.from(psi(x, tSmall[j], A,k,w,a)));
  }
  const data = [{
    z: Z,
    x: x,
    y: tSmall,
    type: 'surface',
    colorscale: 'Viridis',
    cmin: -1, cmax: 1
  }];
  const layout = { margin:{l:40,r:12,t:30,b:40}, scene:{xaxis:{title:'x'}, yaxis:{title:'t'}, zaxis:{title:'Ψ'}}, autosize:true };
  Plotly.react(surfaceDiv, data, layout, {displayModeBar:true});
}

function updateAll(){
  updateLabels();
  drawSnapshot();
  drawSurface();
  document.getElementById('x-range').textContent = `${xMin} → ${xMax}`;
}

// export PNG of the snapshot plot
document.getElementById('export-btn').addEventListener('click', function(){
  Plotly.toImage(lineDiv, {format:'png', width:1600, height:600}).then(function(url){
    const a = document.createElement('a');
    a.href = url; a.download = 'cf_snapshot.png'; document.body.appendChild(a); a.click(); a.remove();
  }).catch(()=> alert('Export failed (Plotly export may be blocked by browser).'));
});

// initial draw and hook
updateAll();
</script>
<!-- interactive-simulation-end -->
