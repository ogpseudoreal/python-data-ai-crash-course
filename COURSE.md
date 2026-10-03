# Python → Data → AI

## Your route from complete beginner to independent projects

**Your complete plan: approximately 200 focused hours — a 160-hour foundation plus a 40-hour AI application and career bridge.** At your chosen 10–15 hours per week, the planned work takes roughly 14–20 weeks. Allow extra time whenever a checkpoint needs another attempt. Read, type, change, explain, and build. You do not need prior programming experience; your Excel knowledge and basic algebra provide a useful starting point.

This course aims to make you able to take an unfamiliar CSV file, understand its structure, clean it with a reproducible script, answer useful questions with charts and SQL, and build and evaluate a sensible predictive model. You will also learn how neural networks train, how text retrieval works, and how language-model applications are assembled and evaluated.

It does not make you an experienced data scientist in a few weeks. Professional proficiency takes repeated work with messy real problems, feedback, and deeper study. The fast route is to remove duplicated content and unnecessary tool changes while retaining practice, statistics, debugging, and honest evaluation.

**Your preferences:** 10–15 study hours per week; comfortable with Excel and basic algebra; interested in analytics, ML models, AI applications, and career preparation. The sequence puts analytics first and develops the other goals from that foundation. Setup is macOS first, based on your current workspace, with a Windows alternative. The exercises use invented retail data and small teaching datasets, so your first work needs no external accounts or private information.

### Build on what you know from Excel

| Excel idea | Python/data equivalent | The difference to learn |
|---|---|---|
| Cell value | Variable | A name refers to a value, not a grid location |
| Formula | Expression or function | Write reusable logic and validate inputs |
| Table column | pandas Series | Operate on the whole column |
| Filter | Boolean mask and `.loc` | The filtering rule becomes saved, repeatable code |
| PivotTable | `groupby` or `pivot_table` | Define aggregation and missing-value behavior explicitly |
| XLOOKUP | Dictionary lookup or table merge | A duplicate lookup key can multiply rows in a merge |
| IF | `if/elif/else` | Python blocks use indentation |
| COUNTIF/SUMIF | Mask plus count/sum, or grouping | Check the denominator and row grain |
| Power Query steps | Data-cleaning functions/pipeline | You write, test, and rerun each transformation |

Use familiar spreadsheet reasoning to check small Python results by hand. Avoid maintaining a separately edited spreadsheet as a second, conflicting source of truth.

### What counts as passing

You can use documentation and look up syntax. For each checkpoint, however, you must design and explain the solution yourself, without an AI assistant writing it. A successful run alone is insufficient: you should predict the output, test an edge case, and explain why the result answers the question.

Use a three-level score: **0** = cannot start; **1** = complete with substantial hints; **2** = complete independently and explain it. Move on only when every checkpoint criterion scores 2. If you score 0 or 1, revisit the named prerequisite, do two new variants, and retry after a night's sleep. Do not repeat an entire course for one missing concept.

### Your study rhythm

A 90-minute session: 10 minutes recalling yesterday without notes; 20 minutes reading or watching the assigned explanation; 45 minutes writing and changing code; 10 minutes checking mistakes; 5 minutes recording the next step. This is a suggested routine, not a research-derived optimum. Use two shorter blocks when necessary.

After learning a concept, revisit it the next day, later that week, and the following week. Keep `learning_log.md` with: the problem, your first attempt, the error, the cause, the correction, and a new example. Reading a solution is the start of a repair; reproducing it on different inputs is the evidence that the repair worked.

An AI tutor can explain an error, ask questions, and give hints. Use: “Give me one hint, do not write the solution. Ask me to predict the next step.” Try for 15–20 minutes before asking. At checkpoints, close the chat. You must be able to maintain code you accept from any source.

### Schedule and dependencies

The hours below include the selected reading, notebook work, exercises, and module checkpoint. They do **not** include completing every linked external course. Core reading assignments are targeted topics, not whole textbooks.

| Module | Focus | Hours | Concrete output |
|---|---|---:|---|
| 0 | Tools and first program | 3 | Working script and notebook |
| 1 | Values, variables, expressions, strings | 10 | Small calculators |
| 2 | Decisions, loops, collections | 10 | Transaction summaries |
| 3 | Functions, debugging, tests, objects | 12 | Tested reusable functions |
| 4 | Files, modules, JSON, project structure | 9 | CSV-to-summary script |
| 5 | NumPy and essential linear algebra | 10 | Array calculations |
| 6 | pandas and data quality | 14 | Audited retail dataset |
| 7 | SQL and visual communication | 10 | Queries, charts, short report |
| 8 | Statistics and uncertainty | 12 | A defensible comparison |
| 9 | First ML workflow | 14 | Baseline and predictive model |
| 10 | Model selection and error analysis | 12 | Validated model comparison |
| 11 | Neural-network foundations | 10 | Training loop and classifier |
| 12 | Text, retrieval, and language AI | 8 | Search system and AI evaluation plan |
| 13 | Reproducible, responsible delivery | 6 | Rerunnable project handoff |
| 14 | Independent capstone | 20 | Portfolio-quality beginner project |
| **Total** | | **160** | |

The 160-hour foundation occupies 8 weeks at 20 hours/week, about 11 at 15, and 16 at 10. Add the [40-hour application and career bridge](BRIDGE.html) for your full set of goals: **200 hours, about 14–20 weeks at your pace**. A planning allowance of 220–260 hours including remediation is more forgiving, roughly 15–26 weeks. These are arithmetic conversions, not promises. Do not sacrifice sleep to meet the table.

For an eight-week intensive schedule: week 1 = Modules 0–1 and 7 hours of Module 2; week 2 = finish 2, complete 3, start 4; week 3 = finish 4, complete 5, start 6; week 4 = finish 6, complete 7, start 8; week 5 = finish 8 and start 9; week 6 = finish 9, complete 10, start 11; week 7 = finish 11, complete 12–13; week 8 = capstone. Slower schedules use the same order.

### The first seven study sessions

