"""Render portable local reading pages, including executed notebook previews."""
from pathlib import Path
import base64
import html
import json
import re
import markdown

ROOT = Path(__file__).resolve().parent
CSS = """
:root{--ink:#172c35;--muted:#526770;--teal:#126e7e;--paper:#fcfaf5;--line:#d7e0df;--nav:#eef3f1}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:24px}body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.7 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
a{color:var(--teal);text-underline-offset:3px}a:hover{color:#093e49}a:focus-visible,button:focus-visible{outline:3px solid #bc5738;outline-offset:3px}
.brand{font-size:12px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--teal)}.layout{display:grid;grid-template-columns:250px minmax(0,950px);max-width:1240px;margin:auto;gap:44px;padding:38px 30px 80px}
aside{position:sticky;top:24px;height:calc(100vh - 48px);overflow:auto;padding-right:14px;font-size:13px;line-height:1.5}aside .brand{display:block;padding-bottom:18px;border-bottom:1px solid var(--line)}.navlinks{display:grid;gap:8px;margin:20px 0}.navlinks a{text-decoration:none;padding:7px 10px;border-radius:6px}.navlinks a.current{background:var(--ink);color:white;font-weight:650}.toc{padding-top:18px;border-top:1px solid var(--line)}.toc ul{list-style:none;margin:0;padding:0}.toc>ul>li>a{display:none}.toc li a{display:block;padding:5px 0;text-decoration:none}.toc ul ul{padding:0}.toc ul ul ul{padding-left:12px}.toc li{margin:0}
main{min-width:0}h1{font-family:Georgia,serif;font-size:52px;line-height:1.09;letter-spacing:-1.6px;margin:28px 0 25px;font-weight:500}h2{font-size:27px;line-height:1.3;margin:55px 0 20px;border-top:1px solid var(--line);padding-top:28px;letter-spacing:-.5px}h3{font-size:20px;line-height:1.4;margin:30px 0 12px}p{margin:15px 0}li{margin:9px 0}strong{font-weight:700}code{font-size:.88em;background:#edf1ef;padding:2px 5px;border-radius:4px;color:#154e59}pre{background:#142d38;color:#edf7f4;padding:22px;border-radius:9px;overflow:auto;line-height:1.65;font-size:14px;margin:24px 0}pre code{background:none;color:inherit;padding:0;font-size:inherit}.tablewrap{overflow:auto;margin:25px 0;border:1px solid var(--line);border-radius:8px}table{border-collapse:collapse;width:100%;font-size:14px;line-height:1.55}th{text-align:left;background:#e9efeb;font-weight:700;padding:13px 15px;vertical-align:top}td{padding:13px 15px;border-top:1px solid var(--line);vertical-align:top}tbody tr:nth-child(even){background:#f4f5ef}td:first-child{font-weight:550}blockquote{border-left:4px solid var(--teal);margin:24px 0;padding:2px 22px;background:var(--nav)}.topline{display:flex;justify-content:space-between;gap:20px;align-items:center}.topline span{font-size:12px;color:var(--muted);letter-spacing:.6px}.topline button{border:1px solid var(--line);border-radius:6px;padding:8px 12px;background:transparent;color:var(--muted);cursor:pointer}.meta{color:var(--muted);font-size:13px;margin:35px 0;padding-top:20px;border-top:1px solid var(--line)}.output{background:#eef3ef;color:#263f47;border-left:3px solid #147d92;white-space:pre-wrap;word-break:break-word}.cell-label{font:11px/1.5 system-ui;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin:24px 0 -15px}.plot{display:block;max-width:100%;height:auto;margin:25px auto;border-radius:8px;background:white}details{border:1px solid var(--line);border-radius:6px;padding:12px 16px;margin:18px 0}summary{cursor:pointer;font-weight:600}
@media(max-width:950px){.layout{grid-template-columns:190px minmax(0,1fr);gap:25px;padding:25px 20px}h1{font-size:43px}}
@media(max-width:700px){.layout{display:block;padding:20px 18px 50px}aside{position:static;height:auto;padding:0;margin-bottom:30px}.navlinks{grid-template-columns:1fr 1fr;gap:3px}.toc{display:none}h1{font-size:39px}h2{font-size:25px}body{font-size:16px}.topline{flex-wrap:wrap}th,td{min-width:110px}pre{padding:16px;font-size:13px}}
@media print{body{background:white;font:11pt/1.5 Georgia,serif;color:#111}.layout{display:block;padding:0;max-width:none}aside,.topline button{display:none}h1{font-size:30pt}h2{font-size:20pt;break-before:page}h3{font-size:14pt}pre{white-space:pre-wrap;background:#f2f2f2;color:#111;border:1px solid #ddd;break-inside:avoid;font-size:9pt}table{font-size:9pt}.tablewrap{overflow:visible}tr{break-inside:avoid}a{color:#111;text-decoration:underline}.plot{max-height:7in;object-fit:contain}.meta{font-size:9pt}}
"""

