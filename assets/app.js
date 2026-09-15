'use strict';
(() => {
  const $ = (s, root = document) => root.querySelector(s);
  const $$ = (s, root = document) => [...root.querySelectorAll(s)];
  const slugs = $$('[data-progress]').map(el => el.dataset.progress);
  const storageKey = 'spark-fieldnotes-v1';
  let state = { version: 1, completed: [], notes: [] };
  let writable = true;
  let persistedRaw = null;
  let toastTimer;
  function toast(message) {
    $('#toast').textContent = message;
    $('#toast').classList.add('visible');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => $('#toast').classList.remove('visible'), 6500);
  }
  function validUrl(url) {
    if (!url) return true;
    try { return ['https:', 'http:'].includes(new URL(url).protocol); } catch { return false; }
  }
  function validNote(note) {
    return note && typeof note.id === 'string' && /^[a-zA-Z0-9_-]{1,100}$/.test(note.id)
      && slugs.includes(note.topic)
      && typeof note.question === 'string' && note.question.trim().length > 0 && note.question.length <= 2000
      && typeof note.answer === 'string' && note.answer.length <= 10000
      && typeof note.date === 'string' && (note.date === '' || /^\d{4}-\d{2}-\d{2}$/.test(note.date))
      && typeof note.source === 'string' && note.source.length <= 2000 && validUrl(note.source);
  }
  function validate(data) {
    return data && data.version === 1 && Array.isArray(data.completed)
      && data.completed.every(slug => slugs.includes(slug))
      && Array.isArray(data.notes) && data.notes.length <= 1000
      && data.notes.every(validNote) && new Set(data.notes.map(n => n.id)).size === data.notes.length;
  }
  function cleanNote(note) {
    return Object.fromEntries(['id', 'topic', 'question', 'answer', 'date', 'source'].map(k => [k, note[k]]));
  }
  try {
    const raw = localStorage.getItem(storageKey);
    persistedRaw = raw;
    if (raw) {
      const saved = JSON.parse(raw);
      if (!validate(saved)) throw new Error('Invalid saved notebook');
      state = { version: 1, completed: [...new Set(saved.completed)], notes: saved.notes.map(cleanNote) };
    }
  } catch {
    writable = false;
    toast('Browser storage could not be read. Changes are temporary; export a backup before leaving.');
  }
  function save(next) {
    state = next;
    if (!writable) return false;
    try {
      if (localStorage.getItem(storageKey) !== persistedRaw) {
        writable = false;
        return false;
      }
      persistedRaw = JSON.stringify(state);
      localStorage.setItem(storageKey, persistedRaw);
      return true;
    }
    catch { writable = false; return false; }
  }
  function saveMessage(success, text) {
    toast(success ? text : 'Kept in this tab only. Browser storage is unavailable; export before leaving.');
    if (!success && $('.storage-note')) $('.storage-note').textContent = 'Storage unavailable: changes are kept in this tab only. Export your notebook before leaving this page.';
  }
  function updateProgress() {
    $('#progress-count').textContent = `${state.completed.length} / ${slugs.length}`;
    $('#course-progress').value = state.completed.length;
    $$('[data-progress]').forEach(el => el.classList.toggle('done', state.completed.includes(el.dataset.progress)));
    const button = $('.complete-button');
    if (button) {
      const done = state.completed.includes(button.dataset.lesson);
      button.setAttribute('aria-pressed', String(done));
      button.textContent = done ? 'Understood ✓ · mark for review' : 'Mark as understood ✓';
    }
    if ($('#resume-learning') && state.completed.length) {
      const next = slugs.find(slug => !state.completed.includes(slug));
      $('#resume-learning').href = next ? `${next}.html` : 'questions.html';
      $('#resume-learning').textContent = next ? 'Continue the learning path →' : 'Put your knowledge into practice →';
    }
  }
  updateProgress();
  $('.complete-button')?.addEventListener('click', event => {
    const slug = event.currentTarget.dataset.lesson;
    const completed = state.completed.includes(slug) ? state.completed.filter(s => s !== slug) : [...state.completed, slug];
    const ok = save({ ...state, completed });
    updateProgress(); saveMessage(ok, 'Reading progress updated.');
  });
  const menu = $('.mobile-toggle');
  const sidebar = $('#sidebar');
  function closeMenu() {
    sidebar.classList.remove('open'); $('.scrim').hidden = true;
    document.body.classList.remove('menu-open'); menu.setAttribute('aria-expanded', 'false');
    if (innerWidth <= 700) sidebar.inert = true;
  }
  function syncMenu() { closeMenu(); sidebar.inert = innerWidth <= 700; }
  syncMenu(); window.addEventListener('resize', syncMenu);
  menu.addEventListener('click', () => {
    if (sidebar.classList.contains('open')) return closeMenu();
    sidebar.inert = false; sidebar.classList.add('open'); $('.scrim').hidden = false;
    document.body.classList.add('menu-open'); menu.setAttribute('aria-expanded', 'true');
    $('a', sidebar).focus();
  });
  $('.scrim').addEventListener('click', closeMenu);
  document.addEventListener('keydown', event => {
    if (sidebar.classList.contains('open') && event.key === 'Escape') { closeMenu(); menu.focus(); }
    if (sidebar.classList.contains('open') && event.key === 'Tab') {
      const links = $$('a, button', sidebar);
      if (event.shiftKey && document.activeElement === links[0]) { event.preventDefault(); links.at(-1).focus(); }
      else if (!event.shiftKey && document.activeElement === links.at(-1)) { event.preventDefault(); links[0].focus(); }
    }
  });
  const dialog = $('#search-dialog');
  let searchIndex;
  async function openSearch() {
    closeMenu(); dialog.showModal(); $('#site-search').focus();
    if (searchIndex) return renderSearch();
    $('#search-results').textContent = 'Loading the fieldnotes…';
    try {
      const response = await fetch('search.json');
      if (!response.ok) throw new Error('Search unavailable');
      searchIndex = await response.json(); renderSearch();
    } catch { $('#search-results').textContent = 'Search could not load. Use the topic navigation, or try opening search again.'; }
  }
  $('#open-search').addEventListener('click', openSearch);
  $('[data-close-dialog]').addEventListener('click', () => dialog.close());
  dialog.addEventListener('keydown', event => {
    if (event.key === 'Escape') {
      event.preventDefault();
      dialog.close();
    }
  });
  document.addEventListener('keydown', event => {
    if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === 'k') {
      event.preventDefault(); if (dialog.open) dialog.close(); else openSearch();
    }
  });
  dialog.addEventListener('click', event => {
    if (event.target !== dialog) return;
    const r = dialog.getBoundingClientRect();
    if (event.clientX < r.left || event.clientX > r.right || event.clientY < r.top || event.clientY > r.bottom) dialog.close();
  });
  function element(tag, text, className) {
    const el = document.createElement(tag); if (text !== undefined) el.textContent = text;
    if (className) el.className = className; return el;
  }
  function renderSearch() {
    if (!searchIndex) return;
    const query = $('#site-search').value.trim().toLowerCase();
    // Title matches first, then body matches, each in index order.
    const inTitle = item => item.title.toLowerCase().includes(query);
    const matches = searchIndex.filter(item => `${item.title} ${item.text}`.toLowerCase().includes(query))
      .sort((a, b) => inTitle(b) - inTitle(a)).slice(0, 10);
    $('#search-results').replaceChildren();
    if (!matches.length) $('#search-results').append(element('p', 'No matches. Try “shuffle”, “memory”, or “driver”.'));
    matches.forEach(item => {
      const link = element('a'); link.href = item.url;
      link.append(element('small', item.kind), element('span', item.title)); $('#search-results').append(link);
    });
  }
  $('#site-search').addEventListener('input', renderSearch);
  $$('.copy-code').forEach(button => button.addEventListener('click', async () => {
    const code = $('code', button.closest('.code-block'));
    try { await navigator.clipboard.writeText(code.textContent); toast('Code copied.'); }
    catch {
      const range = document.createRange(); range.selectNodeContents(code);
      const selection = window.getSelection(); selection.removeAllRanges(); selection.addRange(range);
      toast('Clipboard unavailable. Code selected; use your browser’s Copy command.');
    }
  }));
  let filter = 'All';
  function filterQuestions() {
    const query = $('#question-search').value.trim().toLowerCase();
    let count = 0;
    $$('.question-card').forEach(card => {
      card.hidden = !((filter === 'All' || card.dataset.type === filter) && card.dataset.search.includes(query));
      if (!card.hidden) count++;
    });
    $('#question-count').textContent = `${count} question${count === 1 ? '' : 's'}`;
    $('#no-questions').hidden = count !== 0;
  }
  $('#question-search')?.addEventListener('input', filterQuestions);
  $$('[data-filter]').forEach(button => button.addEventListener('click', () => {
    filter = button.dataset.filter;
    $$('[data-filter]').forEach(b => { b.classList.toggle('active', b === button); b.setAttribute('aria-pressed', String(b === button)); });
    filterQuestions();
  }));
  if (!$('#question-form')) return;
  if (!writable) $('.storage-note').textContent = 'Storage unavailable: changes are kept in this tab only. Export your notebook before leaving this page.';
  const form = $('#question-form');
  function resetForm() { form.reset(); $('#editing-id').value = ''; $('#form-title').textContent = 'Add an interview question'; $('#cancel-edit').hidden = true; }
  $('#cancel-edit').addEventListener('click', resetForm);
  function renderNotes() {
    $('#notes-count').textContent = `${state.notes.length} saved`;
    const list = $('#notes-list'); list.replaceChildren();
    if (!state.notes.length) {
      const empty = element('div', undefined, 'empty-notes');
      empty.append(element('h3', 'Your next interview starts a page.'), element('p', 'Add a question above. Your notes and reasoning will appear here.'));
      list.append(empty);
    }
    state.notes.forEach(note => {
      const card = element('article', undefined, 'note-card');
      card.append(element('div', `Needs verification${note.date ? ` · ${note.date}` : ''}`, 'note-meta'), element('h3', note.question));
      const topic = element('a', $(`#note-topic option[value="${note.topic}"]`).textContent + ' ↗'); topic.href = `${note.topic}.html`; card.append(topic);
      card.append(element('p', note.answer || 'No answer yet. Start with what you would investigate.'));
      if (note.source) { const source = element('a', 'Open your reference ↗'); source.href = note.source; source.target = '_blank'; source.rel = 'noreferrer'; card.append(source); }
      const actions = element('div', undefined, 'note-actions');
      const edit = element('button', 'Edit');
      edit.addEventListener('click', () => {
        $('#editing-id').value = note.id;
        ['question', 'answer', 'topic', 'date', 'source'].forEach(key => $(`#note-${key}`).value = note[key]);
        $('#form-title').textContent = 'Edit your question'; $('#cancel-edit').hidden = false;
        $('#note-question').focus(); form.scrollIntoView({ block: 'start' });
      });
      const remove = element('button', 'Delete');
      remove.addEventListener('click', () => {
        if (!confirm('Delete this saved question? Export your notebook first if you need a backup.')) return;
        const ok = save({ ...state, notes: state.notes.filter(n => n.id !== note.id) });
        if ($('#editing-id').value === note.id) resetForm();
        renderNotes(); saveMessage(ok, 'Question deleted.');
      });
      actions.append(edit, remove); card.append(actions); list.append(card);
    });
  }
  form.addEventListener('submit', event => {
    event.preventDefault();
    const id = $('#editing-id').value || (globalThis.crypto?.randomUUID?.() ?? `note-${Date.now()}-${Math.random().toString(36).slice(2)}`);
    const note = { id };
    ['question', 'answer', 'topic', 'date', 'source'].forEach(key => note[key] = $(`#note-${key}`).value.trim());
    if (!validNote(note)) return toast('Enter a question and a valid http or https reference URL.');
    if (!$('#editing-id').value && state.notes.length >= 1000) return toast('Notebook limit reached (1,000 questions). Export a backup before removing older notes.');
    const notes = state.notes.some(n => n.id === id) ? state.notes.map(n => n.id === id ? note : n) : [note, ...state.notes];
    const ok = save({ ...state, notes }); resetForm(); renderNotes(); saveMessage(ok, 'Question saved · needs verification.');
  });
  $('#export-notes').addEventListener('click', () => {
    const url = URL.createObjectURL(new Blob([JSON.stringify(state, null, 2)], { type: 'application/json' }));
    const link = element('a'); link.href = url; link.download = `spark-fieldnotes-${new Date().toISOString().slice(0, 10)}.json`;
    document.body.append(link); link.click(); link.remove(); setTimeout(() => URL.revokeObjectURL(url), 1000);
    toast('Notebook export prepared. Keep the downloaded JSON as your backup.');
  });
  $('#import-notes').addEventListener('change', async event => {
    const file = event.target.files[0]; if (!file) return;
    try {
      if (file.size > 5 * 1024 * 1024) throw new Error('Choose a notebook smaller than 5 MB.');
      const imported = JSON.parse(await file.text());
      if (!validate(imported)) throw new Error('This file is not a valid Spark Fieldnotes v1 notebook. Nothing was imported.');
      const signature = n => JSON.stringify([n.topic, n.question, n.answer, n.date, n.source]);
      const signatures = new Set(state.notes.map(signature));
      const ids = new Set(state.notes.map(n => n.id));
      const additions = [];
      let conflicts = 0;
      for (const note of imported.notes) {
        if (signatures.has(signature(note))) continue;
        if (ids.has(note.id)) { conflicts++; continue; }
        additions.push(cleanNote(note)); ids.add(note.id); signatures.add(signature(note));
      }
      if (state.notes.length + additions.length > 1000) throw new Error('Import would exceed 1,000 questions. Nothing was imported.');
      const ok = save({ version: 1, notes: [...additions, ...state.notes], completed: [...new Set([...state.completed, ...imported.completed])] });
      renderNotes(); updateProgress();
      saveMessage(ok, `Imported ${additions.length} questions. ${conflicts ? `${conflicts} changed copies skipped; existing notes kept.` : 'Duplicates skipped.'}`);
    } catch (error) { toast(error instanceof SyntaxError ? 'Invalid JSON. Nothing was imported.' : error.message); }
    finally { event.target.value = ''; }
  });
  renderNotes();
})();
