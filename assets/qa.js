'use strict';
(() => {
  const $ = (s, root = document) => root.querySelector(s);
  const $$ = (s, root = document) => [...root.querySelectorAll(s)];
  const items = $$('.qa-item');
  if (!items.length) return;
  // Separate from the notebook's storage so its export and import format stay unchanged.
  const storageKey = 'spark-fieldnotes-qa-v1';
  const questionId = item => item.id.slice(3);
  let known = new Set();
  try {
    const saved = JSON.parse(localStorage.getItem(storageKey) || '[]');
    if (Array.isArray(saved)) known = new Set(saved.filter(id => typeof id === 'string' && $(`#qa-${CSS.escape(id)}`)));
  } catch { /* unreadable storage: marks last for this visit only */ }
  const state = { type: 'All', query: '', ran: false, hideKnown: false };

  function save() {
    try { localStorage.setItem(storageKey, JSON.stringify([...known])); } catch { /* keep marks in memory */ }
  }
  function paintKnown() {
    items.forEach(item => {
      const on = known.has(questionId(item));
      item.classList.toggle('is-known', on);
      $('[data-qa-known]', item).checked = on;
    });
    $('#qa-known-total').textContent = known.size;
    $$('[data-qa-count]').forEach(el => {
      const inTopic = items.filter(item => item.dataset.qaTopic === el.dataset.qaCount);
      const done = inTopic.filter(item => known.has(questionId(item))).length;
      el.textContent = done ? `${done}/${inTopic.length}` : String(inTopic.length);
      el.classList.toggle('complete', done === inTopic.length);
    });
  }
  function apply() {
    let shown = 0;
    items.forEach(item => {
      const visible = (state.type === 'All' || item.dataset.qaType === state.type)
        && (!state.ran || item.dataset.qaRan === 'true')
        && (!state.hideKnown || !known.has(questionId(item)))
        && item.dataset.search.includes(state.query);
      item.hidden = !visible;
      if (visible) shown++;
    });
    $$('[data-qa-section]').forEach(section => { section.hidden = !$('.qa-item:not([hidden])', section); });
    $('#qa-count').textContent = `Showing ${shown} of ${items.length}`;
    $('#qa-empty').hidden = shown !== 0;
  }
  function setRevealed(item, open) {
    item.classList.toggle('revealed', open);
    const button = $('.qa-reveal', item);
    button.setAttribute('aria-expanded', String(open));
    button.textContent = open ? 'Hide answer' : 'Show answer';
  }

  $('#qa-search').addEventListener('input', event => { state.query = event.target.value.trim().toLowerCase(); apply(); });
  $$('[data-qa-filter]').forEach(button => button.addEventListener('click', () => {
    state.type = button.dataset.qaFilter;
    $$('[data-qa-filter]').forEach(b => { b.classList.toggle('active', b === button); b.setAttribute('aria-pressed', String(b === button)); });
    apply();
  }));
  function toggle(id, onChange) {
    const button = $(`#${id}`);
    button.addEventListener('click', () => {
      const on = button.getAttribute('aria-pressed') !== 'true';
      button.setAttribute('aria-pressed', String(on));
      onChange(on);
    });
  }
  toggle('qa-quiz', on => { document.body.classList.toggle('qa-quiz', on); items.forEach(item => setRevealed(item, false)); });
  toggle('qa-only-ran', on => { state.ran = on; apply(); });
  toggle('qa-hide-known', on => { state.hideKnown = on; apply(); });
  $$('.qa-reveal').forEach(button => button.addEventListener('click', () => {
    const item = button.closest('.qa-item');
    setRevealed(item, !item.classList.contains('revealed'));
  }));
  $$('[data-qa-known]').forEach(box => box.addEventListener('change', () => {
    if (box.checked) known.add(box.dataset.qaKnown); else known.delete(box.dataset.qaKnown);
    save(); paintKnown();
    if (state.hideKnown) apply();
  }));
  paintKnown();
})();