PAGES = [
    ("README.md", "index.html", "Start here"),
    ("COURSE.md", "COURSE.html", "Course handbook"),
    ("BRIDGE.md", "BRIDGE.html", "AI apps & career"),
    ("PRACTICE.md", "PRACTICE.html", "40 exercises"),
    ("GLOSSARY.md", "GLOSSARY.html", "Glossary"),
    ("SOURCES.md", "SOURCES.html", "Resource evaluation"),
    ("PROGRESS.md", "PROGRESS.html", "Progress tracker"),
    ("SOLUTIONS.md", "SOLUTIONS.html", "Answer guide"),
    ("VALIDATION.md", "VALIDATION.html", "Verification"),
]

def render_markdown(source):
    renderer = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "sane_lists"], extension_configs={"toc": {"toc_depth": "1-2"}})
    body = renderer.convert(source)
    for markdown_file, html_file, _ in PAGES:
        body = body.replace(f'href="{markdown_file}"', f'href="{html_file}"')
    body = body.replace("<table>", '<div class="tablewrap"><table>').replace("</table>", "</table></div>")
    return body, renderer.toc

def shell(title, body, toc, current, prefix=""):
    links = "".join(f'<a class="{"current" if filename==current else ""}" href="{prefix}{filename}">{label}</a>' for _, filename, label in PAGES)
    links += f'<a href="{prefix}LABS.html">Notebook reading room</a>'
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="A comprehensive beginner Python course for data analytics, machine learning, and AI applications."><title>{html.escape(title)} · Python → Data → AI</title><style>{CSS}</style></head><body><div class="layout"><aside><a class="brand" href="{prefix}index.html">Python / Data / AI</a><nav class="navlinks" aria-label="Course materials">{links}</nav><nav aria-label="Page contents">{toc}</nav></aside><main><div class="topline"><span>YOUR BEGINNER-TO-BUILDER COURSE · SEPTEMBER 2026</span><button type="button" onclick="window.print()">Print / Save PDF</button></div>{body}<div class="meta">Designed for 10–15 hours a week · 160-hour foundation + 40-hour application and career bridge<br>Learn by building, testing, and explaining. Time estimates are planning guides; checkpoints determine progress.</div></main></div></body></html>'''

for source, filename, title in PAGES:
    path = ROOT / source
    if not path.exists():
        continue
    body, toc = render_markdown(path.read_text(encoding="utf-8"))
    (ROOT / filename).write_text(shell(title, body, toc, filename), encoding="utf-8")

lessons = ROOT / "lessons"
lessons.mkdir(exist_ok=True)
lab_links = []
for path in sorted((ROOT / "notebooks").glob("*.ipynb")):
    notebook = json.loads(path.read_text(encoding="utf-8"))
    parts = []
    title = path.stem.replace("_", " ")
    for cell in notebook["cells"]:
        source = "".join(cell["source"])
        if cell["cell_type"] == "markdown":
            parts.append(render_markdown(source)[0])
        elif cell["cell_type"] == "code":
            parts.append('<div class="cell-label">Python cell</div><pre><code>' + html.escape(source) + '</code></pre>')
            for output in cell.get("outputs", []):
                if output["output_type"] == "stream":
                    parts.append('<pre class="output">' + html.escape("".join(output.get("text", []))) + '</pre>')
                data = output.get("data", {})
                if "image/png" in data:
                    encoded = "".join(data["image/png"]).replace("\n", "")
                    parts.append(f'<img class="plot" alt="Executed teaching chart; description and units appear in the adjacent lesson and chart labels" src="data:image/png;base64,{encoded}">')
                elif "text/plain" in data:
                    parts.append('<pre class="output">' + html.escape("".join(data["text/plain"])) + '</pre>')
    filename = path.stem + ".html"
    intro = f'<p><a href="../notebooks/{path.name}" download>Download executable notebook</a> · This page is a reading preview of the notebook and its saved outputs.</p>'
    (lessons / filename).write_text(shell(title, intro + "\n".join(parts), "", "", prefix="../"), encoding="utf-8")
    lab_links.append(f"- [Read lesson {path.stem.split('_')[0]}: {title[3:]}](lessons/{filename}) · [Download notebook](notebooks/{path.name})")

lab_body, lab_toc = render_markdown("# Notebook reading room\n\nRead the worked examples here, then run and modify the `.ipynb` files in your course environment. Reading is not a substitute for executing and changing code. Saved outputs reflect the validation environment; see the verification record.\n\n" + "\n".join(lab_links) + "\n\n## Working safely\n\nCreate personal copies before adding answers. `build_notebooks.py` is a maintainer script that overwrites generated lessons; you do not need to run it to study. Notebook 4 reads the included CSV. The other notebooks create their own teaching data. No core notebook calls a paid API or downloads models.\n")
(ROOT / "LABS.html").write_text(shell("Notebook reading room", lab_body, lab_toc, "LABS.html"), encoding="utf-8")
print("Rendered handbook pages and eight notebook previews.")
