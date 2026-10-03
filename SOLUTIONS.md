# Answer guide

Use this after attempting `PRACTICE.html`. A different correct approach is welcome. After reading an answer, close this guide and solve a changed version later. For open-ended work, the answer is a set of defensible criteria, not a single magic output.

## Python basics

**1. Receipt:** `3 * 12.5 * (1 - 0.10) + 5` is **38.75 AED**. Discount the merchandise before adding delivery under the stated rule. `print(f"{total:.2f}")` formats two decimals.

**2. Minutes:** `135 // 60` is 2 and `135 % 60` is 15. For 59: 0 hours, 59 minutes. For 60: 1 hour, 0 minutes.

**3. Conversion:** `int(quantity) * float(price)` gives **30.0**. Before conversion, `quantity * 2` gives `"44"` because multiplying a string by an integer repeats it.

**4. Name:** `"  sOMRIt  ".strip().title()` gives `"Somrit"`. The empty string remains empty. Name capitalization in real data is culturally complex; this is a string-method exercise, not a universal identity-cleaning rule.

**5. Outputs:** 14, 20, 3, 1, and `"A"`. Multiplication precedes addition; parentheses change grouping; floor division and remainder split whole groups from the remainder; indexing starts at zero.

**6. Delivery:**

```python
def delivery_fee(spend):
    if spend < 0:
        raise ValueError("spend must be nonnegative")
    if spend >= 100:
        return 0
    if spend >= 50:
        return 5
    return 10
```

Expected fees for 49, 50, 99, 100: **10, 5, 5, 0**. For external numeric input also validate type and finiteness; `NaN` does not behave like an ordinary ordered number.

**7. Positive sum:**

```python
total = 0
for value in [12, -3, 0, 8, 5]:
    if value > 0:
        total += value
assert total == 25
```

An empty list leaves zero. After understanding the loop, `sum(x for x in values if x > 0)` is a concise alternative.

**8. Grouping:**

```python
totals = {}
for customer, amount in [("A", 12), ("B", 8), ("A", 15)]:
    totals[customer] = totals.get(customer, 0) + amount
assert totals == {"A": 27, "B": 8}
```

**9. Unique customers:** `unique = set(customers)`; `len(unique)` is **3** and `sorted(unique)` is `["A", "B", "C"]`. A set itself does not promise your desired presentation order.

**10. Aliasing:** both `a` and `b` become `[1, 2, 3]`, because they name the same list. `b = a.copy()` creates a new outer list. If `a` contains lists, their inner objects still have shared references after a shallow copy.

## Functions, files, and tests

**11. Average:**

```python
def average(values):
    if not values:
        raise ValueError("average requires at least one value")
    return sum(values) / len(values)
```

`average([5]) == 5` and `average([2, 4, 6]) == 4`. This contract assumes a numeric list/sequence. Do not silently use zero for the mean of an empty sample.

**12. Discount:** see Notebook 2 for the complete function and tests, including nonfinite inputs. Check both rate boundaries, an empty basket, a negative price, an invalid rate, and a normal calculation. Use approximate equality for nonexact floating-point expectations.

**13. Print versus return:**

```python
def wrong(values):
    print(sum(values))

def correct(values):
    return sum(values)

result = correct([2, 3])  # 5; wrong([2, 3]) displays 5 but returns None
```

**14. Input parser:**

```python
def parse_nonnegative_integer(text):
    try:
        value = int(text)
    except (TypeError, ValueError) as error:
        raise ValueError("Enter a whole number as text") from error
    if value < 0:
        raise ValueError("Enter zero or a positive whole number")
    return value
```

For the stated **text input** contract, `"4"` and `" 4 "` give 4; `"4.5"`, `"hello"`, and `"-1"` are rejected. If your API also accepts arbitrary numeric objects, validate types explicitly: `int(4.5)` would truncate and booleans have integer-like behavior. A parser's contract must match its callers.

**15. CSV project:** there are several valid designs. Require headers; strip categories; convert amounts; reject nonfinite/negative values; retain valid zero; record row numbers and reasons. Reject blank categories under a declared policy. The total of category sums should equal the sum of accepted amounts. Use `math.isfinite` in addition to numeric conversion because text such as `"nan"` can parse as a float.

