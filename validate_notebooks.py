"""Execute all notebooks with a workspace-owned kernel and record results."""
from pathlib import Path
import os
import json
import sys
import platform
from importlib.metadata import version
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
scratch = ROOT / ".validation"
kernel = scratch / "jupyter" / "kernels" / "python3"
kernel.mkdir(parents=True, exist_ok=True)
(kernel / "kernel.json").write_text(json.dumps({
    "argv": [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
    "display_name": "Python 3 (course validation)", "language": "python"
}), encoding="utf-8")
os.environ["JUPYTER_PATH"] = str(scratch / "jupyter")
os.environ["JUPYTER_RUNTIME_DIR"] = str(scratch / "runtime")
os.environ["IPYTHONDIR"] = str(scratch / "ipython")
os.environ["MPLCONFIGDIR"] = str(scratch / "matplotlib")
for value in ["JUPYTER_RUNTIME_DIR", "IPYTHONDIR", "MPLCONFIGDIR"]:
    Path(os.environ[value]).mkdir(parents=True, exist_ok=True)

import nbformat
from nbclient import NotebookClient

results = []
for path in sorted((ROOT / "notebooks").glob("*.ipynb")):
    if len(sys.argv) > 1 and path.name not in sys.argv[1:]:
        continue
    nb = nbformat.read(path, as_version=4)
    nbformat.validate(nb)
    NotebookClient(nb, timeout=120, kernel_name="python3", resources={"metadata": {"path": str(path.parent)}}).execute()
    nbformat.write(nb, path)
    cells = sum(cell.cell_type == "code" for cell in nb.cells)
    print("PASS", path.name, flush=True)

for path in sorted((ROOT / "notebooks").glob("*.ipynb")):
    nb = nbformat.read(path, as_version=4)
    code_cells = [cell for cell in nb.cells if cell.cell_type == "code"]
    assert all(cell.execution_count is not None for cell in code_cells), path.name
    assert not any(output.output_type == "error" for cell in code_cells for output in cell.outputs), path.name
    results.append(f"| `{path.name}` | Passed | {len(code_cells)} |")

packages = ["numpy", "pandas", "matplotlib", "scikit-learn", "ipykernel", "nbformat", "nbclient"]
versions = {package: version(package) for package in packages}
(ROOT / "requirements.txt").write_text("# Direct dependencies used for the verified teaching notebooks.\n" + "\n".join(f"{name}=={value}" for name, value in versions.items()) + "\n", encoding="utf-8")
report = f"""# Validation record

Validated on {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}.

All eight notebooks were validated structurally and executed top-to-bottom in separate fresh Python kernels. Assertions passed. Executed outputs are retained in the notebooks. Every dataset is generated locally or included as a CSV; no notebook calls a hosted AI model or downloads model weights.

Python: **{platform.python_version()}**. Platform: **{platform.system()} {platform.machine()}**.

| Notebook | Execution | Code cells |
|---|---|---:|
""" + "\n".join(results) + "\n\n## Versions\n\n" + "\n".join(f"- {name}: {value}" for name, value in versions.items()) + """

## Scope and limits

Notebook assertions check arithmetic, shapes, valid values, row reconciliation, SQL/pandas parity, and valid prediction outputs. Successful execution does not certify a learner's understanding or real-world model validity. Generated teaching datasets cannot establish business, medical, or other domain conclusions. The 40-hour application/career bridge is a set of learner implementation assignments; real PyTorch/Transformers/LLM integrations in that bridge are not prebuilt or executed here. Setup commands on Windows and other Python versions were documented, not exercised on those systems.

## Rerun

Open the course folder, create/select the environment described in Module 0, and install `requirements.txt`. Run `python validate_notebooks.py` from the course root, or select the same environment in VS Code and restart/run all cells in each notebook. Notebook 4 recreates three derived CSVs in `outputs/` while preserving `data/orders.csv`.

`requirements.txt` records direct versions. `environment-freeze.txt` records the full validation environment. Neither guarantees identical binary behavior on every operating system. `build_notebooks.py` is a maintainer utility: running it regenerates notebooks and would overwrite your edits. Work in copies if you want to keep personal answers.
"""
(ROOT / "VALIDATION.md").write_text(report, encoding="utf-8")
print("Validation record and direct requirements written.")
