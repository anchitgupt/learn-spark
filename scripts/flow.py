"""Render the execution walkthrough as readable HTML before adding interaction."""
from html import escape as e


def render_flow(phases):
    buttons = []
    panels = []
    for i, phase in enumerate(phases):
        buttons.append(
            f'<button type="button" data-flow-select="{i}" '
            f'aria-controls="flow-phase-{i}" aria-pressed="false">'
            f'<span>{i + 1:02}</span>{e(phase["title"])}</button>'
        )
        panels.append(
            f'<div class="flow-panel" id="flow-phase-{i}" data-flow-panel>'
            f'<span class="eyebrow">PHASE {i + 1:02} / {len(phases):02}</span>'
            f'<h3>{e(phase["title"])}</h3>'
            f'<p>{e(phase["detail"])}</p>'
            f'<dl><dt>Who owns it</dt><dd>{e(phase["owner"])}</dd>'
            f'<dt>What changes</dt><dd>{e(phase["state"])}</dd>'
            f'<dt>Where is the data?</dt><dd>{e(phase["data"])}</dd>'
            f'<dt>How to verify it</dt><dd>{e(phase["evidence"])}</dd></dl>'
            f'<a class="text-link" href="#{e(phase["anchor"])}">Read the detailed steps →</a>'
            '</div>'
        )
    return (
        '<section id="flow-map" class="flow-walkthrough" aria-labelledby="flow-heading">'
        '<span class="eyebrow">THE WHOLE STORY AT A GLANCE</span>'
        '<h2 id="flow-heading">Six phases. Follow the responsibility.</h2>'
        '<p>Explore one phase at a time, then read the numbered steps below. '
        'This is a conceptual guide; planning can be demanded by an action or by plan inspection.</p>'
        '<div class="flow-board"><div class="flow-phase-nav js-only" role="group" '
        'aria-label="Choose an execution phase">' + ''.join(buttons) + '</div>'
        '<div class="flow-panels">' + ''.join(panels) + '</div></div>'
        '<div class="flow-controls js-only"><button type="button" id="flow-prev">← Previous phase</button>'
        '<span id="flow-status" role="status" aria-live="polite"></span>'
        '<button type="button" id="flow-next">Next phase →</button></div>'
        '<p class="code-note">An application can repeat query execution. Executor allocation, metrics, '
        'and failure recovery can also occur while work is running.</p></section>'
    )
