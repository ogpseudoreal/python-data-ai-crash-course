# Synthetic retail data

`orders.csv` was generated specifically for this course by `build_notebooks.py`. It contains **62 raw rows**: 60 intended unique orders plus 2 exact copies. Four unique rows have invalid fields deliberately planted for data-quality practice. This is invented data and represents no real people, retailer, or commercial result.

Grain: one order, containing one product, denominated in AED. This simplified grain avoids mixed order-line/order-level totals. The represented dates are in January 2026; dates are local business dates, not timestamps.

| Column | Meaning | Intended valid values |
|---|---|---|
| `order_id` | Unique order identifier | Nonempty `O`-prefixed ID |
| `date` | Order's business date | ISO YYYY-MM-DD |
| `customer_id` | Invented customer ID | One of C00–C11 |
| `region` | Invented order region | North, South, East; unknown can be retained |
| `units` | Quantity in the order | Positive whole number |
| `unit_price` | Price per unit in AED | Finite nonnegative number |

Planted defects: one negative quantity; one textual quantity; one missing price; one invalid date; one missing region; four region labels with extra spaces and inconsistent casing; two exact duplicate records. Missing region is retained as Unknown under the stated course policy. Missing/invalid dates, quantities, or prices are rejected. There are no overlapping rejection reasons in the supplied original file, but Notebook 4 handles overlap without double-counting rejected rows.

Expected row reconciliation: **62 raw = 2 exact duplicates + 4 rejected unique rows + 56 clean orders**. This is a policy-specific answer key, not a universal rule for cleaning retail data. Do not change raw input in place. Use copies for deliberate corruption exercises.

The course's other notebooks generate their own invented data independently. The regression and two-class examples use scikit-learn's data generators with fixed seeds. Those synthetic patterns are chosen for teaching and should not be interpreted as representative of a business population.
