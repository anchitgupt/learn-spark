"""Render original prediction exercises with native, no-JavaScript answer reveals."""
from html import escape as e


def code_block(code):
    return (
        '<div class="code-block"><div><span>PYTHON / PYSPARK</span>'
        '<button class="copy-code js-only">Copy code</button></div>'
        f'<pre><code>{e(code)}</code></pre></div>'
    )


def render_exercise(exercise, index):
    prompts = ''.join(f'<li>{e(prompt)}</li>' for prompt in exercise['prompts'])
    reasoning = ''.join(f'<p>{e(item)}</p>' for item in exercise['reasoning'])
    flow = ''.join(
        f'<li><strong>{e(step["label"])}</strong><span>{e(step["detail"])}</span></li>'
        for step in exercise['flow']
    )
    evidence = ''.join(f'<li>{e(item)}</li>' for item in exercise['evidence'])
    sources = ' · '.join(
        f'<a href="#source-{e(source)}">{e(source.replace("-", " "))}</a>'
        for source in exercise['sources']
    )
    return (
        f'<section class="prediction-exercise" id="{e(exercise["id"])}">'
        f'<span class="eyebrow">EXERCISE {index:02} / AUTHORED PRACTICE</span>'
        f'<h2>{e(exercise["title"])}</h2><p>{e(exercise["intro"])}</p>'
        '<p class="code-note">Run the shared setup above first. Predict before running this snippet.</p>'
        + code_block(exercise['code']) +
        '<div class="prediction-prompts"><h3>Pause and predict</h3>'
        f'<ol>{prompts}</ol><p>Say or write your prediction before revealing the answer.</p></div>'
        f'<details class="answer prediction-answer"><summary>Reveal the reasoning: {e(exercise["title"])}</summary>'
        '<div class="prediction-body"><h3>Follow the work</h3>'
        '<p class="code-note">Conceptual flow under the shared baseline; not a captured Spark UI trace.</p>'
        f'<ol class="prediction-flow" aria-label="Expected execution flow">{flow}</ol>'
        f'{reasoning}<div class="expected"><strong>Expected result</strong><p>{e(exercise["output"])}</p></div>'
        '<h3>Check the plan and Spark UI</h3>' + code_block(exercise['verify_code']) +
        f'<ol>{evidence}</ol><h3>A short interview answer</h3><p>{e(exercise["spoken"])}</p>'
        f'<details class="answer followup-answer"><summary>Interviewer follow-up: {e(exercise["followup"])}</summary>'
        f'<p>{e(exercise["followup_answer"])}</p></details>'
        f'<p class="section-source">Check the sources: {sources}</p>'
        f'<a class="text-link" href="notebook.html#question-form">Record your own version in My notebook →</a>'
        '</div></details></section>'
    )
