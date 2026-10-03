# Python, data, ML, and AI glossary

Use this as a lookup tool, not a memorization assignment. Learn a term when you first use it, then explain it with your own example. The definitions below are original concise teaching definitions; for exact API behavior, use the library documentation linked in `SOURCES.md`.

## Tools and programming

| Term | Plain English meaning |
|---|---|
| Algorithm | A defined sequence of steps for solving a problem. |
| API | An agreed interface through which one piece of software uses another. |
| Argument | A value supplied when calling a function. |
| Assertion | A development-time check that a condition holds; failure raises an error. |
| Attribute | A named value belonging to an object, such as `array.shape`. |
| Boolean | A logical value: `True` or `False`. |
| Breakpoint | A place where a debugger pauses execution so you can inspect state. |
| Class | A definition used to create objects with particular data and behavior. |
| CLI | Command-line interface: interacting through typed terminal commands. |
| Code | Instructions written in a programming language. |
| Comment | Explanatory text in source code that is not executed, usually after `#`. |
| Comprehension | Compact syntax for constructing a collection from an iterable. |
| Conditional | A branch that runs according to whether a condition is true. |
| Context manager | An object used with `with` to manage setup and cleanup, such as closing a file. |
| Debugging | Finding the cause of incorrect behavior and correcting it. |
| Dependency | Another library or tool your program requires. |
| Dictionary | A mapping from unique keys to values, such as `{"city": "Dubai"}`. |
| Docstring | Text at the start of a function/module/class explaining its use. |
| Environment variable | A value supplied by the surrounding operating environment, often used for configuration. |
| Exception | A runtime signal that an operation could not proceed normally. |
| Expression | Code that evaluates to a value, such as `price * quantity`. |
| Float | A number stored using floating-point representation; often approximate. |
| Function | A named reusable operation that may accept inputs and return a result. |
| Git | A system for recording and comparing versions of files. |
| IDE | Integrated development environment: tools for editing, running, and debugging code. |
| Immutable | Unable to be changed in place after creation, as with a string. |
| Import | Make another module's functionality available in your code. |
| Index | A position or label used to access an item; the meaning depends on the object. |
| Integer | A whole number, represented by Python's `int`. |
| Interpreter | The program that executes Python code. |
| Iterable | Something whose elements can be visited, such as a list or range. |
| JSON | A text format for exchanging nested data such as objects and arrays. |
| Kernel | The process executing notebook cells and storing their current state. |
| Library | Reusable code implementing related capabilities. |
| List | An ordered, mutable sequence of items. |
| Loop | Code that repeats over items or while a condition holds. |
| Method | A function accessed through an object or class. |
| Module | An importable unit of Python code, often a `.py` file. |
| Mutable | Able to change in place, as with lists and dictionaries. |
| None | Python's explicit value for absence; distinct from zero or an empty string. |
| Notebook | A document containing text, code cells, and their outputs. |
| Object | A runtime entity with a type, identity, and value/behavior. |
| Package | A collection of reusable modules; also commonly used for installable distributions. |
| Parameter | A named input in a function definition; in ML it can instead mean a learned model quantity. |
| Path | A location of a file or directory. |
| pip | A Python package installation tool. |
| REPL | Read-evaluate-print loop: an interactive interpreter, often displaying `>>>`. |
| Repository | A project and its tracked version history. |
| Return value | The result sent back to the caller by a function. |
| Scope | The region in which a name can be resolved. |
| Script | A program saved as a file and run to perform a task. |
| Set | A collection of distinct hashable elements. |
| Slice | Selection of a sequence interval, such as `items[1:4]`. |
| String | A sequence of text characters. |
| Syntax | The grammar governing valid code. |
| Terminal / shell | The terminal presents a text interface; a shell interprets operating-system commands. |
| Traceback | The call history shown when an exception propagates. |
| Tuple | An immutable sequence, often used for a fixed group of related values. |
| Type | The kind of value and the operations it supports. |
| Unit test | A repeatable check of a small unit of behavior against an expected result. |
| Variable | A name associated with a value/object. |
| Virtual environment | A project-specific Python environment with its own installed packages. |
| Working directory | The current folder used to resolve relative file paths. |

## Data and analytics

