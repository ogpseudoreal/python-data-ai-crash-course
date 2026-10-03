"""Build the original teaching notebooks and synthetic course dataset."""
from pathlib import Path
import csv
import json
import textwrap
import nbformat as nbf

ROOT = Path(__file__).resolve().parent
NOTEBOOKS = ROOT / "notebooks"
DATA = ROOT / "data"
NOTEBOOKS.mkdir(exist_ok=True)
DATA.mkdir(exist_ok=True)

def md(text):
    return nbf.v4.new_markdown_cell(textwrap.dedent(text).strip())

def code(text):
    return nbf.v4.new_code_cell(textwrap.dedent(text).strip())

def save(name, cells):
    nb = nbf.v4.new_notebook(cells=cells)
    nb.metadata.kernelspec = {"display_name": "Python 3", "language": "python", "name": "python3"}
    nb.metadata.language_info = {"name": "python", "version": "3.12"}
    nbf.validate(nb)
    nbf.write(nb, NOTEBOOKS / name)

rows = []
for i in range(60):
    rows.append({
        "order_id": f"O{i:03d}", "date": f"2026-01-{1+i//4:02d}",
        "customer_id": f"C{i%12:02d}", "region": ["North", "South", "East"][i%3],
        "units": 1+i%4, "unit_price": [10, 20, 30, 15, 25][i%5],
    })
rows[4]["units"] = -1
rows[7]["unit_price"] = ""
rows[10]["date"] = "not-a-date"
rows[13]["units"] = "two"
rows[16]["region"] = ""
for i in [5, 20, 35, 50]:
    rows[i]["region"] = "  " + rows[i]["region"].lower() + " "
rows += [rows[0].copy(), rows[1].copy()]
with (DATA / "orders.csv").open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

save("01_python_basics.ipynb", [
md("""
# 1. Python from zero
## Goal
Read and change a small program using values, decisions, collections, and loops.
Course Modules 1–2. Predict each output before running it. All data are invented.
## Setup
Select your course Python kernel. This notebook uses only Python's standard library.
Reference: [CS50P](https://cs50.harvard.edu/python/).
## Steps
### 1. Calculate and format
The right side of an assignment is evaluated before its result is assigned to the name on the left.
"""),
code('''
quantity = 3
unit_price = 12.50
discount_rate = 0.10
delivery_fee = 5
total = quantity * unit_price * (1 - discount_rate) + delivery_fee
print(f"Total: {total:.2f} AED")
assert total == 38.75
'''),
md("""
### 2. Inspect types and text
Quotes make a value text. Calling `float` converts valid numeric text into a number.
"""),
code('''
text_quantity = "4"
text_price = "7.5"
print(text_quantity * 2)
numeric_total = int(text_quantity) * float(text_price)
print(numeric_total, type(numeric_total).__name__)
name = "  sOMRIt  ".strip().title()
print(name, name[0], name[-1])
assert numeric_total == 30
assert name == "Somrit"
'''),
md("### 3. Make a decision\nTest the boundaries; only the first matching branch runs."),
code('''
spend = 50
if spend >= 100:
    fee = 0
elif spend >= 50:
    fee = 5
else:
    fee = 10
print("Delivery:", fee)
assert fee == 5
'''),
md("### 4. Group values with a loop\nTrace the dictionary after each order."),
code('''
orders = [("A", 12), ("B", 8), ("A", 15)]
totals = {}
for customer, amount in orders:
    totals[customer] = totals.get(customer, 0) + amount
    print(customer, amount, totals.copy())
assert totals == {"A": 27, "B": 8}
'''),
md("### 5. Check shared objects\nTwo names can refer to the same list. A shallow copy separates the outer list."),
code('''
a = [1, 2]
b = a
b.append(3)
print("a after editing b:", a)
c = a.copy()
c.append(4)
print("a:", a, "c:", c)
assert a == [1, 2, 3]
assert c == [1, 2, 3, 4]
'''),
md("""
## Checks
The assertions confirm this worked example. Your skill check is separate: in a new cell, summarize a different list of orders without looking at Step 4, then test an empty list.
## Next Steps
Complete exercises 1–10 as you finish Modules 1–2. Explain `=` versus `==`, strings versus numbers, and why a loop updates a dictionary. Restart the kernel and run all cells before saving.
"""),
])

