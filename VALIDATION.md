# Validation record

Validated on 2026-09-05 12:24 UTC.

All eight notebooks were validated structurally and executed top-to-bottom in separate fresh Python kernels. Assertions passed. Executed outputs are retained in the notebooks. Every dataset is generated locally or included as a CSV; no notebook calls a hosted AI model or downloads model weights.

Python: **3.12.14**. Platform: **Darwin arm64**.

| Notebook | Execution | Code cells |
|---|---|---:|
| `01_python_basics.ipynb` | Passed | 5 |
| `02_functions_files_tests.ipynb` | Passed | 4 |
| `03_numpy_statistics.ipynb` | Passed | 5 |
| `04_pandas_data_quality.ipynb` | Passed | 6 |
| `05_sql_and_charts.ipynb` | Passed | 3 |
| `06_machine_learning_pipeline.ipynb` | Passed | 4 |
| `07_neural_network_foundations.ipynb` | Passed | 4 |
| `08_text_retrieval_and_ai_evaluation.ipynb` | Passed | 4 |

## Versions

- numpy: 2.5.2
- pandas: 3.0.5
- matplotlib: 3.11.1
- scikit-learn: 1.9.0
- ipykernel: 7.3.0
- nbformat: 5.11.1
- nbclient: 0.11.0

## Scope and limits

Notebook assertions check arithmetic, shapes, valid values, row reconciliation, SQL/pandas parity, and valid prediction outputs. Successful execution does not certify a learner's understanding or real-world model validity. Generated teaching datasets cannot establish business, medical, or other domain conclusions. The 40-hour application/career bridge is a set of learner implementation assignments; real PyTorch/Transformers/LLM integrations in that bridge are not prebuilt or executed here. Setup commands on Windows and other Python versions were documented, not exercised on those systems.

## Rerun

Open the course folder, create/select the environment described in Module 0, and install `requirements.txt`. Run `python validate_notebooks.py` from the course root, or select the same environment in VS Code and restart/run all cells in each notebook. Notebook 4 recreates three derived CSVs in `outputs/` while preserving `data/orders.csv`.

`requirements.txt` records direct versions. `environment-freeze.txt` records the full validation environment. Neither guarantees identical binary behavior on every operating system. `build_notebooks.py` is a maintainer utility: running it regenerates notebooks and would overwrite your edits. Work in copies if you want to keep personal answers.
