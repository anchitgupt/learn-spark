'use strict';
(() => {
  const panels = [...document.querySelectorAll('[data-flow-panel]')];
  const buttons = [...document.querySelectorAll('[data-flow-select]')];
  if (!panels.length) return;
  document.querySelector('.flow-walkthrough').classList.add('is-interactive');
  let selected = 0;
  const previous = document.querySelector('#flow-prev');
  const next = document.querySelector('#flow-next');
  function select(index) {
    selected = Math.max(0, Math.min(index, panels.length - 1));
    panels.forEach((panel, i) => { panel.hidden = i !== selected; });
    buttons.forEach((button, i) => {
      button.setAttribute('aria-pressed', String(i === selected));
    });
    previous.disabled = selected === 0;
    next.disabled = selected === panels.length - 1;
    document.querySelector('#flow-status').textContent =
      `Phase ${selected + 1} of ${panels.length}: ${panels[selected].querySelector('h3').textContent}`;
  }
  buttons.forEach((button, i) => button.addEventListener('click', () => select(i)));
  previous.addEventListener('click', () => select(selected - 1));
  next.addEventListener('click', () => select(selected + 1));
  select(0);
})();