save("02_functions_files_tests.ipynb", [
md("""
# 2. Reusable functions, files, and checks
## Goal
Turn a calculation into tested reusable code and read/write CSV and JSON.
Course Modules 3–4. All example data are invented.
## Setup
Standard library only. Files are written to a temporary directory and removed automatically.
Reference: [Python standard library](https://docs.python.org/3/library/).
## Steps
### 1. Define a contract
A function returns a result. Invalid data are rejected, and an empty basket totals zero.
"""),
code('''
from math import isclose, isfinite
def discounted_total(prices, rate=0.0):
    """Total finite nonnegative prices using a finite discount from 0 to 1."""
    if not isfinite(rate) or not 0 <= rate <= 1:
        raise ValueError("rate must be finite and between 0 and 1")
    if any(not isfinite(price) or price < 0 for price in prices):
        raise ValueError("prices must be finite and nonnegative")
    return sum(prices) * (1 - rate)

print(discounted_total([10, 20], 0.1))
'''),
md("### 2. Test behavior\nTests include boundaries and invalid values, not only the usual input."),
code('''
assert isclose(discounted_total([10, 20], 0.1), 27)
assert discounted_total([], 0.5) == 0
assert discounted_total([20], 1) == 0
for prices, rate in [([-1], 0), ([10], 1.5), ([float("nan")], 0)]:
    try:
        discounted_total(prices, rate)
    except ValueError:
        pass
    else:
        raise AssertionError("Invalid input was accepted")
print("Normal, boundary, and invalid-input checks passed.")
'''),
md("### 3. Read records and write a summary\nCSV numeric fields are text until converted. The context managers close files and clean up the temporary folder."),
code('''
import csv
import json
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    source = Path(folder) / "expenses.csv"
    source.write_text("category,amount\\nFood,12\\nTravel,8\\nFood,15\\n", encoding="utf-8")
    with source.open(newline="", encoding="utf-8") as handle:
        records = list(csv.DictReader(handle))
    totals = {}
    for record in records:
        category = record["category"]
        totals[category] = totals.get(category, 0) + float(record["amount"])
    output = Path(folder) / "summary.json"
    output.write_text(json.dumps(totals, indent=2), encoding="utf-8")
    restored = json.loads(output.read_text(encoding="utf-8"))
    print(restored)
    assert restored == {"Food": 27.0, "Travel": 8.0}
'''),
md("### 4. Parse an API-shaped response\nThis is a local string, not a live network request. Validate the structure you rely on."),
code('''
payload = '{"status": "ok", "items": [{"id": 1, "amount": 12}]}'
response = json.loads(payload)
if response.get("status") != "ok" or not isinstance(response.get("items"), list):
    raise ValueError("Unexpected response shape")
print(response["items"][0]["amount"])
'''),
md("""
## Checks
All assertions should pass from a fresh kernel. Explain why the `except` block is narrow and why JSON parsing alone does not validate business meaning.
## Next Steps
Complete exercises 11–15. Your CSV mini-project should preserve raw data, record rejected rows, and handle a new file. Add meaningful tests rather than copying the function's implementation into a test.
"""),
])