Suggested architecture:

```text
read_csv(path) → raw records with row numbers
validate_record(record) → clean record OR reason
summarize(clean_records) → totals and counts
write_outputs(summary, rejected) → JSON + CSV
```

Accept an empty CSV **with the required headers** as zero records and an empty summary. Reject missing headers clearly. A row `Food,0` is valid; `Food,-1` is rejected; `Food,abc` is rejected; `Food,12` plus `Food,15` totals 27. The raw file must remain byte-for-byte unchanged. The supplied Notebook 2 teaches the file mechanics; completing this fuller validation project yourself is part of the course.

## NumPy and data quality

**16. Arrays:** `np.array([2, 1, 3]) * np.array([10, 25, 8])` gives **[20, 25, 24]**, totaling **69**. Python's `[2, 1, 3] * 2` repeats a list; multiplying one Python list by another is not defined.

**17. Shapes:** `(4, 3) @ (3,)` gives `(4,)`. Reducing `(4, 3)` along axis 0 gives `(3,)`. A `(4,)` weight vector has the wrong contracted dimension for this matrix product and raises an error.

**18. Standardization:** column means are `[2, 20]`, population standard deviations approximately `[0.81649658, 8.16496581]`, and standardized rows approximately `[-1.22474487, -1.22474487]`, `[0, 0]`, `[1.22474487, 1.22474487]`. Replace a zero scale with 1 under a stated policy, which produces zero for a constant column after mean subtraction. Fitting scales on test data lets held-back information influence the model pipeline.

**19–20. Audit:** the data dictionary and Notebook 4 define the policy. **62 raw = 2 exact duplicates + 4 rejected unique rows + 56 accepted orders.** One missing region remains `Unknown`. The four rejected unique records have invalid quantity (two records), missing price (one), and invalid date (one). Count rows with any failure, rather than adding overlapping reason counts. If a newly modified file has conflicting repeated IDs, stop and resolve their meaning instead of arbitrarily keeping the first.

**21. Aggregation:** use `revenue = units * unit_price`, then aggregate valid unique orders by region. Verified totals: **East 1,000 AED / 20 orders; North 1,000 AED / 20 orders; South 775 AED / 15 orders; Unknown 20 AED / 1 order**. Total revenue is **2,795 AED** and average order value is `2795/56`, approximately **49.91 AED**. A weighted mean of region averages using their order counts equals this; an unweighted mean gives each region equal influence regardless of how many orders it contains. The executed Notebook 4 and `outputs/region_summary.csv` contain the same values.

**22. Join trap:**

```python
orders = pd.DataFrame({"customer": ["A"], "amount": [10]})
customers = pd.DataFrame({"customer": ["A", "A"], "tier": ["Gold", "Silver"]})
# Two matches produce two output rows and would double the apparent amount.
orders.merge(customers, on="customer", validate="many_to_one")
# Raises pandas.errors.MergeError: the right key is not unique.
```

Correct the dimension's meaning upstream. Blindly removing one tier may conceal a time-dependent relationship or data error.

## SQL and statistics

**23. SQL:** `SELECT customer, SUM(amount) AS total FROM orders GROUP BY customer ORDER BY customer;` gives A=27, B=8 for exercise 8's data. In pandas: `df.groupby("customer", as_index=False)["amount"].sum()`. Match column names, order, and numeric types before comparing. Notebook 5 demonstrates parity on a separate six-order table.

**24. NULL:** `COUNT(*)` includes every row; `COUNT(amount)` excludes rows where amount is NULL. Filter with `WHERE amount IS NULL`. Zero is a known numeric value and is counted by both.

**25. Charts:** acceptable work includes a region bar chart with revenue in AED, a sorted daily line chart with dates, and a histogram of order values with labeled bin/count meaning. Check totals against tables. State that the data are synthetic, missing/invalid records were handled under a policy, and the brief period does not establish long-term patterns.

**26. Mean/median:** **32.5 / 10**. The median is the middle-order summary here. Mean × count equals the total of 130.