1. Install and verify the tools; run `hello.py`; change its printed output.
2. Numbers, variables, strings; do exercises 1–3.
3. Predict outputs; type and modify examples; start Notebook 1.
4. Comparisons and `if`; implement two different discount rules.
5. Lists and `for`; trace each loop iteration on paper.
6. Dictionaries and grouping; redo a previous exercise from a blank file.
7. Review errors; test your understanding with the Module 1 checkpoint. Continue the remaining module hours as needed.

## Module 0 — Set up your tools

### Understand the pieces

**Python** is a programming language. The **interpreter** is the program that executes Python instructions. **VS Code** is where you edit files; its Python extension connects it to an installed interpreter. A **terminal** accepts operating-system commands. A **notebook** mixes text, executable code cells, and output. Its **kernel** is a running interpreter that remembers values between cells.

A `.py` file is a script, executed from top to bottom. A `.ipynb` file is a notebook. A `.csv` file is a plain-text table. A package is reusable code installed into an environment. A virtual environment gives a project its own package set. These are different things; installing an editor does not install Python. See [Microsoft's Python setup guide](https://code.visualstudio.com/docs/python/python-tutorial).

### Recommended setup

Use VS Code with the Microsoft **Python** and **Jupyter** extensions, plus a stable Python 3 installation. For a new installation, choose the current stable installer from the [official downloads page](https://www.python.org/downloads/), not a preview release. An existing supported Python 3.12–3.14 installation is also a reasonable starting point. The supplied labs were verified on Python **3.12.14** with the exact library versions in `requirements.txt`; other interpreter/OS combinations were not exercised here. Obtain VS Code from [its official site](https://code.visualstudio.com/).

If you already have a working supported Python, verify it first. Do not replace macOS's system-managed software. Open the downloaded course folder using **File → Open Folder** in VS Code, then open **Terminal → New Terminal**. Type terminal commands into that panel, not into a Python file or the `>>>` Python prompt.

On macOS, verify that `python3` reports the version you chose, then create the environment:

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python --version
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If `python3` points to an older or unintended installation, use the chosen interpreter's explicit command (for example, `python3.14`) in the first two commands instead. Once the environment is active, use `python` consistently.

On Windows PowerShell:

```powershell
py -3 --version
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

These Windows commands call the environment directly and do not depend on PowerShell activation policy. In subsequent terminal examples, substitute `.\.venv\Scripts\python.exe` for `python` unless your terminal has already activated that environment.

`-m` tells Python to run an installed module. `venv` creates the environment; `pip` installs packages; `requirements.txt` records package versions. The leading dot makes `.venv` a hidden folder on some systems. More details: [Python's venv documentation](https://docs.python.org/3/library/venv.html).

In VS Code, open the Command Palette with **Cmd+Shift+P** on Mac or **Ctrl+Shift+P** on Windows. Choose **Python: Select Interpreter**, then the interpreter inside `.venv`. Open `notebooks/01_python_basics.ipynb`; use the notebook's **Select Kernel** control to choose the same environment. The script interpreter and notebook kernel can accidentally be different. [Notebook setup reference](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).

Create `hello.py` and enter:

```python
name = "Somrit"
study_minutes = 30
print(f"Hello, {name}. Today I will practice for {study_minutes} minutes.")
```

Save it. In the activated terminal, run `python hello.py`. Change 30 to 45 and rerun. The sentence should change. Now place a breakpoint by clicking beside a line number and run the debugger; inspect the variables and step through the program.

Verify the package setup in a notebook cell:

```python
import sys
import numpy as np
import pandas as pd
import sklearn
print(sys.executable)
print(np.__version__, pd.__version__, sklearn.__version__)
```

The executable should belong to your selected environment. Read `VALIDATION.md` to compare versions. You can study Modules 1–4 with Python alone; the data libraries become necessary in Module 5.

### Browser fallback

If local setup blocks your first session, use [Google Colab](https://colab.research.google.com/) to open a notebook, or use the browser environment offered by [CS50P](https://cs50.harvard.edu/python/). Google documents its browser-based ML exercises in the [ML prework guide](https://developers.google.com/machine-learning/crash-course/prereqs-and-prework). Save a downloaded copy of your work. When running Notebook 4 in a hosted environment, upload `orders.csv` and adjust its path. Complete local setup by Module 4 so you learn files, environments, and scripts. The supplied labs require no GPU.

### Troubleshooting you will actually use

| Symptom | Likely cause | First action |
|---|---|---|
| Command not found | Wrong command or interpreter not on the command search path | Restart terminal; verify the installed Python's command |
| `ModuleNotFoundError` | Package absent from this interpreter | Check `sys.executable`; install with that interpreter's `-m pip` |
| Terminal works, notebook fails | Different kernel | Select the `.venv` kernel and restart it |
| `FileNotFoundError` | Wrong working directory/path | Print `Path.cwd()` and inspect the file location |
| `SyntaxError` on `pip install` | Terminal command entered as Python | Move the command to the terminal |
| Notebook output seems impossible | Cells ran out of order | Restart the kernel and run every cell from the top |
| Installation wants to compile scientific libraries | Interpreter/platform mismatch or missing wheel | Confirm supported Python and library versions before changing tools |

**Checkpoint:** explain editor versus interpreter versus kernel; run a script; run a notebook; demonstrate that both use your environment; deliberately cause and fix a misspelled variable. Record what you did.

## Module 1 — Values, variables, and expressions

**Prerequisite:** Module 0. **Resource:** selected Functions/Variables material from [CS50P](https://cs50.harvard.edu/python/). If that feels too fast, substitute PY4E's Variables lesson from [its lesson sequence](https://www.py4e.com/lessons). Do not watch both courses in full.

A program is a sequence of precise instructions. Begin with **input → transformation → output**: receive quantities and prices, calculate a total, display it. Before writing code, write a concrete example with its expected answer.

```python
units = 3
unit_price = 12.50
subtotal = units * unit_price
discount_rate = 0.10
total = subtotal * (1 - discount_rate)
print(f"Total: {total:.2f}")  # Total: 33.75
```

`=` associates a name with a value; it does not mean mathematical equality. The right side is evaluated first. `count = count + 1` reads the old value and assigns the incremented value. Use names that explain meaning: `unit_price`, not `x`, unless doing a short mathematical example.

| Type | Example | Use |
|---|---|---|
| `int` | `3` | Whole numbers |
| `float` | `12.5` | Approximate real-number arithmetic |
| `str` | `"Dubai"` | Text |
| `bool` | `True` | Logical yes/no values |
| `NoneType` | `None` | Explicit absence of a value |

Use `type(value)` to inspect a type. Quotes matter: `"3"` is text, whereas `3` is numeric. `"3" + "4"` produces `"34"`; `3 + 4` produces `7`. `input()` returns text; convert it deliberately using `int()` or `float()` and handle invalid input when you learn exceptions.

Arithmetic operators: `+`, `-`, `*`, `/`, `//` (floor division), `%` (remainder), `**` (power). Parentheses make your intention clear. For positive quantities, `17 // 5` is 3 and `17 % 5` is 2. `-7 // 2` is -4 because flooring rounds down. `2 ** 3` is 8; `^` is not exponentiation in Python.

Computers approximate most decimal fractions using binary floating point. Do not expect `0.1 + 0.2 == 0.3` to hold. Use `math.isclose` for approximate comparisons. For real accounting systems use deliberate decimal or integer-minor-unit rules; this course's retail arithmetic is teaching arithmetic.

Strings have positions starting at zero:

```python
city = "Dubai"
print(city[0])      # D
print(city[-1])     # i
print(city[1:4])    # uba; stop position is excluded
clean_name = "  SOMRIT  ".strip().title()
print(clean_name)   # Somrit
```

A function call uses parentheses. A method is a function accessed through an object, such as `city.lower()`. A comment begins with `#`. An f-string embeds expressions inside braces. `:.2f` controls display precision; it does not change the stored value.

**Practice:** Notebook 1 and exercises 1–5. Predict every line before executing it. **Checkpoint:** write a price calculator from a blank file, handle text-to-number conversion on a valid input, explain all five types above, and fix one type error. You can look up formatting syntax.

## Module 2 — Decisions, repetition, and collections

**Resource:** CS50P's Conditionals and Loops; use [Helsinki Parts 1–4](https://programming-26.mooc.fi/) for extra short exercises where needed.

Comparisons such as `price > 100` produce booleans. Use `==` for equality, `!=` for inequality, and `and`, `or`, `not` to combine conditions. Use `is None` to test for the missing-value sentinel. Do not use `is` as a general numeric/string equality test.

```python
spend = 120
if spend >= 100:
    delivery_fee = 0
elif spend >= 50:
    delivery_fee = 5
else:
    delivery_fee = 10
```

Indentation defines a block: use four spaces consistently. Only the first true branch in this chain runs. Test boundaries: 49, 50, 99, 100. Many real bugs hide at boundaries, not typical inputs.

A list stores an ordered collection; a dictionary maps unique keys to values; a set stores unique values; a tuple groups items in an immutable sequence.

```python
amounts = [12, 8, 15]
total = 0
for amount in amounts:
    total += amount
print(total)  # 35

order = {"customer": "A", "amount": 12}
print(order["amount"])
print(order.get("coupon", "none"))
```

A `for` loop visits items. `range(3)` yields 0, 1, 2. `enumerate(items)` supplies positions and items; `zip(a, b)` pairs two collections and normally stops at the shorter one. A `while` loop repeats while a condition remains true; make sure some state changes so it can stop. `break` exits the loop; `continue` skips to its next iteration.

Think through a grouping operation:

```python
orders = [("A", 12), ("B", 8), ("A", 15)]
totals = {}
for customer, amount in orders:
    totals[customer] = totals.get(customer, 0) + amount
print(totals)  # {'A': 27, 'B': 8}
```

Trace the dictionary after each iteration. This same grouping idea reappears in pandas `groupby` and SQL `GROUP BY`.

Lists and dictionaries are mutable: they can change in place. `b = a` does not duplicate a list; both names refer to the same object. Use `a.copy()` for a shallow copy; nested mutable items still need care. Strings and tuples cannot have their elements reassigned. Prefer constructing a new list to removing elements while iterating over the original.

After you can write the loop, learn its compact form:

```python
large_amounts = [amount for amount in amounts if amount >= 10]
```

Do not compress complicated logic into a comprehension. Readability reduces mistakes. Know that looking for an item in a long list usually inspects items one by one; dictionary/set lookup is typically much faster. This intuition matters before formal algorithm analysis.

**Practice:** exercises 6–10. **Checkpoint:** summarize orders by customer, count unique customers, filter invalid amounts, and explain an empty-input case without copying an existing solution.

## Module 3 — Functions, debugging, tests, and objects

**Resources:** selected CS50P Functions, Exceptions, and Unit Tests topics. Use [Python's tutorial](https://docs.python.org/3/tutorial/index.html) as a lookup reference once the concepts make sense; it explicitly assumes prior general programming knowledge.

A function packages an operation so it can be reused and tested. A parameter names an input inside the definition; an argument is the value supplied in a call. `return` gives a result back to the caller. `print` only displays something. A function with no explicit return gives `None`.

```python
def discounted_total(prices, rate=0.0):
    """Return total after a fractional discount; reject invalid inputs."""
    if not 0 <= rate <= 1:
        raise ValueError("rate must be between 0 and 1")
    if any(price < 0 for price in prices):
        raise ValueError("prices must be nonnegative")
    return sum(prices) * (1 - rate)

result = discounted_total([10, 20], rate=0.1)
print(result)  # 27.0
```

`prices` and `rate` are local names. Keep inputs explicit rather than relying on changing global variables. A default argument is created once when the function is defined; avoid mutable defaults such as `items=[]`. Use `None` and create a new list inside when necessary.

Use exceptions to communicate errors. Catch the particular exception you can handle. A broad `except: pass` hides errors and often corrupts analysis silently. A traceback shows the call chain; read the final error type/message, then find the relevant line in your code.

Debugging sequence: reproduce the problem with the smallest input; state what you expected; inspect actual values and types; test one explanation; change one thing; rerun the original and boundary cases. Use breakpoints for changing state and `print` for a quick inspection.

```python
from math import isclose
assert isclose(discounted_total([10, 20], 0.1), 27)
assert discounted_total([], 0.2) == 0
assert discounted_total([10], 1) == 0

try:
    discounted_total([10], 1.5)
except ValueError:
    print("Invalid rate rejected correctly")
else:
    raise AssertionError("Expected a ValueError")
```

An assertion checks an assumption during development. It is not a replacement for validating external input, since Python can disable assertions. Later, put checks into a test runner. Learn the difference between syntax errors, runtime exceptions, and logic errors: a logic error can run successfully and still give a wrong answer.

Objects combine data and behavior. You already use them: a string has methods; a DataFrame will have columns and methods; a model will have `.fit()` and `.predict()`. A class defines a kind of object. Learn enough to read a small class with `__init__`, attributes, `self`, and a method. Extensive inheritance design can wait.

```python
class StudySession:
    def __init__(self, minutes):
        self.minutes = minutes

    def hours(self):
        return self.minutes / 60

session = StudySession(90)
assert session.hours() == 1.5
```

**Practice:** Notebook 2 and exercises 11–14. **Checkpoint:** write two reusable functions, test normal/boundary/invalid cases, fix a traceback, and explain `return`, scope, and a method call. Build a small receipt calculator without a tutorial.

## Module 4 — Files and small projects

**Resources:** CS50P File I/O and Libraries; PY4E Files and Web Services if you need another explanation. The supplied Notebook 2 uses local files and JSON with no network dependency.

An absolute path starts at the filesystem root; a relative path starts from your current working directory. `Path.cwd()` tells you where the program is looking. Use `pathlib` to construct paths instead of manually mixing slashes.

```python
from pathlib import Path
import csv
import json

path = Path("orders_small.csv")
path.write_text("customer,amount\nA,12\nB,8\nA,15\n", encoding="utf-8")

with path.open(encoding="utf-8", newline="") as handle:
    rows = list(csv.DictReader(handle))

total = sum(float(row["amount"]) for row in rows)
Path("summary.json").write_text(
    json.dumps({"total": total, "rows": len(rows)}, indent=2),
    encoding="utf-8",
)
```

CSV fields are initially text here. `with` closes the file even when an exception occurs. JSON represents nested objects, arrays, text, numbers, booleans, and null; it is a common API exchange format. An API is an agreed way for software to request information or actions. For a future network client, check HTTP status, set a timeout, handle failures, and validate the JSON shape before using it. Notebook 2 teaches response parsing through a local example.

Keep `data/raw/`, `data/clean/`, `notebooks/`, `src/`, and `reports/` as your own project grows. Preserve raw input; save cleaned outputs separately. A module is an importable Python file. Put reusable calculations in a module and exploratory work in a notebook. Avoid naming files `pandas.py`, `csv.py`, or `random.py`, which can hide the real library.

Use `if __name__ == "__main__":` around a script's entry point when you also want to import its functions without running the entire program. Read enough Git to make a local commit, inspect `git diff`, and restore a file deliberately; Module 13 covers the workflow.

**Practice:** exercise 15 and the first mini-project: a CSV expense analyzer that validates rows, totals by category, writes JSON, and has at least five meaningful tests. **Checkpoint:** another person can rerun it using your README and a new CSV. This completes the initial 44-hour Python foundation.

## Module 5 — NumPy and the math of arrays

**Resource:** selected array creation, indexing, shape, and aggregation sections of [NumPy's beginner guide](https://numpy.org/doc/stable/user/absolute_beginners.html). [Python for Data Analysis](https://wesmckinney.com/book/), Chapter 4, is an optional deeper companion.

NumPy operates on arrays of values efficiently. A vector is a one-dimensional collection; a matrix is a two-dimensional collection. A tensor generalizes the idea to other numbers of dimensions. In ML, a common matrix shape is `(number_of_examples, number_of_features)`.

```python
import numpy as np

quantities = np.array([2, 1, 3])
prices = np.array([10.0, 25.0, 8.0])
revenues = quantities * prices
print(revenues)        # [20. 25. 24.]
print(revenues.sum())  # 69.0

X = np.array([[2.0, 10.0], [1.0, 25.0], [3.0, 8.0]])
print(X.shape)        # (3, 2)
print(X.mean(axis=0))  # one mean per column
```

`axis=0` reduces down the rows; `axis=1` reduces across columns for a 2D array. Write the shape beside each operation until it becomes natural. `*` is elementwise multiplication; `@` is matrix multiplication. A dot product multiplies corresponding vector entries and adds the results: `[2, 3] @ [10, 4] = 32`.

A linear prediction is a weighted sum plus an intercept: `prediction = X @ weights + bias`. If `X` is `(100, 3)`, `weights` is `(3,)`, the result is `(100,)`. This is the same arithmetic as a price calculator, now applied to many examples.

Broadcasting allows some differently shaped arrays to interact; for example subtracting a `(3,)` column-mean vector from a `(100, 3)` matrix. Shapes match from the right when dimensions are equal or one is 1. Accidental `(n, 1)` versus `(n,)` combinations can produce `(n, n)` results, so inspect shape before trusting arithmetic.

Use boolean masks for filtering: `revenues[revenues > 20]`. Use `np.random.default_rng(42)` for repeatable random examples. A seed supports reproducibility; it does not make a dataset representative. Some slices share underlying memory; explicitly copy when independence matters.

**Practice:** Notebook 3, exercises 16–18. **Checkpoint:** calculate per-column means, filter rows, distinguish `*` from `@`, and predict the shapes of three operations before running them.

## Module 6 — pandas and trustworthy data

**Resource:** [pandas getting-started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html): read/write, subsets, new columns, summaries, combining tables, and dates. Use Chapters 7, 8, and 10 of Python for Data Analysis selectively when stuck; the book uses older library versions, so consult current documentation for changed APIs.

A pandas **Series** is a labeled one-dimensional sequence. A **DataFrame** is a labeled table with potentially different types in each column. An index labels rows; it is not automatically a trustworthy business identifier.

Before analyzing data, state its **grain**: what does one row represent? In the supplied retail file, each valid business record is one order with one product; repeated rows and invalid values were planted for practice. Read `data/README.md` before choosing a cleaning rule.

```python
import pandas as pd

orders = pd.DataFrame({
    "customer": ["A", "B", "A"],
    "units": [2, 1, 3],
    "price": [10.0, 25.0, 8.0],
})
orders["revenue"] = orders["units"] * orders["price"]
summary = orders.groupby("customer", as_index=False)["revenue"].sum()
print(summary)
```

Initial inspection: `head()`, `shape`, `info()`, `describe()`, `isna().sum()`, and identifier duplicate counts. Read dates explicitly; check units, currency, valid ranges, categories, and missingness. Blank values do not all mean zero. A missing price cannot safely become a free order.

Use `.loc[rows, columns]` for labels and boolean selection; `.iloc` for integer positions. For assignments use a single `.loc` operation instead of chained indexing. Example: `df.loc[df["units"] < 0, "needs_review"] = True`. Treat pandas warnings as something to understand, not silence.

Use vectorized column operations before reaching for row-by-row `apply`. For categories, normalize casing and whitespace only when those differences are not meaningful. Record every excluded row and the reason. A duplicate customer is not a duplicate order; deduplication depends on grain and business meaning.

A merge combines tables on keys. A many-to-many merge can multiply rows and inflate totals. Use `validate="many_to_one"` when adding a customer dimension to orders, check unmatched keys with `indicator=True`, and reconcile row counts and total amounts. `concat` stacks compatible tables; `pivot_table` reshapes aggregated data.

For dates, learn `pd.to_datetime`, `.dt`, sorting, and resampling. A zero-sales date and a missing date are different. For time zones, define the business day before grouping. Never draw a trend from dates that are still unsorted strings.

Notebook 4 walks through explicit cleaning rules, exclusion counts, validated joins, aggregation, and CSV output. Its conclusions apply only to the synthetic practice data. Do not infer facts about an actual retailer.

**Practice:** exercises 19–22. **Checkpoint:** take the supplied CSV, document grain and cleaning policy, reconcile raw/duplicate/rejected/clean counts, validate a merge, and give three findings with denominators and units. Your cleaned result must rerun from raw input.

## Module 7 — SQL and charts that answer a question

**Resources:** [Python's SQLite documentation](https://docs.python.org/3/library/sqlite3.html) for connection/parameter examples; [Matplotlib quick start](https://matplotlib.org/stable/users/explain/quick_start.html) for figure and axes usage. Use the supplied SQL notebook as the guided lesson.

SQL asks questions of tables in a database. Start with `SELECT` (columns), `FROM` (table), `WHERE` (filter rows), `GROUP BY` (aggregate groups), `HAVING` (filter groups), and `ORDER BY` (sort results). `COUNT(*)` counts rows; `COUNT(column)` counts non-null entries. Use `IS NULL`, not `= NULL`.

```sql
SELECT customer, SUM(amount) AS total_amount
FROM orders
WHERE amount > 0
GROUP BY customer
HAVING SUM(amount) >= 20
ORDER BY total_amount DESC;
```

An inner join retains matched rows; a left join retains all left rows and attaches matches when present. A condition on the right table in `WHERE` can accidentally remove unmatched rows after a left join. Learn join keys and cardinality before combining large tables. Use parameter binding for values supplied from outside the program; do not build SQL by concatenating input strings.

Produce the same grouped result once in pandas and once in SQL and compare them. This is a useful independent check of your interpretation. Later learn common table expressions and window functions for ranking or running totals; they are optional extensions after the core exercise.

Choose a chart from the question: a bar chart compares categories, a line chart shows ordered change over time, a histogram shows one distribution, a scatter plot explores the relationship between two numeric variables. Label title, axes, units, period, and source. Bars should normally start at zero because their length carries the value. A histogram's bin choices affect the impression; inspect more than one sensible bin width.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 3.5))
ax.bar(["A", "B"], [44, 25])
ax.set(title="Synthetic revenue by customer", xlabel="Customer", ylabel="Revenue (AED)")
fig.tight_layout()
plt.show()
```

Write a finding as: **observation → evidence → interpretation → limitation**. Example: “Customer A accounts for 44 of 69 AED in this three-order example. That concentration is visible in the totals, but three invented orders cannot establish a repeat-purchase pattern.” A chart is evidence for a bounded claim, not decoration.

**Practice:** Notebook 5, exercises 23–25. **Checkpoint:** correctly filter and aggregate with SQL; explain a left join; create three appropriate labeled charts; write a one-page analytical memo that distinguishes data from conjecture.

## Module 8 — Statistics and uncertainty

**Resource:** selected data summaries, probability, sampling, and inference topics from [OpenIntro Statistics](https://www.openintro.org/book/os/). Google's [ML prerequisite guide](https://developers.google.com/machine-learning/crash-course/prereqs-and-prework) is a useful checklist of the algebra needed next.

A population is the group you want to understand; a sample is what you observe. A mean uses every numeric value and can be moved by extreme values; a median is the middle ordered value. Standard deviation describes spread. A percentile marks a point below which a specified proportion falls, subject to the percentile convention used. Always inspect the distribution as well as a summary.

For values `[10, 10, 10, 100]`, the mean is 32.5 and median 10. Neither is “the correct average” without a question. The mean helps reconcile total spending; the median describes a typical middle observation here.

Rates need denominators. If group A has 20 conversions from 100 visitors and B has 12 from 40, their rates are 20% and 30%. The difference is **10 percentage points**, or a **50% relative increase** compared with A. It is not a 10% relative increase. Pooling groups can change the conclusion when their compositions differ.

Probability describes uncertainty on a 0–1 scale. Conditional probability changes the reference group: `P(purchase | clicked)` concerns people who clicked. Bayes' rule reverses conditioning using the base rate. A rare event can produce many false alarms even with a seemingly accurate classifier.

Sampling variation means different samples give different estimates. Standard error describes estimator variability, whereas standard deviation describes the spread of observations. More data reduces random sampling error under suitable conditions, but does not automatically repair biased sampling or bad labels.

A confidence interval comes from a procedure with a stated long-run coverage under assumptions; it is not, in frequentist interpretation, a post-data probability assigned to one fixed parameter. A p-value is the probability, under a specified null model, of results at least as extreme as observed according to the chosen test. It is not the probability the null is true. Report effect size and uncertainty, not just a threshold crossing.

A bootstrap repeatedly resamples the observed data with replacement to estimate a statistic's variability. Notebook 3 illustrates a percentile interval for a mean under an independent-observation assumption. Dependent time series or repeated-customer observations need different resampling designs. A convenient interval is not automatically valid.

Correlation measures association and cannot alone establish causation. A campaign's sales may rise because of seasonality, selection, or simultaneous changes. A randomized experiment can support a causal comparison when assignment and analysis are sound. Decide the metric, eligibility, unit of randomization, duration, and stopping rule before inspecting outcomes. Repeatedly checking until something looks significant changes error rates.

Math to know before ML: fractions and percentages; algebraic variables; functions and graphs; a line `y = b + wx`; summation as repeated addition; vectors and dot products; logarithms as inverses of exponentials; the idea of slope. Full calculus proofs can follow later, but understand how a small change in a weight changes an error.

**Practice:** exercises 26–29 and Notebook 3's statistics section. **Checkpoint:** explain mean versus median, compute weighted rates, interpret uncertainty without overclaiming, identify a confounder, and propose an appropriate sampling unit.

## Module 9 — Your first honest machine-learning workflow

**Resources:** Google's [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) for linear/logistic regression, classification, and generalization; the [Inria scikit-learn course](https://inria.github.io/scikit-learn-mooc/) for tabular workflows and pipelines. These resources assume Python familiarity, which you now have.

AI is the broad field of building systems that perform tasks associated with intelligence. ML learns patterns from examples. Deep learning uses neural networks with multiple layers. Analytics describes and investigates data; ML predicts or identifies structure. A useful rule or SQL query may solve a problem without ML.

In **supervised learning**, each example has input features `X` and a target `y`. Regression predicts a number, such as delivery minutes. Classification predicts a category, such as a document topic. In **unsupervised learning**, there is no supplied target; clustering groups similar examples, and dimensionality reduction finds a smaller representation. Reinforcement learning concerns actions, rewards, and sequential decisions; it is a later specialization.

Start by writing: “At time T, using information available by T, predict Y for population P so that someone can do action A.” That sentence determines which features are legitimate, how data should be split, and which errors matter.

Then follow this sequence:

1. Define the observation unit, prediction moment, target, and useful metric.
2. Reserve an untouched test set using a split that matches future use.
3. Explore and develop on training data; use validation or cross-validation for choices.
4. Build a trivial baseline before a more complex model.
5. Fit preprocessing and model together in a pipeline.
6. Compare candidates using training-side validation only.
7. Freeze the decision, then evaluate once on the test set.
8. Inspect errors and state limitations; further changes require fresh evaluation evidence.

Random splits suit some independent examples. Forecasting usually needs earlier data for training and later data for evaluation. Multiple rows from one person or device often need a group split. Randomly separating near-duplicate rows can make a model look excellent while testing memorization.

**Leakage** occurs when information unavailable in actual prediction enters learning or evaluation. Examples: including an eventual refund outcome to predict refunds earlier, fitting a scaler on the entire dataset, tuning against the test score, or letting the same customer appear on both sides when evaluating new-customer performance. [scikit-learn's common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) explain why pipelines help keep fitted preprocessing inside training folds.

A model's `.fit(X, y)` learns from data. `.predict(X)` produces outputs for supplied inputs. A scaler's `.fit` learns training means/spreads and `.transform` applies them. The test set gets `.transform`, never `.fit` or `.fit_transform`.

For regression, mean absolute error (MAE) is the average absolute prediction error in target units. Root mean squared error (RMSE) penalizes large errors more strongly and also uses target units. `R²` compares squared error with a constant-mean reference and can be negative on new data. Use a dummy mean or median predictor as a baseline.

For classification, a confusion matrix counts true/false positives/negatives for a defined positive class. Accuracy is the fraction correct; precision is `TP/(TP+FP)`; recall is `TP/(TP+FN)`; F1 is their harmonic mean. Specify how undefined cases are handled. A 99% negative dataset allows 99% accuracy by always guessing negative. Use metrics and thresholds that reflect error costs, class balance, and intended use.

Notebook 6 compares a dummy model with a linear model and a tree ensemble, using a preprocessing pipeline and training-side cross-validation. Its generated regression data are a controlled teaching problem, not evidence of business value.

**Practice:** exercises 30–32. **Checkpoint:** explain every step in your pipeline; choose an appropriate split; beat or honestly fail to beat a baseline; report the test metric only after model selection; identify two plausible leakage routes.

## Module 10 — Model selection and error analysis

**Resources:** Inria's cross-validation and tree-ensemble sections; selected model assessment/resampling material from [An Introduction to Statistical Learning, Python edition](https://www.statlearning.com/). Use the textbook for depth after the lab, not as another start-to-finish prerequisite.

Linear regression fits a weighted sum. Logistic regression uses a transformed weighted sum for classification. A decision tree partitions feature space using questions. Random forests combine many varied trees; boosting builds an ensemble by sequentially addressing an objective. A neural network learns layers of transformations. Model choice depends on data and constraints; more complicated is not automatically more useful.

Underfitting means the model misses important patterns; overfitting means it captures training-specific patterns that do not generalize. Compare training and validation error. A large gap can indicate overfitting; high error on both can indicate insufficient features, a poor model class, wrong assumptions, or irreducible uncertainty. More data helps some of these problems, not all.

Parameters are learned quantities such as coefficients. Hyperparameters are choices such as tree depth or regularization strength. Regularization discourages excessive complexity. Cross-validation rotates held-out folds within training data to assess candidates. Report its spread as descriptive fold variability, not automatically a confidence interval.

Tune a small, reasoned set of choices. Keep preprocessing inside the cross-validation pipeline. Decide the metric first. Every additional search opportunity risks fitting your development process to the validation evidence. Keep an experiment table recording hypothesis, change, split, metric, cost, and decision.

Missing numeric values may be imputed using training medians; categories may use one-hot encoding with an explicit policy for unseen values. Use `ColumnTransformer` when columns need different processing. Decide whether missingness itself carries useful information and whether that pattern will persist.

Clustering and principal component analysis (PCA) can be useful exploratory tools. Scaling and distance choice affect results. A cluster is not automatically a meaningful customer segment; validate stability and usefulness. PCA directions summarize variance, not necessarily predictive or causal importance.

Inspect errors by meaningful slices, such as product type or month, including sample counts. Feature importance describes the fitted model under a method's assumptions; it does not establish causality. Correlated features can make importance unstable. Calibration concerns whether predicted probabilities match observed event frequencies; ranking quality alone does not guarantee it.

**Practice:** exercises 33–35; extend Notebook 6 with one predeclared training-side experiment. **Checkpoint:** justify a candidate change, compare it fairly, explain a failure slice, distinguish parameter from hyperparameter, and resist further tuning on the final test result.

## Module 11 — Neural networks without mystery

**Resources:** selected neural-network sections of Google MLCC; [PyTorch Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) for the next framework step. [fast.ai](https://course.fast.ai/) becomes useful once you can code comfortably; it is not your day-one Python teacher.

A neuron forms a weighted sum plus a bias, then applies a nonlinear activation. Layers compose these operations. Nonlinearity lets the model represent relationships a single linear transformation cannot. A loss measures the discrepancy between prediction and target. Training adjusts weights to reduce that loss.

For a simple model `prediction = weight * x + bias`, mean squared loss is the average of `(prediction - target) ** 2`. A derivative describes the local sensitivity to a change. A gradient collects those sensitivities for all trainable parameters.

Gradient descent repeats: predict → calculate loss → calculate gradients → move parameters a small distance opposite the gradient. The learning rate controls that distance. Too large can diverge; too small can learn slowly. Backpropagation efficiently applies the chain rule through a network to compute gradients; it is not a separate model.

An epoch is one pass over the training set. A batch is a subset processed in one update. Inference uses learned weights without updating them. For reproducibility, record data, splits, versions, seeds, and training settings; a seed alone does not guarantee bit-identical results on every device.

Notebook 7 first implements gradient descent for a line using NumPy, so you can see the arithmetic. It then compares a linear classifier with a small neural network on a nonlinear synthetic dataset. This is a neural-network foundation exercise, not large-scale deep learning. It runs on a CPU with scikit-learn.

For a subsequent PyTorch implementation, understand tensors, `Dataset`/`DataLoader`, `nn.Module`, the forward pass, loss, `zero_grad`, `backward`, and the optimizer step. Learn `model.train()` versus `model.eval()` and disabled gradient tracking at inference. Follow the current official installation selector when you reach this optional framework extension; PyTorch is not required for the supplied labs.

**Practice:** exercises 36–37. **Checkpoint:** explain why weights change, show loss reduction, recognize a learning-rate failure, and explain why a nonlinear hidden layer can help a curved decision boundary. Do not infer that a neural network is best for ordinary tabular data from this deliberately nonlinear example.

## Module 12 — Text, retrieval, and modern language AI

**Resource:** [Hugging Face's LLM course introduction and first chapter](https://huggingface.co/learn/llm-course/chapter1/1), then its model-use material as an extension. The full course expects solid Python and recommends prior deep-learning foundations. Its later fine-tuning chapters are for later study.

NLP works with language data. A token is a unit used by a tokenizer; it may be part of a word. A representation converts text into numbers. TF-IDF weights terms using their frequency within a document and their prevalence across a document collection. An embedding is a numeric representation, often learned, that can capture relationships beyond exact term overlap.

Notebook 8 builds a local retrieval system over a small invented document collection. It vectorizes documents, compares a query using cosine similarity, returns ranked passages, and evaluates a fixed set of questions. This is lexical search; it contains no language model and generates no answers. That distinction matters when evaluating what a system can do.

A transformer uses attention to combine information across token positions. Many generative language models predict a distribution over the next token repeatedly, conditioned on the current context. Pretraining learns broad patterns; fine-tuning further updates weights for selected data/objectives. Prompting supplies instructions and context at inference without necessarily changing weights.

A retrieval-augmented generation application has two parts: retrieve relevant evidence, then provide it to a generator to help produce an answer. Measure them separately. Good retrieval does not guarantee a faithful answer; fluent prose does not prove that retrieval succeeded. A context window limits how much text a model processes in one request.

Design your first AI app before adding frameworks:

1. Define a narrow task, such as answering questions about a small handbook.
2. Make 20–30 representative questions with expected evidence, including missing-answer cases.
3. Establish a simple retrieval or rules baseline.
4. If adding a generator, specify evidence citation and an “insufficient information” response.
5. Evaluate correctness, support in sources, rejection of unanswerable questions, latency, and cost.
6. Keep credentials in environment variables, set usage limits, and log only appropriate data.

Retrieved pages and user-provided documents are data, not instructions that should override the application's rules. Prompt injection occurs when untrusted content tries to redirect the system. Keep tool permissions narrow, validate inputs/outputs, and require explicit authorization for consequential external actions.

The core exercise uses no paid API. A real hosted or local LLM integration is an optional next project after this course; it requires choosing a provider/model, checking current documentation and terms, and then testing actual behavior. Reading a simulated API response is not the same as completing that integration.

**Practice:** Notebook 8 and exercise 38. **Checkpoint:** distinguish retrieval from generation, prompting from training, and lexical vectors from learned embeddings; measure retrieval quality; design an evaluation set that includes failures.

## Module 13 — Make your work usable by someone else

Reproducibility means a person can follow your instructions, use the specified input, and obtain materially consistent results. Restart every notebook and run from the first cell. Extract reusable processing into functions or scripts. Record package versions and data provenance. Separate inputs, outputs, configuration, and credentials.

Create a README containing the question, data origin, setup commands, run order, output locations, tests, results, and limitations. Record dependency versions with `python -m pip freeze > environment-freeze.txt` in your project environment. A dependency list is useful but is not a universal cross-platform lockfile.

Use Git locally to track deliberate changes:

```bash
git init
git status
git add README.md src tests
git diff --staged
git commit -m "Add reproducible analysis and input checks"
```

These commands assume you created `src/` and `tests/` and configured Git. Install/learn Git from [the official documentation](https://git-scm.com/doc). Git tracks changes locally; a remote hosting service is a separate optional step. Put `.venv/`, private data, credentials, and generated caches in `.gitignore`; do not publish them accidentally.

Record a model's intended use, training population, evaluation split, metrics, limitations, and unsuitable uses. Monitor input changes and performance where labels become available. Data drift is a change in inputs; concept drift is a change in the relation between inputs and target. Neither automatically tells you which repair is appropriate.

Respect data permissions. Check representativeness, labeling quality, and performance differences across relevant groups with adequate sample sizes. A statistically better model can still be unusable because of delay, cost, harmful errors, or inaccessible explanations. Avoid running serialized models from untrusted sources; some serialization formats can execute code when loaded.

**Practice:** exercise 39. **Checkpoint:** rerun in a fresh kernel, provide a clear setup/run path, demonstrate a failed-input check, and explain what would have to be monitored after deployment. Public deployment is not required for course completion.

## Module 14 — Independent capstone

### Required project: answer a question, then predict something useful

Choose a public dataset with a documented origin and license, or an authorized dataset from your own work. Define a narrowly bounded question and prediction target. The synthetic course data can be used for rehearsal, but the final independence check should use a different dataset with unfamiliar imperfections. Dataset choice should serve the question, not just a leaderboard.

Suggested theme: **retail operations**. First identify how order value or delivery performance varies by a useful segment. Then predict a future quantity or category using only information available at the prediction moment. If the chosen data lack a legitimate target or timing information, change the question or select another dataset; do not invent a causal story or a predictive task that leaks the answer.

Allocate the 20 hours: 2 for question and dataset inspection; 4 for cleaning and tests; 4 for analysis and charts; 5 for modeling and evaluation; 3 for error analysis and writing; 2 for independent rerun and presentation. Add time when data access or quality demands it.

Deliver:

- A README, source/license note, and data dictionary with grain and units.
- Raw-data checks, explicit cleaning decisions, exclusion counts, and at least five useful tests.
- At least three question-driven charts and one SQL query reconciled to a pandas result.
- A declared split, baseline, and at most three reasoned model candidates compared on training-side validation.
- A final evaluation after selection, error examples, and limitations on generalization.
- A one-page memo containing findings, practical implications, and what the evidence cannot establish.
- A rerunnable notebook or script and dependency record.

### Rubric

| Area | Points | Evidence |
|---|---:|---|
| Problem definition | 10 | Clear population, unit, target, prediction time, decision |
| Data understanding and cleaning | 20 | Provenance, reconciliation, justified decisions |
| Python and reproducibility | 20 | Readable functions, tests, fresh rerun, instructions |
| Analysis and communication | 15 | Correct metrics, charts, denominators, careful claims |
| Modeling and evaluation | 25 | Baseline, valid split, leakage controls, fair selection |
| Error analysis and limitations | 10 | Concrete failure cases and practical boundaries |
| **Total** | **100** | |

Pass at **80/100**, with no critical failure. Leakage, fabricated data provenance, a wrong central denominator, or inability to rerun are critical failures regardless of total score. Repair and resubmit. Use the rubric with a knowledgeable reviewer when possible; self-assessment is less reliable than external review.

Your final demonstration: in 10 minutes, explain the question, inspect a raw row, trace it through cleaning, justify the split and baseline, interpret one error, and rerun a small piece live. Then do exercise 40 with unfamiliar inputs.

### What to learn next

For **analytics**, deepen SQL joins/window functions, experimental design, domain metrics, time series, and communication. Build two more independent reports using different data grains.

For **ML engineering**, add stronger testing, packaging, APIs, containers, deployment, monitoring, time/group evaluation, and a real PyTorch project. Work through the relevant ISLP chapters and remaining Inria modules.

For **AI applications**, continue directly into the [40-hour application and career bridge](BRIDGE.html): serve a trained model, evaluate a pretrained text model, and build a narrow document assistant with repeatable evaluations and permission boundaries. Then deepen Hugging Face or fast.ai study. Do not begin by training a large language model from scratch.

For **career preparation**, add collaborative Git work, code review, two further original projects, SQL practice, mathematical depth, and explaining tradeoffs aloud. This crash course establishes the base; employability depends on the role and the quality of the work you can independently demonstrate.

## Quick-reference desk card

| Need | Python pattern |
|---|---|
| Inspect a value | `print(value)`, `type(value)` |
| Inspect a table | `df.head()`, `df.info()`, `df.shape` |
| Make a function | `def name(inputs): ... return result` |
| Filter a list | `[x for x in values if condition]` |
| Count/group | Dictionary loop, `groupby`, or SQL `GROUP BY` |
| Read a CSV | `pd.read_csv(path)` |
| Filter rows | `df.loc[condition].copy()` |
| Check missingness | `df.isna().sum()` |
| Validate an identifier | `df["id"].is_unique` |
| Join safely | `left.merge(right, on="id", validate="many_to_one")` |
| Inspect working folder | `Path.cwd()` |
| Install a package | Terminal: `python -m pip install package_name` |
| Fit a model | `pipeline.fit(X_train, y_train)` |
| Predict | `pipeline.predict(X_test)` |
| Repair strange notebook state | Restart kernel, run all cells |

Keep [the glossary](GLOSSARY.html), [exercise workbook](PRACTICE.html), and [source evaluation](SOURCES.html) beside the handbook. You are learning a way of reasoning: define the problem, inspect the evidence, write a small solution, check it, and explain its limits.