save("03_numpy_statistics.ipynb", [
md("""
# 3. Arrays and uncertainty
## Goal
Understand array shapes, weighted sums, summaries, and a simple bootstrap.
Course Modules 5 and 8. Work through Steps 1–3 in Module 5; return for Steps 4–5 in Module 8.
## Setup
Uses NumPy and Matplotlib. All data are invented or simulated.
References: [NumPy basics](https://numpy.org/doc/stable/user/absolute_beginners.html), [OpenIntro Statistics](https://www.openintro.org/book/os/).
## Steps
### 1. Use arrays and inspect their shape
"""),
code('''
import numpy as np
import matplotlib.pyplot as plt

quantities = np.array([2, 1, 3])
prices = np.array([10.0, 25.0, 8.0])
revenue = quantities * prices
print(revenue, revenue.sum())
X = np.array([[1., 10.], [2., 20.], [3., 30.]])
print("Shape:", X.shape, "Column means:", X.mean(axis=0))
assert revenue.sum() == 69
assert X.mean(axis=0).shape == (2,)
'''),
md("### 2. Standardize with an explicit constant-column policy\nUse training statistics on later data. Here the same small array is only an arithmetic demonstration."),
code('''
means = X.mean(axis=0)
scales = X.std(axis=0, ddof=0)
safe_scales = np.where(scales == 0, 1, scales)
standardized = (X - means) / safe_scales
print(standardized)
assert np.allclose(standardized.mean(axis=0), 0)
assert np.allclose(standardized.std(axis=0), 1)
weights = np.array([2., 0.5])
predictions = X @ weights + 1
print("Weighted predictions:", predictions)
assert predictions.shape == (3,)
'''),
md("### 3. Compare mean and median\nA typical middle observation and a total-reconciling average answer different questions."),
code('''
values = np.array([10., 10., 10., 100.])
print("Mean:", values.mean(), "Median:", np.median(values))
assert values.mean() == 32.5
assert np.median(values) == 10
pooled_rate = (20 + 12) / (100 + 40)
print(f"Pooled conversion rate: {pooled_rate:.3%}")
'''),
md("""
### 4. Simulate a bootstrap distribution
Assumption: these 80 simulated waiting times are independent observations from one stable process. The percentile interval illustrates uncertainty for the mean under this design. It does not validate the independence assumption for real data.
"""),
code('''
rng = np.random.default_rng(42)
waiting_minutes = rng.gamma(shape=3, scale=4, size=80)
samples = rng.choice(waiting_minutes, size=(3000, len(waiting_minutes)), replace=True)
bootstrap_means = samples.mean(axis=1)
low, high = np.percentile(bootstrap_means, [2.5, 97.5])
print(f"Sample mean: {waiting_minutes.mean():.2f} minutes")
print(f"Illustrative 95% percentile bootstrap interval: [{low:.2f}, {high:.2f}] minutes")
assert low < high
'''),
md("### 5. Plot the simulated sampling variation\nThis distribution is over resampled means, not individual customer waiting times."),
code('''
fig, ax = plt.subplots(figsize=(7, 3.5))
ax.hist(bootstrap_means, bins=30, color="#147d92", edgecolor="white")
ax.axvline(low, color="#bc5738", linestyle="--", label="Percentile interval bounds")
ax.axvline(high, color="#bc5738", linestyle="--")
ax.set(title="Bootstrap means of simulated waiting times", xlabel="Resampled mean (minutes)", ylabel="Resamples (count)")
ax.legend()
fig.tight_layout()
plt.show()
'''),
md("""
## Checks
Explain `axis=0`, `ddof=0`, `@`, and why the plotted values are means. Changing a seed can change the interval; it does not change the statistical question.
## Next Steps
Complete exercises 16–18 and 26–29. Replace the values with a new small array and verify calculations by hand. For repeated customers, discuss resampling customers rather than pretending each record is independent.
"""),
])