**27. Rates:** A=**20%**, B=**30%**, difference=**10 percentage points**, relative increase from A=**50%**, pooled rate=`32/140`=**22.857%**. The pooled rate is not the unweighted mean of 20% and 30% because denominators differ.

**28. Resampling:** rows from the same customer can share behavior. Resampling individual rows may exaggerate the amount of independent information. Resample customers with their observations if customers are the independent sampling unit and that design matches the question. Time dependence or unequal cluster structure can require more careful methods.

**29. Causality:** seasonality, changes in the customer mix, and a simultaneous price/promotion change are plausible alternatives. Consider random assignment of eligible customers to campaign/control, with a predeclared metric, randomization unit, window, and analysis. Assignment spillovers and noncompliance need attention. Observation after an event alone does not identify its effect.

## ML and AI

**30. Leakage:** eventual refund date is unavailable at checkout and encodes future outcome information. Customer fields must use values available then, not a retrospectively updated account state. Scaling before splitting uses information from held-back examples; put learned preprocessing inside training-only fitting/CV pipelines.

**31. Metrics:** define “positive” as the event of interest. Accuracy=`(8+86)/100`=**94%**; precision=`8/10`=**80%**; recall=`8/12`≈**66.67%**; F1=`2*8/(2*8+2+4)`≈**72.73%**. This classifier misses four of twelve actual positives. Whether that is acceptable depends on consequences, not accuracy alone.

**32. Splits:** (a) train on earlier periods and validate/test on later periods, with a gap when timing/feature windows require it; (b) group by patient so the new-patient test contains different people; (c) random split is sensible for truly independent generated observations. If the intended use is future measurements of existing patients, the design may instead need a time-aware within-patient strategy. State the deployment question first.

**33. Comparison:** a valid answer contains a predeclared hypothesis, same training-side folds, a fixed metric, fold results, and a selection rule. It does not use final test scores to choose settings. No specific model must win; valid methodology is the answer.

**34. Error slice:** show slice definition, size, overall comparison, observed error, and an explicitly tentative explanation. Very small groups support weak conclusions. If final-test errors inspire a change, assess the revision with new appropriate evidence rather than repeatedly optimizing against that test.

**35. Preprocessing:** numeric branch = median imputation, optionally scaling; categorical branch = an explicit missing-category policy and one-hot encoding with an unseen-category policy such as `handle_unknown="ignore"`. Combine via `ColumnTransformer` inside a `Pipeline` with the estimator. Training learns medians, means/scales, category vocabulary, and model parameters; validation/test only receive the learned transformations. Do not assume zero vectors for new categories are always harmless.

**36. Gradient:** next weight=`2 - 0.1*3`=**1.7**. A negative gradient would increase the weight under this update. The gradient describes local change; a large step can overshoot.

**37. Learning rate:** your evidence should show loss against update count with the same data and initialization. Smaller steps may need more updates; large steps can oscillate/diverge. A particular setting's failure is an observed property of that problem, not a universal rule. Keep parameter choice separate from final test evaluation.

**38. Retrieval:** preserve passage IDs; label relevant evidence before tuning; compute a top-k hit measure over answerable questions; assess missing-answer cases separately. TF-IDF uses term statistics, not a pretrained generative language model. A high score on a small hand-written set is a smoke test, and shared terms can still retrieve irrelevant evidence. A generator needs its own correctness/support assessment.

**39. Handoff:** passing means the documented steps work without your private remembered state. Include versions, inputs, run order, output paths, and common failures. Restarting a notebook and running all cells is necessary, but an actual clean-environment or external-reviewer run is stronger evidence.

**40. Independence:** use the capstone rubric. Expect defensible grain, real checks, a reproducible summary, labeled chart, and either a legitimate prediction plan or a clear explanation that the dataset cannot support one. Do not invent targets, provenance, or numerical claims. Needing syntax documentation is normal; needing someone else to design every step means more practice is needed.

## Answering without memorizing

For every exercise you missed, invent one variant that would break a superficial solution. Examples: empty lists, zero denominators, duplicated lookup keys, future-dated features, or an unanswered question sharing keywords with a passage. Explain the failure before repairing it.