| Term | Plain English meaning |
|---|---|
| Aggregation | Combining multiple observations into a summary, such as sum or mean. |
| Array | An indexed collection of values; NumPy arrays support efficient numeric operations. |
| Axis | A dimension along which an array operation acts. |
| Broadcasting | Rules allowing compatible different array shapes to participate in arithmetic. |
| Cardinality | Number of distinct values or the relationship of matches between tables, depending on context. |
| Categorical variable | A value representing a category, such as region or product type. |
| CSV | Comma-separated values: a common plain-text table format. |
| Data dictionary | Definitions of columns, types, units, valid values, and meanings. |
| DataFrame | A labeled table, commonly from pandas, with potentially mixed column types. |
| Data quality | How well data satisfy the requirements of the intended use. |
| Denominator | The reference total beneath a fraction or rate. |
| Dimension table | A table of descriptive information joined to event/fact records. |
| Duplicate | A repeated record under a stated definition of identity. |
| EDA | Exploratory data analysis: inspecting distributions, relationships, and quality. |
| ETL | Extract, transform, load: obtain data, reshape/clean it, and put it into a destination. |
| Grain | What one row represents, such as one order or one customer-day. |
| Imputation | Replacing missing values using an explicit rule. |
| Join / merge | Combining tables through matching keys. |
| Key | A field or combination of fields used to identify or match records. |
| Mask | Boolean values used to select corresponding records/elements. |
| Matrix | A two-dimensional array of numbers. |
| Missing value | An absent or unknown entry; its meaning must be investigated. |
| NaN / NA / NULL | Missing-value markers whose exact behavior depends on Python/library/SQL context. |
| Normalization | An overloaded term: may mean text cleanup, a numeric rescaling, or database design. State which. |
| Outlier | An observation unusually far from others; it may be valid or erroneous. |
| Pivot | Reshaping data to put groups along rows/columns, often with aggregation. |
| Provenance | Where data came from and how they were transformed. |
| Schema | Expected fields, types, and structural constraints of data. |
| Series | A labeled one-dimensional pandas object. |
| Shape | The size of each array dimension, such as `(100, 3)`. |
| SQL | A language for querying and manipulating relational data. |
| Standardization | Often subtracting a mean and dividing by a standard deviation. |
| Tensor | A multidimensional numerical object; usage and rank conventions depend on context. |
| Vector | A one-dimensional collection of numbers. |
| Vectorization | Expressing operations on whole arrays instead of Python-level item loops. |

## Statistics and mathematics

| Term | Plain English meaning |
|---|---|
| Base rate | How common an event is in the relevant population. |
| Bias | Systematic distortion in estimation or selection; in a neural layer, also an additive parameter. |
| Bootstrap | Repeated resampling with replacement to study variability under stated assumptions. |
| Causation | A change in one factor produces a change in another under an appropriate causal interpretation. |
| Conditional probability | Probability within a specified condition or subgroup. |
| Confidence interval | An interval produced by a procedure with stated long-run coverage under assumptions. |
| Confounder | A variable that can distort an apparent causal relationship. |
| Correlation | A measure of association; it does not by itself establish causation. |
| Derivative | Local rate of change of a function with respect to an input. |
| Distribution | The pattern of values and their frequencies/probabilities. |
| Dot product | Multiply corresponding vector entries and add the products. |
| Effect size | The magnitude of a difference or relationship, in a specified scale. |
| Expected value | A probability-weighted average. |
| Gradient | A collection of derivatives of a function with respect to its inputs/parameters. |
| IID | Independent and identically distributed: a modeling assumption about observations. |
| Mean | Sum divided by number of observations. |
| Median | The middle value of ordered data, or a convention for the two middle values. |
| Null hypothesis | A specified baseline claim used in a statistical test. |
| p-value | Probability under a null model of a test result at least as extreme as observed. |
| Percentile | A threshold associated with a given proportion of the distribution. |
| Percentage point | Absolute difference between percentages: 20% to 30% is 10 points. |
| Population | The full group about which a question is asked. |
| Sample | Observations actually collected from a population or process. |
| Sampling bias | Systematic difference between what is observed and the intended population. |
| Standard deviation | A measure of the spread of observations around their mean. |
| Standard error | Variability of an estimator across possible samples. |
| Variance | Average squared deviation under the chosen population/sample convention. |

## Machine learning and AI