save("04_pandas_data_quality.ipynb", [
md("""
# 4. Audit and analyze retail orders
## Goal
Load a CSV, define valid data, reconcile row counts, validate a join, and summarize revenue.
Course Module 6. This is invented teaching data, not a real retailer.
## Setup
Requires the included `data/orders.csv`. Open the course folder or run from its `notebooks/` folder. See `data/README.md` for provenance and the data dictionary.
Reference: [pandas tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html).
## Steps
### 1. Load raw data without editing it
"""),
code('''
from pathlib import Path
import numpy as np
import pandas as pd

candidates = [Path("../data/orders.csv"), Path("data/orders.csv"), Path("orders.csv")]
source = next((path for path in candidates if path.exists()), None)
if source is None:
    raise FileNotFoundError("Put the course data/orders.csv beside the course notebooks folder.")
raw = pd.read_csv(source)
print("Raw shape:", raw.shape)
print(raw.head().to_string(index=False))
print("Missing cells by column:")
print(raw.isna().sum().to_string())
'''),
md("""
### 2. State policy, then clean
Grain: one order with one product. For this synthetic dataset, repeated order IDs are known exact duplicate records: remove exact duplicates first, then reject remaining duplicate IDs as ambiguous. Normalize region whitespace/case and label missing region Unknown. Reject invalid dates, nonfinite/nonpositive/noninteger units, and missing/nonfinite/negative prices. Zero price is allowed. A rejected row counts once even if it has multiple reasons.
"""),
code('''
unique = raw.drop_duplicates().copy()
duplicate_rows = len(raw) - len(unique)
if not unique["order_id"].is_unique:
    raise ValueError("Conflicting rows share an order ID; resolve before analyzing.")
unique["date"] = pd.to_datetime(unique["date"], format="%Y-%m-%d", errors="coerce")
unique["units"] = pd.to_numeric(unique["units"], errors="coerce")
unique["unit_price"] = pd.to_numeric(unique["unit_price"], errors="coerce")
unique["region"] = unique["region"].astype("string").str.strip().str.title().replace("", pd.NA).fillna("Unknown")
bad_date = unique["date"].isna()
bad_units = (~np.isfinite(unique["units"])) | (unique["units"] <= 0) | (unique["units"] % 1 != 0)
bad_price = (~np.isfinite(unique["unit_price"])) | (unique["unit_price"] < 0)
reasons = pd.DataFrame({"invalid_date": bad_date, "invalid_units": bad_units, "invalid_price": bad_price})
invalid = reasons.any(axis=1)
rejected = unique.loc[invalid].copy()
rejected["reason"] = reasons.loc[invalid].apply(lambda row: ", ".join(row.index[row]), axis=1)
clean = unique.loc[~invalid].copy()
clean["revenue"] = clean["units"] * clean["unit_price"]
print(rejected[["order_id", "reason"]].to_string(index=False))
'''),
md("### 3. Reconcile before calculating\nThese checks test row identity, exclusions, and valid values."),
code('''
audit = {"raw": len(raw), "exact_duplicates": duplicate_rows, "rejected": len(rejected), "clean": len(clean)}
print(audit)
assert audit == {"raw": 62, "exact_duplicates": 2, "rejected": 4, "clean": 56}
assert len(raw) == duplicate_rows + len(rejected) + len(clean)
assert clean["order_id"].is_unique
assert clean["revenue"].ge(0).all()
assert clean["date"].notna().all()
'''),
md("### 4. Validate a dimension join\nThe customer table must have one row per customer; otherwise the join can multiply revenue."),
code('''
customers = pd.DataFrame({"customer_id": [f"C{i:02d}" for i in range(12)], "tier": ["Standard", "Member"] * 6})
joined = clean.merge(customers, on="customer_id", how="left", validate="many_to_one", indicator=True)
assert len(joined) == len(clean)
assert joined["_merge"].eq("both").all()
assert np.isclose(joined["revenue"].sum(), clean["revenue"].sum())
print("All customer keys matched without multiplying rows.")
'''),
md("### 5. Summarize with counts and units\nUnknown is retained as an explicit region group; excluding it silently would change totals."),
code('''
summary = clean.groupby("region", as_index=False).agg(orders=("order_id", "size"), revenue_aed=("revenue", "sum"), average_order_aed=("revenue", "mean"))
print(summary.to_string(index=False))
overall_average = clean["revenue"].mean()
weighted_average = np.average(summary["average_order_aed"], weights=summary["orders"])
assert np.isclose(overall_average, weighted_average)
assert np.isclose(summary["revenue_aed"].sum(), clean["revenue"].sum())
print(f"Overall average order value: {overall_average:.2f} AED")
'''),
md("### 6. Save derived outputs separately\nThe raw CSV is preserved. These files are small and are recreated on rerun."),
code('''
output_dir = source.resolve().parent.parent / "outputs"
output_dir.mkdir(exist_ok=True)
clean.to_csv(output_dir / "orders_clean.csv", index=False)
rejected.to_csv(output_dir / "orders_rejected.csv", index=False)
summary.to_csv(output_dir / "region_summary.csv", index=False)
print("Saved clean, rejected, and summary CSV files in outputs/.")
'''),
md("""
## Checks
The reconciliation is 62 = 2 + 4 + 56. Explain why missing region can remain Unknown while missing price is rejected under this policy. These choices belong to this dataset's contract, not every business dataset.
## Next Steps
Complete exercises 19–22. Write three findings using actual outputs. Add a conflicting duplicate order to a copy of the source and make your pipeline stop; do not overwrite the original course data.
"""),
])

