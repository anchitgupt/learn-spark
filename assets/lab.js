'use strict';
(() => {
  const canvas = document.querySelector('#shuffle-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const mode = document.querySelector('#lab-mode');
  const play = document.querySelector('#lab-play');
  const next = document.querySelector('#lab-step');
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const descriptions = {
    shuffle: [
      'Input: each partition contains a mix of cities. Pune appears in all three partitions.',
      'Group by city: rows with the same key need compatible distribution. The lines show where rows will move in this simplified model.',
      'Redistribute: rows cross partition boundaries to meet others with the same city key.',
      'Aggregate: Pune has 3 rows, Delhi has 2, and Mumbai has 1. Real Spark may combine locally before the shuffle.'
    ],
    filter: [
      'Input: each partition contains a mix of cities. Pune appears in all three partitions.',
      'Filter to Pune: evaluate each row inside its existing partition. No city grouping is needed.',
      'Discard Delhi and Mumbai locally. Retained Pune rows stay in their original partitions.',
      'Result: one Pune row remains in each of the three partitions. No cross-partition movement was needed.'
    ]
  };
  const rows = [
    { city: 'Pune', input: 0, slot: 0, target: 0, out: 0, color: '#b64c2d' },
    { city: 'Delhi', input: 0, slot: 1, target: 1, out: 0, color: '#527966' },
    { city: 'Mumbai', input: 1, slot: 0, target: 2, out: 0, color: '#627994' },
    { city: 'Pune', input: 1, slot: 1, target: 0, out: 1, color: '#b64c2d' },
    { city: 'Delhi', input: 2, slot: 0, target: 1, out: 1, color: '#527966' },
    { city: 'Pune', input: 2, slot: 1, target: 0, out: 2, color: '#b64c2d' }
  ];
  let step = 0, timer = null, frame = null;
  function label(text, x, y, size = 16, color = '#66725f') {
    ctx.fillStyle = color; ctx.font = `${size}px sans-serif`; ctx.fillText(text, x, y);
  }
  function box(x, y, w, h, fill, stroke) {
    ctx.fillStyle = fill; ctx.strokeStyle = stroke; ctx.lineWidth = 1;
    ctx.beginPath(); ctx.roundRect(x, y, w, h, 7); ctx.fill(); ctx.stroke();
  }
  function draw(progress = 1) {
    ctx.clearRect(0, 0, 1000, 440);
    ctx.fillStyle = '#fffefa'; ctx.fillRect(0, 0, 1000, 440);
    label('INPUT PARTITIONS', 50, 38, 15);
    label(mode.value === 'shuffle' ? 'SHUFFLE → GROUP' : 'LOCAL FILTER', 410, 38, 15, '#a84427');
    label('OUTPUT PARTITIONS', 720, 38, 15);
    for (let i = 0; i < 3; i++) {
      box(40, 70 + i * 115, 280, 94, '#f5f5ef', '#d9ddd1');
      box(680, 70 + i * 115, 280, 94, '#f5f5ef', '#d9ddd1');
      label(`P${i}`, 55, 94 + i * 115, 12);
      label(`P${i}`, 695, 94 + i * 115, 12);
    }
    for (const row of rows) {
      const x1 = 85 + row.slot * 110, y1 = 113 + row.input * 115;
      const target = mode.value === 'shuffle' ? row.target : row.input;
      const x2 = 728 + (mode.value === 'shuffle' ? row.out * 72 : 0), y2 = 113 + target * 115;
      const kept = mode.value === 'shuffle' || row.city === 'Pune';
      if (step >= 1 && kept) {
        ctx.strokeStyle = row.color + '65'; ctx.setLineDash([5, 6]); ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(x1 + 42, y1); ctx.bezierCurveTo(420, y1, 580, y2, x2, y2); ctx.stroke(); ctx.setLineDash([]);
      }
      const t = step >= 2 && kept ? progress : 0;
      const x = x1 + (x2 - x1) * t, y = y1 + (y2 - y1) * t;
      ctx.globalAlpha = !kept && step >= 2 ? .14 : 1;
      box(x - 4, y - 3, mode.value === 'shuffle' && step >= 2 ? 67 : 95, 29, row.color, row.color);
      label(row.city, x + 3, y + 17, 14, '#ffffff'); ctx.globalAlpha = 1;
    }
    if (step === 3) {
      label(mode.value === 'shuffle' ? 'Pune: 3     Delhi: 2     Mumbai: 1' : 'Pune stays distributed: 1 row per partition', 290, 420, 18, '#354d3e');
    } else label('Illustrative rows • not a live Spark execution', 315, 420, 14);
  }
  function render(animate = false) {
    cancelAnimationFrame(frame);
    document.querySelector('#lab-step-label').textContent = `STEP ${step + 1} / 4`;
    document.querySelector('#lab-description').textContent = descriptions[mode.value][step];
    next.disabled = step === 3;
    if (animate && step === 2 && !reduced.matches) {
      let start;
      const tick = time => {
        if (!start) start = time;
        const p = Math.min((time - start) / 1000, 1);
        draw(p * p * (3 - 2 * p));
        if (p < 1) frame = requestAnimationFrame(tick);
      };
      frame = requestAnimationFrame(tick);
    } else draw();
  }
  function pause() { clearInterval(timer); timer = null; play.textContent = 'Play walkthrough'; }
  function advance() { step = Math.min(step + 1, 3); render(true); if (step === 3) pause(); }
  play.addEventListener('click', () => {
    if (timer) { pause(); cancelAnimationFrame(frame); render(); return; }
    if (step === 3) step = 0;
    render(); play.textContent = 'Pause walkthrough';
    timer = setInterval(advance, 2000);
  });
  next.addEventListener('click', () => { pause(); advance(); });
  document.querySelector('#lab-reset').addEventListener('click', () => { pause(); step = 0; render(); });
  mode.addEventListener('change', () => { pause(); step = 0; render(); });
  document.addEventListener('visibilitychange', () => { if (document.hidden) pause(); });
  reduced.addEventListener('change', () => { cancelAnimationFrame(frame); render(); });
  render();
})();