| Term | Plain English meaning |
|---|---|
| Accuracy | Fraction of predictions that are correct. |
| Activation | A transformation, often nonlinear, applied within a neural network. |
| AI | Broad field concerned with systems performing tasks associated with intelligence. |
| Backpropagation | Efficient gradient computation through a composed network using the chain rule. |
| Baseline | A simple reference method that a proposed solution must be compared with. |
| Batch | A subset of training examples processed together. |
| Calibration | Agreement between predicted probabilities and observed frequencies. |
| Classification | Predicting a discrete category. |
| Clustering | Grouping examples by a similarity-based method without supplied class labels. |
| Confusion matrix | Counts of predicted versus actual categories. |
| Cross-validation | Repeated training/validation partitions within development data for assessment/selection. |
| Data leakage | Information entering a model/evaluation that would not be available in the intended use. |
| Deep learning | Learning with neural networks containing multiple processing layers. |
| Drift | Change in input distributions or relationships over time; specify which kind. |
| Embedding | A numeric representation, often learned, of an item such as a word or document. |
| Epoch | One complete pass through the training examples. |
| F1 | Harmonic mean of precision and recall under a specified averaging rule. |
| Feature | An input used by a model. |
| Feature engineering | Constructing useful model inputs from available information. |
| Fine-tuning | Further training an existing model on selected data/objectives. |
| Fit | Learn a model or transformation's quantities from data. |
| Generalization | Performance on relevant examples beyond the training data. |
| Generative AI | Models that produce new content, such as text or images. |
| Gradient descent | Iteratively adjusting parameters opposite the gradient to reduce an objective. |
| Hallucination | Generated content that is unsupported or false despite plausible presentation. |
| Hyperparameter | A chosen model/training setting rather than a quantity directly fitted in the main training step. |
| Inference | Applying a trained model; in statistics, drawing conclusions from evidence is another meaning. |
| Label / target | The desired output supplied for supervised training. |
| Learning rate | Step-size control for parameter updates. |
| LLM | Large language model: a large trained model for processing/generating language. |
| Loss | The numerical objective used to guide model fitting. |
| MAE | Mean absolute error, in the target's units. |
| Metric | A defined measurement used to evaluate performance or outcomes. |
| ML | Machine learning: methods that learn patterns from data. |
| Model | A learned or specified mapping/representation used for prediction or understanding. |
| Neural network | A parameterized composition of layers that transforms inputs into outputs. |
| NLP | Natural language processing: computational work with human language. |
| One-hot encoding | Representing categories with indicator columns. |
| Overfitting | Learning training-specific patterns that do not transfer adequately to new data. |
| PCA | Principal component analysis: a linear representation emphasizing directions of variance. |
| Pipeline | A sequence that combines preprocessing and an estimator in one fitted workflow. |
| Precision | True positives divided by predicted positives, for a defined positive class. |
| Pretraining | Initial broad training before later adaptation or task-specific use. |
| Prompt | Instructions and/or context supplied to a model at inference. |
| Prompt injection | Untrusted content attempting to redirect a model application's instructions or actions. |
| RAG | Retrieval-augmented generation: retrieve evidence and supply it to a generator. |
| Recall | True positives divided by actual positives. |
| Regression | Predicting a numerical outcome. |
| Regularization | Constraints/penalties that discourage excessive model complexity. |
| Reinforcement learning | Learning behavior through actions and rewards in sequential interaction. |
| Retrieval | Finding relevant items or passages from a collection. |
| RMSE | Square root of mean squared error, in the target's units. |
| ROC-AUC | Area under the ROC curve, summarizing ranking across classification thresholds. |
| Seed | An initialization input used to reproduce a pseudorandom sequence. |
| Supervised learning | Learning from examples paired with desired outputs. |
| Test set | Held-back data reserved for final evaluation after development decisions. |
| TF-IDF | Term weighting based on within-document frequency and across-document rarity. |
| Threshold | A cutoff used to turn a score into a decision. |
| Token | A unit used by a language tokenizer; not necessarily a whole word. |
| Training set | Data used to fit model parameters and training-side transformations. |
| Transformer | A neural architecture using attention to combine information across positions. |
| Underfitting | A model failing to capture useful structure available in the data. |
| Unsupervised learning | Finding structure without supplied prediction targets. |
| Validation set | Data used during development to compare or tune choices. |

## Often-confused pairs

- **`=` / `==`:** assignment / equality comparison.
- **`print` / `return`:** display a value / supply a function's result to its caller.
- **`pip install` / `import`:** install a package into an environment / use a module in code.
- **Editor / interpreter:** where you write / what runs the code.
- **Standard deviation / standard error:** observation spread / estimator variability.
- **Percentage / percentage points:** proportional quantity / difference between percentages.
- **Prediction / explanation:** a useful forecast need not reveal a causal mechanism.
- **Validation / test:** development decisions / final held-back assessment.
- **Retrieval / generation:** find evidence / produce content.
- **Prompting / fine-tuning:** supply inference context / update model weights.