save("05_sql_and_charts.ipynb", [
md("""
# 5. Ask the same question with SQL and pandas
## Goal
Query an in-memory database, verify SQL/pandas agreement, and choose suitable charts.
Course Module 7. All input records are invented and created below; no dependency on previous notebooks.
## Setup
Uses sqlite3 from Python, pandas, and Matplotlib.
References: [SQLite API](https://docs.python.org/3/library/sqlite3.html), [Matplotlib](https://matplotlib.org/stable/users/explain/quick_start.html).
## Steps
### 1. Define one order per row
"""),
code('''
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

orders = pd.DataFrame({"order_id": range(1, 7), "date": ["2026-01-01", "2026-01-01", "2026-01-02", "2026-01-02", "2026-01-03", "2026-01-03"], "customer": ["A", "B", "A", "C", "B", "A"], "amount": [12., 8., 15., 10., 20., 5.]})
print(orders.to_string(index=False))
assert orders["order_id"].is_unique
'''),
md("### 2. Query and reconcile\nUse a bound parameter for a value. `:memory:` creates a temporary database; the connection is closed explicitly."),
code('''
connection = sqlite3.connect(":memory:")
try:
    orders.to_sql("orders", connection, index=False, if_exists="replace")
    query = """
    SELECT customer, SUM(amount) AS total
    FROM orders
    WHERE amount >= ?
    GROUP BY customer
    ORDER BY customer
    """
    sql_summary = pd.read_sql_query(query, connection, params=(0,))
finally:
    connection.close()
pandas_summary = orders.loc[orders["amount"] >= 0].groupby("customer", as_index=False)["amount"].sum().rename(columns={"amount": "total"})
pd.testing.assert_frame_equal(sql_summary, pandas_summary)
print(sql_summary.to_string(index=False))
'''),
md("### 3. Make three charts with distinct questions\nCategory totals, chronological change, and a distribution show different aspects of the same six observations."),
code('''
orders["date"] = pd.to_datetime(orders["date"])
daily = orders.groupby("date")["amount"].sum().sort_index()
fig, axes = plt.subplots(1, 3, figsize=(12, 3.6))
axes[0].bar(sql_summary["customer"], sql_summary["total"], color="#147d92")
axes[0].set(title="Who contributes revenue?", xlabel="Customer", ylabel="Revenue (AED)", ylim=(0, 36))
axes[1].plot(daily.index, daily.values, marker="o", color="#147d92")
axes[1].set(title="How do daily totals vary?", xlabel="Date in January 2026", ylabel="Revenue (AED)")
axes[1].set_xticks(daily.index, ["Jan 1", "Jan 2", "Jan 3"])
axes[2].hist(orders["amount"], bins=[0, 5, 10, 15, 20, 25], color="#147d92", edgecolor="white")
axes[2].set(title="How are order values distributed?", xlabel="Order value (AED)", ylabel="Orders (count)")
fig.suptitle("Synthetic six-order example — descriptive evidence only", fontsize=12)
fig.tight_layout()
plt.show()
'''),
md("""
## Checks
SQL and pandas should agree. Customer A totals 32 AED, B 28, and C 10. Daily totals are 20, 25, and 25 AED. Six invented orders cannot establish a durable trend or a causal explanation.
## Next Steps
Complete exercises 23–25. Rebuild these chart types using your cleaned retail data and explain one limitation of each. Add a null amount in a copy of the table and compare `COUNT(*)` with `COUNT(amount)`.
"""),
])

