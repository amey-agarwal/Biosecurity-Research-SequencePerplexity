# Biosecurity Research - Sequence Perplexity Project

---

**Can the Bio model give low likelihood scores of sequence relevance to the training composition?**

If gene sequence has LOW NATURAL PLAUSABILTY but HIGH FUNCTIONALITY, then it could be ```engineered``` (and potentially harmful). 

> Themes: Biosecurity risk; AI safety

---

# Results

<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Perplexity Pilot Results</title>
<meta name="description" content="Final quality-controlled comparison of natural vs. engineered sequence perplexity for a genome language model — no detectable difference, with Welch's t-test and Cohen's d.">
<style>
.viz-root {
  color-scheme: light;
  --surface-1: #fcfcfb;
  --page: #f9f9f7;
  --text-primary: #0b0b0b;
  --text-secondary: #52514e;
  --text-muted: #898781;
  --grid: #e1e0d9;
  --axis: #c3c2b7;
  --series-1: #2a78d6;
  --series-2: #eb6834;
  --border: rgba(11,11,11,0.10);
}
@media (prefers-color-scheme: dark) {
  :root:where(:not([data-theme="light"])) .viz-root {
    color-scheme: dark;
    --surface-1: #1a1a19;
    --page: #0d0d0d;
    --text-primary: #ffffff;
    --text-secondary: #c3c2b7;
    --text-muted: #898781;
    --grid: #2c2c2a;
    --axis: #383835;
    --series-1: #3987e5;
    --series-2: #d95926;
    --border: rgba(255,255,255,0.10);
  }
}
:root[data-theme="dark"] .viz-root {
  color-scheme: dark;
  --surface-1: #1a1a19;
  --page: #0d0d0d;
  --text-primary: #ffffff;
  --text-secondary: #c3c2b7;
  --text-muted: #898781;
  --grid: #2c2c2a;
  --axis: #383835;
  --series-1: #3987e5;
  --series-2: #d95926;
  --border: rgba(255,255,255,0.10);
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--page); }
.viz-root {
  background: var(--page);
  color: var(--text-primary);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  padding: 28px 20px 40px;
  max-width: 720px;
  margin: 0 auto;
}
h1 { font-size: 20px; margin: 0 0 4px; }
.sub { color: var(--text-secondary); font-size: 13px; margin: 0 0 20px; line-height: 1.5; }
.card {
  background: var(--surface-1);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 18px 18px 8px;
  overflow-x: auto;
}
.legend { display: flex; gap: 20px; align-items: center; font-size: 12px; color: var(--text-secondary); margin: 4px 0 14px; flex-wrap: wrap; }
.legend .dot { display: inline-block; width: 10px; height: 10px; border-radius: 50%; margin-right: 6px; vertical-align: -1px; }
svg { display: block; width: 100%; height: auto; }
.axis-label { fill: var(--text-muted); font-size: 11px; }
.tick-label { fill: var(--text-muted); font-size: 10px; }
.row-label { fill: var(--text-primary); font-size: 12px; font-weight: 600; }
.grid-line { stroke: var(--grid); stroke-width: 1; }
.axis-line { stroke: var(--axis); stroke-width: 1; }
.pt { cursor: pointer; }
.mean-tick { stroke-width: 2; }
.stats { display: flex; gap: 18px; flex-wrap: wrap; font-size: 12.5px; color: var(--text-secondary); margin: 2px 0 16px; font-variant-numeric: tabular-nums; }
.stats b { color: var(--text-primary); }
.callout {
  margin-top: 18px;
  padding: 14px 16px;
  border-radius: 10px;
  background: color-mix(in srgb, var(--series-1) 10%, var(--surface-1));
  border: 1px solid var(--border);
  font-size: 13px;
  line-height: 1.55;
  color: var(--text-primary);
}
.callout b { color: var(--text-primary); }
table { border-collapse: collapse; width: 100%; margin-top: 22px; font-size: 12.5px; }
th, td { text-align: left; padding: 6px 10px; border-bottom: 1px solid var(--grid); }
th { color: var(--text-muted); font-weight: 600; font-size: 11px; text-transform: uppercase; letter-spacing: 0.02em; }
td.num { font-variant-numeric: tabular-nums; text-align: right; }
.flag { color: var(--text-muted); font-size: 11px; }
</style>
</head>
<body>
<div class="viz-root">
  <h1>Final pilot scores: engineered vs. natural sequences</h1>

  <div class="card">
    <div class="legend">
      <span><span class="dot" style="background:var(--series-1)"></span>Natural (E. coli CDS, n=8)</span>
      <span><span class="dot" style="background:var(--series-2)"></span>Engineered (iGEM "Works" parts, n=7)</span>
    </div>
    <div class="stats">
      <span>Welch's <b>t = -0.07</b></span>
      <span><b>p = 0.95</b> (no detectable difference)</span>
      <span>Cohen's <b>d = -0.03</b> (negligible)</span>
    </div>

    <svg viewBox="0 0 640 240" role="img" aria-label="Strip plot of perplexity scores for fully quality-controlled natural and engineered sequences">
      <line class="grid-line" x1="80" y1="40" x2="80" y2="210"></line>
      <line class="grid-line" x1="272" y1="40" x2="272" y2="210"></line>
      <line class="grid-line" x1="464" y1="40" x2="464" y2="210"></line>
      <text class="tick-label" x="80" y="225" text-anchor="middle">-9.5</text>
      <text class="tick-label" x="272" y="225" text-anchor="middle">-8.5</text>
      <text class="tick-label" x="464" y="225" text-anchor="middle">-7.5</text>
      <text class="axis-label" x="320" y="238" text-anchor="middle">score (higher = lower perplexity) →</text>

      <line class="axis-line" x1="80" y1="210" x2="560" y2="210"></line>

      <text class="row-label" x="8" y="104">Natural</text>
      <text class="row-label" x="8" y="174">Engineered</text>

      <circle class="pt" cx="164.5" cy="100" r="6" fill="var(--series-1)"><title>WP_001517211.1: -9.060</title></circle>
      <circle class="pt" cx="250.1" cy="92" r="6" fill="var(--series-1)"><title>WP_001287824.1: -8.614</title></circle>
      <circle class="pt" cx="263.4" cy="108" r="6" fill="var(--series-1)"><title>WP_024203168.1: -8.545</title></circle>
      <circle class="pt" cx="342.3" cy="92" r="6" fill="var(--series-1)"><title>WP_001517860.1: -8.134</title></circle>
      <circle class="pt" cx="375.1" cy="108" r="6" fill="var(--series-1)"><title>WP_001024536.1: -7.963</title></circle>
      <circle class="pt" cx="407.0" cy="92" r="6" fill="var(--series-1)"><title>WP_182294302.1: -7.797</title></circle>
      <circle class="pt" cx="411.2" cy="108" r="6" fill="var(--series-1)"><title>WP_498087657.1: -7.775</title></circle>
      <circle class="pt" cx="476.5" cy="100" r="6" fill="var(--series-1)"><title>WP_498087655.1: -7.435</title></circle>
      <line class="mean-tick" x1="336.3" y1="86" x2="336.3" y2="114" stroke="var(--series-1)"></line>
      <text class="tick-label" x="336.3" y="80" text-anchor="middle">mean</text>

      <circle class="pt" cx="267.8" cy="162" r="6" fill="var(--series-2)"><title>BFP: -8.522</title></circle>
      <circle class="pt" cx="280.6" cy="178" r="6" fill="var(--series-2)"><title>SYFP2: -8.455</title></circle>
      <circle class="pt" cx="311.6" cy="162" r="6" fill="var(--series-2)"><title>BBa_K1590009: -8.294</title></circle>
      <circle class="pt" cx="323.1" cy="178" r="6" fill="var(--series-2)"><title>YFP: -8.234</title></circle>
      <circle class="pt" cx="334.6" cy="170" r="6" fill="var(--series-2)"><title>BBa_K1680009: -8.174</title></circle>
      <circle class="pt" cx="382.4" cy="170" r="6" fill="var(--series-2)"><title>cheZ: -7.925</title></circle>
      <circle class="pt" cx="474.2" cy="170" r="6" fill="var(--series-2)"><title>eyfp: -7.447</title></circle>
      <line class="mean-tick" x1="339.2" y1="156" x2="339.2" y2="184" stroke="var(--series-2)"></line>
      <text class="tick-label" x="339.2" y="150" text-anchor="middle">mean</text>
    </svg>

    <div class="callout">
    </div>

    
  </div>
</div>
</body>
</html>

Read notes.md for more info
