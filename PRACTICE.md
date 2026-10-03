# Practice workbook — 40 exercises

Work in a new notebook or `.py` file. Read the relevant module first. For each exercise write expected outputs before running code, test an edge case, and explain the solution aloud. Solutions are in `SOLUTIONS.html`; open them only after a serious attempt. Documentation is allowed. Generated solutions are not allowed for checkpoints.

Suggested standard: an exercise passes when the code works on the example and a different input, and you can explain its behavior. A correct answer copied from the guide does not pass until you can solve a new variant the following day.

## Python basics — Modules 1–2

1. **Receipt.** Three items cost 12.50 each. Apply a 10% discount, then add a 5 AED delivery fee. Display the result to two decimals. Change the quantity and recompute.
2. **Minutes.** Convert 135 minutes into whole hours and remaining minutes. What changes for 59 and 60?
3. **Text conversion.** Given `quantity = "4"` and `price = "7.5"`, calculate a numeric total. Explain the effect of `quantity * 2` before converting it.
4. **Clean a name.** Transform `"  sOMRIt  "` into `"Somrit"`. What happens for an empty string?
5. **Predict first.** Predict `2 + 3 * 4`, `(2 + 3) * 4`, `7 // 2`, `7 % 2`, and `"AI"[0]`. Explain each.
6. **Delivery rule.** Charge 10 below 50, 5 from 50 up to 99.99, and 0 from 100 onward. Test 49, 50, 99, and 100. Reject negative spend.
7. **Filter and sum.** Sum only positive values from `[12, -3, 0, 8, 5]`, using a loop first. Try an empty list.
8. **Group orders.** For `[("A", 12), ("B", 8), ("A", 15)]`, return total spend by customer without pandas.
9. **Unique customers.** Given `["A", "B", "A", "C", "B"]`, count unique customers. Produce an alphabetically sorted list of them.
10. **Aliasing bug.** Predict what happens after `a = [1, 2]; b = a; b.append(3)`. Then create an independent shallow copy and explain its limit with nested lists.

## Reusable Python — Modules 3–4

11. **Safe average.** Write `average(values)` returning the arithmetic mean. For empty input raise `ValueError`. Test one value and several values.
12. **Discount function.** Implement `discounted_total(prices, rate)` with rate constrained to 0–1 and nonnegative prices. Test valid, empty, and invalid cases.
13. **Return bug.** A function computes a sum and prints it, but assigning its result gives `None`. Write and repair a minimal example.
14. **Input parser.** Write a function that converts text to a nonnegative integer. Reject negative, fractional, and nonnumeric input. Catch only expected conversion exceptions.
15. **CSV mini-project.** Read a CSV with `category,amount`; total by category; reject malformed/negative amounts with a recorded reason; write a JSON summary and a rejected-row CSV. Preserve the raw file. Add tests for empty input, missing headers, malformed amount, valid zero, and two rows in one category.

## Arrays and data — Modules 5–7

16. **Arrays.** Multiply quantities `[2, 1, 3]` by prices `[10, 25, 8]`. Explain why Python-list multiplication is different from NumPy elementwise multiplication.
17. **Shapes.** For `X.shape == (4, 3)` and `w.shape == (3,)`, predict `(X @ w).shape` and `X.mean(axis=0).shape`. What goes wrong if `w.shape == (4,)`?
18. **Standardize.** Standardize columns `[[1, 10], [2, 20], [3, 30]]` using their population means and standard deviations. Explain how you would handle a constant column and why test-set scaling must use training statistics.
19. **Quality audit.** Inspect `data/orders.csv`. Identify grain, duplicates, missing/invalid quantities and prices, invalid dates, and inconsistent regions. Write the policy before deleting anything.
20. **Clean and reconcile.** Apply Notebook 4's stated cleaning policy. Show raw = duplicate + rejected + clean rows, with categories counted without overlap. Do not count one rejected row twice in that reconciliation.
21. **Aggregation.** Compute revenue by region and average order value from the valid unique orders. Include counts and units. Explain why averaging region averages without weights is wrong.
22. **Join trap.** Create an orders table with customer A once and a customer table with A twice. Merge them. Explain the row inflation and make the merge reject the unexpected cardinality.
23. **SQL parity.** Write a SQL total by customer for the three orders in exercise 8. Reproduce it in pandas and compare the result.
24. **NULL.** Explain the difference between `COUNT(*)` and `COUNT(amount)` when an amount is null. Write the SQL filter for missing amounts.
25. **Charts.** Build a category bar chart, a chronological daily-revenue line chart, and an order-value histogram from the clean data. Give each a question, units, and a bounded finding.

## Statistics and ML — Modules 8–10

26. **Mean and median.** Calculate both for `[10, 10, 10, 100]`. Which better describes the middle order? Which reconciles total spending?
27. **Rate comparison.** A has 20 conversions out of 100 visitors; B has 12 out of 40. Calculate both rates, percentage-point difference, relative increase from A, and the pooled conversion rate.
28. **Uncertainty.** Explain why a bootstrap over individual rows may be misleading when each customer has 20 correlated observations. Suggest a more suitable resampling unit.
29. **Causality.** Sales increased after a campaign. Give three alternative explanations and describe a better study design.
30. **Leakage review.** You predict whether an order will be refunded at checkout. Candidate fields: order value, checkout time, eventual refund date, customer information available then. Identify illegitimate information. Explain why scaling before splitting is also a problem.
31. **Metric arithmetic.** A classifier produces TP=8, FP=2, FN=4, TN=86. Compute accuracy, precision, recall, and F1. State the positive class before interpreting the metrics.
32. **Split design.** Pick splits for (a) next-month demand, (b) new-patient classification with repeated measurements, (c) independent generated observations. Explain the intended future use in each.
33. **Model comparison.** In Notebook 6, use only training data and the same CV folds to compare a new regularization setting. Record your hypothesis before running. Do not use the final test score to choose the setting.
34. **Error slice.** Choose a meaningful training-validation slice. Report its size, error, and one plausible explanation. Explain why a tiny slice is uncertain and why a plausible explanation is not proof.
35. **Preprocessing.** Describe a pipeline for numeric and categorical inputs with missing values and previously unseen categories. Identify which quantities are learned from training data.

## AI and independence — Modules 11–14

36. **Gradient step.** Given `w=2`, `dL/dw=3`, and learning rate `0.1`, calculate the next weight. Explain the direction. What changes if the gradient is negative?
37. **Training loop.** Change Notebook 7's learning rate using training-side evidence. Show one slower setting and, if possible, one unstable setting. Compare losses without changing the test set or choosing settings from it.
38. **Retrieval.** Add three documents and five questions to Notebook 8. Mark which questions are answerable. Evaluate ranked evidence and behavior on missing-answer cases. Explain why TF-IDF search is not an LLM.
39. **Handoff.** Give your project folder to a reviewer, or simulate a fresh environment. They must follow only the README. Record every missing assumption and fix the instructions.
40. **Final independence challenge.** In 90 minutes with documentation but no generated solutions: inspect an unfamiliar CSV; state grain and three risks; write a tested summary function; produce a justified chart; propose a valid prediction target/split/baseline if the data permit. Explain what cannot be inferred. Use the capstone rubric for the larger final project.

## Weekly reflection

Record: what you can now do without hints, the most instructive error, a concept you can explain with an Excel analogy, a weak area to revisit, and next week's concrete output. Count completed independent tasks, not videos watched.