save("06_machine_learning_pipeline.ipynb", [
md("""
# 6. A complete regression workflow
## Goal
Compare a trivial baseline, a regularized linear model, and a tree ensemble using training-side cross-validation, then evaluate the selected model once on held-back data.
Course Modules 9–10. This uses generated independent observations and a deliberately simple regression relationship, with 5% missing feature entries. The target uses arbitrary units. Scores are teaching results, not forecasts of real-world model performance.
## Setup
Uses NumPy and scikit-learn; requires no downloads or credentials.
References: [scikit-learn pitfalls](https://scikit-learn.org/stable/common_pitfalls.html), [Inria course](https://inria.github.io/scikit-learn-mooc/).
## Steps
### 1. Generate data and reserve a test set
The split is random because the generated observations are independent. This choice would need reconsideration for time series or grouped records.
"""),
code('''
import numpy as np
import pandas as pd
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

X, y = make_regression(n_samples=700, n_features=5, n_informative=4, noise=20, random_state=42)
rng = np.random.default_rng(42)
X[rng.random(X.shape) < 0.05] = np.nan
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Train and test shapes:", X_train.shape, X_test.shape)
assert len(X_train) == 560 and len(X_test) == 140
'''),
md("### 2. Define candidates and the selection rule\nChoose lowest mean training-side CV MAE. Each fold learns its own imputer/scaler. The held-back test is not used here."),
code('''
candidates = {
    "dummy median": make_pipeline(SimpleImputer(strategy="median"), DummyRegressor(strategy="median")),
    "ridge": make_pipeline(SimpleImputer(strategy="median"), StandardScaler(), Ridge(alpha=1.0)),
    "random forest": make_pipeline(SimpleImputer(strategy="median"), RandomForestRegressor(n_estimators=100, min_samples_leaf=3, random_state=42, n_jobs=1)),
}
cv = KFold(n_splits=5, shuffle=True, random_state=42)
rows = []
for name, model in candidates.items():
    errors = -cross_val_score(model, X_train, y_train, cv=cv, scoring="neg_mean_absolute_error", n_jobs=1)
    rows.append({"model": name, "cv_mae": errors.mean(), "fold_sd": errors.std(ddof=1)})
comparison = pd.DataFrame(rows).sort_values("cv_mae").reset_index(drop=True)
print(comparison.to_string(index=False))
selected_name = comparison.iloc[0]["model"]
print("Selected using training data only:", selected_name)
'''),
md("### 3. Freeze the decision and evaluate\nBoth the selected model and reference baseline are fitted on all training data. Fold SD above is descriptive variability, not a confidence interval."),
code('''
selected_model = candidates[selected_name]
selected_model.fit(X_train, y_train)
predictions = selected_model.predict(X_test)
dummy = make_pipeline(SimpleImputer(strategy="median"), DummyRegressor(strategy="median"))
dummy.fit(X_train, y_train)
test_mae = mean_absolute_error(y_test, predictions)
baseline_mae = mean_absolute_error(y_test, dummy.predict(X_test))
print(f"Final test MAE: {test_mae:.2f} target units")
print(f"Baseline test MAE: {baseline_mae:.2f} target units")
print(f"Relative MAE reduction: {(baseline_mae-test_mae)/baseline_mae:.1%}")
assert predictions.shape == y_test.shape
assert np.isfinite(predictions).all()
assert test_mae >= 0 and baseline_mae >= 0
'''),
md("### 4. Inspect errors after final assessment\nUse these examples to understand limitations. If they inspire model changes, you need fresh evaluation evidence for the revised model."),
code('''
errors = pd.DataFrame({"actual": y_test, "predicted": predictions})
errors["absolute_error"] = (errors["actual"] - errors["predicted"]).abs()
print(errors.nlargest(5, "absolute_error").round(2).to_string(index=False))
'''),
md("""
## Checks
Explain why imputation lives inside the pipeline. Explain why a linear model can do well on this generated relationship and why this does not rank model families universally. Report the actual outputs, including a failure to improve if one occurs; do not make passing conditional on beating a baseline on every dataset.
## Next Steps
Exercises 30–35. For a new experiment, work only with training-side validation and record choices before execution. The existing test has now been revealed: do not claim it remains a pristine test for an adaptively redesigned model. Your independent capstone needs its own declared split.
"""),
])

save("07_neural_network_foundations.ipynb", [
md("""
# 7. See how a model learns
## Goal
Implement gradient descent for a line and compare a linear classifier with a small neural network on synthetic curved classes.
Course Module 11. This is a foundation exercise; it does not train a large deep-learning model.
## Setup
Uses NumPy, scikit-learn, and Matplotlib. No GPU or network access required.
References: [Google MLCC](https://developers.google.com/machine-learning/crash-course), [PyTorch basics for the next step](https://docs.pytorch.org/tutorials/beginner/basics/intro.html).
## Steps
### 1. Fit a line using visible arithmetic
These 100 noiseless pairs are a numerical optimization demonstration. They are not a train/test performance claim.
"""),
code('''
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-1, 1, 100)
y = 3*x + 2
w, b = 0.0, 0.0
learning_rate = 0.1
losses = []
for step in range(150):
    error = w*x + b - y
    losses.append(np.mean(error**2))
    gradient_w = 2*np.mean(error*x)
    gradient_b = 2*np.mean(error)
    w -= learning_rate * gradient_w
    b -= learning_rate * gradient_b
print(f"Learned weight={w:.4f}, bias={b:.4f}")
print(f"Loss: {losses[0]:.4f} → {losses[-1]:.8f}")
assert losses[-1] < losses[0]
assert np.isclose(w, 3, atol=0.001) and np.isclose(b, 2, atol=0.001)
'''),
md("### 2. Plot the optimization trace\nLoss is squared error in this numeric demonstration."),
code('''
fig, ax = plt.subplots(figsize=(6, 3.2))
ax.plot(losses, color="#147d92")
ax.set(title="Gradient descent fits a synthetic line", xlabel="Update step", ylabel="Mean squared error")
fig.tight_layout()
plt.show()
'''),
md("""
### 3. Define two fixed classification candidates
Two interlocking curved groups are generated using `make_moons`. Compare candidates on validation data before revealing the test. Class 1 is the positive class; balanced classes and equal example costs make accuracy a useful first metric here.
"""),
code('''
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

features, labels = make_moons(n_samples=600, noise=0.20, random_state=42)
X_develop, X_test, y_develop, y_test = train_test_split(features, labels, test_size=0.2, stratify=labels, random_state=42)
X_train, X_valid, y_train, y_valid = train_test_split(X_develop, y_develop, test_size=0.25, stratify=y_develop, random_state=42)
models = {
    "linear": make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),
    "neural": make_pipeline(StandardScaler(), MLPClassifier(hidden_layer_sizes=(12,), activation="tanh", solver="lbfgs", alpha=0.1, max_iter=2000, random_state=42)),
}
validation_scores = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    validation_scores[name] = accuracy_score(y_valid, model.predict(X_valid))
    print(name, "validation accuracy:", round(validation_scores[name], 3))
winner = max(validation_scores, key=validation_scores.get)
print("Chosen before test evaluation:", winner)
'''),
md("### 4. Refit the chosen architecture and test once\nThe library trains the network; Step 1 showed the update principle. This neural model uses a different numerical optimizer (`lbfgs`), so its internal updates are not identical to our simple loop."),
code('''
model = models[winner]
model.fit(X_develop, y_develop)
test_predictions = model.predict(X_test)
print("Final test accuracy:", round(accuracy_score(y_test, test_predictions), 3))
print("Confusion matrix: rows = actual 0/1; columns = predicted 0/1")
print(confusion_matrix(y_test, test_predictions, labels=[0, 1]))
assert len(test_predictions) == len(y_test)
assert set(np.unique(test_predictions)) <= {0, 1}
'''),
md("""
## Checks
Explain a weight, bias, activation, loss, gradient, learning rate, and inference. Explain why a hidden nonlinearity can help these generated curved groups. Results are bounded to this teaching dataset and split.
## Next Steps
Exercises 36–37. For a real framework extension follow the official PyTorch tutorial after understanding the calculations here. Changing this example based on the revealed test makes that test part of development history.
"""),
])

save("08_text_retrieval_and_ai_evaluation.ipynb", [
md("""
# 8. Build and evaluate a tiny search system
## Goal
Represent text numerically, retrieve source passages, and separate evidence retrieval from answer generation.
Course Module 12. The six documents and evaluation queries below are invented. There is no LLM, API request, or generated answer in this notebook.
## Setup
Uses scikit-learn and NumPy. The collection is a fixed search corpus; fitting its TF-IDF vocabulary is indexing available documents, not fitting on held-back question labels.
Reference: [Hugging Face course](https://huggingface.co/learn/llm-course/chapter1/1) for the subsequent language-model concepts.
## Steps
### 1. Index the documents
"""),
code('''
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = {
    "refunds": "Refunds are returned to the original payment method within seven business days.",
    "delivery": "Standard delivery takes three days. Express delivery arrives the next day.",
    "hours": "Customer support hours are Monday to Friday from nine to five.",
    "password": "Reset your password using the account settings page and your email address.",
    "cancellation": "Cancel an order before dispatch by contacting customer support.",
    "privacy": "Export or delete your account data from the privacy settings page.",
}
ids = list(documents)
vectorizer = TfidfVectorizer(stop_words="english")
document_vectors = vectorizer.fit_transform(documents.values())
print("Document-term matrix shape:", document_vectors.shape)
'''),
md("### 2. Return evidence with a bounded fallback\nA zero-overlap fallback is simple and incomplete: nonzero similarity does not prove that a question is answerable."),
code('''
def retrieve(question, k=2):
    if not isinstance(question, str) or not question.strip():
        return []
    query_vector = vectorizer.transform([question])
    scores = cosine_similarity(query_vector, document_vectors).ravel()
    ranked = np.argsort(-scores)
    return [{"id": ids[i], "score": float(scores[i]), "text": documents[ids[i]]}
            for i in ranked[:k] if scores[i] > 0]

for hit in retrieve("How long do refunds take?"):
    print(hit)
assert retrieve("How long do refunds take?")[0]["id"] == "refunds"
assert retrieve("") == []
'''),
md("""
### 3. Evaluate a fixed small question set
For each answerable query, one relevant document is labeled. Hit@k asks whether it appears among the top k. With one relevant document per query here, this is also recall@k. The tiny hand-authored set is a smoke test, not a reliable estimate of production quality.
"""),
code('''
evaluation = [
    ("When will refunds arrive?", "refunds"),
    ("How fast is express delivery?", "delivery"),
    ("What are customer support hours?", "hours"),
    ("How do I reset my password?", "password"),
    ("Can I cancel before dispatch?", "cancellation"),
    ("How can I delete my account data?", "privacy"),
]
top1, top2 = [], []
for question, relevant_id in evaluation:
    found = [hit["id"] for hit in retrieve(question)]
    top1.append(relevant_id in found[:1])
    top2.append(relevant_id in found[:2])
    print(question, "→", found, "expected:", relevant_id)
print(f"Hit@1: {np.mean(top1):.1%}; Hit@2: {np.mean(top2):.1%}")
assert all(isinstance(value, bool) for value in top1)
'''),
md("### 4. Find a failure that a good-looking score hides\nBoth questions below are outside the corpus. Shared vocabulary can still retrieve a passage."),
code('''
unknown_questions = ["What is the capital of Peru?", "Do refunds include a cryptocurrency bonus?"]
for question in unknown_questions:
    hits = retrieve(question)
    print(question, "→", [hit["id"] for hit in hits] or "No matching terms")
print("A retrieved refund policy does not answer whether cryptocurrency bonuses exist.")
print("Singular/plural mismatch:", retrieve("How long does a refund take?"))
print("Without stemming, refund and refunds are different vocabulary terms; relevant evidence can be missed.")
'''),
md("""
## Checks
Explain why the system has not answered the question merely by retrieving a passage. Explain the difference between lexical TF-IDF and a learned embedding, and between indexing documents and training a generator. The deliberately irrelevant 'refunds' question exposes the weakness of the fallback even if the answerable-query score is high.
## Next Steps
Complete exercise 38. Write five new questions before changing the retriever. Add ambiguous and unsupported cases. The 40-hour bridge then requires a real pretrained model and a document assistant with separately measured retrieval, correctness, evidence support, latency, and optional provider cost.
"""),
])

print(f"Built {len(list(NOTEBOOKS.glob('*.ipynb')))} notebooks and {len(rows)} synthetic CSV rows.")
