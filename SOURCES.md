# Resource evaluation

## What was evaluated, and how

Checked on **5 September 2026**. I compared a representative set of authoritative beginner courses, university materials, books by their authors, and official library documentation. I inspected course descriptions, prerequisite statements, contents, and relevant documentation pages. I did not complete every assignment or independently test every external example. This is an editorial selection for your goals, not an exhaustive internet census or a quantified ranking of learning outcomes.

Selection criteria: **beginner suitability, exercise quality, progression, relevance to analytics/ML/AI apps, technical currency, author/provider authority, and access friction**. The verdicts are my judgments based on those criteria. A prestigious or popular resource can still be inappropriate at the beginning.

The course handbook and its original labs form the main path. External material is assigned selectively. Most core explanations are available without buying a certificate. Registration may be needed for hosted exercises; paid platform access, certificates, and promotions can change. Check the provider before paying.

## Python foundations

| Resource | Evaluation | Use in your course |
|---|---|---|
| [Harvard CS50P](https://cs50.harvard.edu/python/) | Explicitly accommodates people without programming experience. Includes testing, exceptions, files, and a final project. Lectures and problem sets provide a substantial practice path; some problems are demanding for a first encounter. OpenCourseWare is free. | **Primary explanatory spine**, selected topics in Modules 1–4. Completing all official problem sets and certificate requirements is extra work outside the 160-hour estimate. |
| [Python for Everybody](https://www.py4e.com/lessons) | Gentle introductory progression, moving toward files, web data, and databases. Particularly useful for a data-oriented learner who needs a slower explanation. Free materials on the author's site. | **Substitute explanations**, especially variables, loops, dictionaries, and files. Do not repeat its entire beginner sequence alongside CS50P. |
| [University of Helsinki Python MOOC 2026](https://programming-26.mooc.fi/) | University material divided into introductory Parts 1–7 and advanced Parts 8–14. Many exercises make it useful for repeated independent practice. Formal grading/exam participation is a separate commitment. | **Exercise bank** when a checkpoint reveals a weakness. Start with Parts 1–4; deepen functions and files as needed. |
| [Official Python tutorial](https://docs.python.org/3/tutorial/index.html) | Authoritative language reference/tutorial, but explicitly intended for people who already understand programming generally. That prerequisite makes it a poor sole day-one teacher. | **Lookup reference** from Module 3 onward. |
| [DeepLearning.AI: AI Python for Beginners](https://www.deeplearning.ai/courses/ai-python-for-beginners) | An approachable AI-assisted entry route with packages and APIs. Its AI-oriented format is relevant to your motivation, but independent coding checks are still necessary. The page advertises access conditions that may change. | **Optional motivation or alternative introduction**; does not replace our debugging, data-quality, and independent assessments. |

## Setup and data analysis

| Resource | Evaluation | Use in your course |
|---|---|---|
| [VS Code Python setup](https://code.visualstudio.com/docs/python/python-tutorial) and [notebook guide](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) | Official instructions distinguish editor, extension, interpreter, and notebook kernel. More reliable for interface details than old setup videos. | **Required reference** for Module 0. |
| [Python venv documentation](https://docs.python.org/3/library/venv.html) | Precise environment and activation behavior across operating systems. Dense as a first read but excellent for resolving environment confusion. | **Targeted troubleshooting**. |
| [NumPy absolute basics](https://numpy.org/doc/stable/user/absolute_beginners.html) | Official introduction to arrays, shape, indexing, and operations. Assumes enough Python to read examples. | **Core selected sections** in Module 5. |
| [pandas introductory tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html) | Small task-focused lessons map well to spreadsheet experience: loading, selection, derived columns, summaries, and combining data. | **Core selected tutorials** in Module 6. |
| [Wes McKinney: Python for Data Analysis, 3rd edition](https://wesmckinney.com/book/) | Strong author-written treatment of the Python data stack, with an open-access web edition. Published examples target older Python/pandas versions than current docs. | **Deeper companion**, selected Chapters 4, 7, 8, 10; check current APIs when examples differ. |
| [Kaggle Learn catalog](https://www.kaggle.com/learn) | Short, applied Python, pandas, and ML practice. Useful reinforcement, but brevity leaves less room for debugging and statistical reasoning. | **Optional drills** after the corresponding handbook module. Intro ML's [course page](https://www.kaggle.com/learn/intro-to-machine-learning) describes no-cost access. |
| [Matplotlib quick start](https://matplotlib.org/stable/users/explain/quick_start.html) | Official explanation of figures and axes, a solid basis for charts you can label and control. | **Core plotting reference** for Module 7. |
| [Python SQLite documentation](https://docs.python.org/3/library/sqlite3.html) | Reliable Python/database interface reference, including parameter binding. It is not by itself a full beginner SQL course. | **API reference** alongside our guided SQL lab. |

## Statistics and machine learning

| Resource | Evaluation | Use in your course |
|---|---|---|
| [OpenIntro Statistics](https://www.openintro.org/book/os/) | Broad introductory treatment of data, probability, inference, and modeling, with textbook and supporting materials. More depth than a quick ML video provides. | **Selected statistics topics** in Module 8; optional deeper study afterward. |
| [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course) | Concise concept lessons and exercises, extending into neural networks and real-world issues. Its [prerequisites](https://developers.google.com/machine-learning/crash-course/prereqs-and-prework) include Python and mathematical readiness; “ML beginner” does not mean “programming beginner.” | **ML concept companion** in Modules 9–12 after the Python/data foundation. |
| [Inria scikit-learn MOOC](https://inria.github.io/scikit-learn-mooc/) | An applied progression through tabular modeling, preprocessing, pipelines, validation, and model families. A strong fit for sound practical habits after Python basics. | **Primary applied ML companion**, selected sections in Modules 9–10. |
| [scikit-learn common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) | Direct guidance on inconsistent preprocessing, leakage, and reproducibility. Narrow scope makes it valuable at the moment these mistakes become possible. | **Required reading** during your first pipeline. |
| [An Introduction to Statistical Learning](https://www.statlearning.com/) | Author-hosted statistical-learning textbook with a Python edition and chapter labs. Excellent depth for understanding methods and evaluation; too much to stack in full onto the crash course. | **Selected resampling/model-assessment reading**; subsequent depth track. |
| [DeepLearning.AI Machine Learning Specialization](https://www.deeplearning.ai/specializations/machine-learning) | Structured conceptual and programming route through ML with Andrew Ng. Useful if you prefer a single longer video-led program. Platform/course access terms should be checked before enrollment. | **Alternative longer ML spine** to the selected Google/Inria path, not an additional mandatory course. |
| [DeepLearning.AI Mathematics for ML and Data Science](https://www.deeplearning.ai/specializations/mathematics-for-machine-learning-and-data-science) | Focused math sequence; its page expects high-school math and basic programming/ML familiarity. | **Remediation or depth option** if the Module 8 math checklist is difficult. Your existing algebra means you need not start here. |

## Neural networks and AI applications

| Resource | Evaluation | Use in your course |
|---|---|---|
| [PyTorch Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) | Official guided workflow covering data, models, training, and saving. Assumes familiarity with Python and deep-learning concepts. | **Framework bridge** after Notebook 7. |
| [fast.ai Practical Deep Learning for Coders](https://course.fast.ai/) | Motivating, application-first deep learning. Its stated prerequisite is ability to code, with high-school mathematics; it is not a replacement for learning programming. | **Post-foundation extension**, especially for vision and applied deep learning. |
| [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1) | Free, ecosystem-specific treatment of language models and NLP. It explicitly requires good Python and recommends an introductory deep-learning course first. | **Introductory chapter in Module 12**, then selected model-use/demo sections in the 40-hour bridge. |
| [Transformers pipeline guide](https://huggingface.co/docs/transformers/pipeline_tutorial) and [model cards](https://huggingface.co/docs/hub/model-cards) | Official implementation and model-context guidance. Useful for choosing a real model and recording limitations instead of relying on a bare model name. | **Application bridge references**. |

## What to postpone, and why

Avoid enrolling in several overlapping beginner tracks. You need one explanation that works, then enough independent practice to use it. Keep advanced metaprogramming, distributed data systems, complex agent frameworks, training large models from scratch, and extensive cloud infrastructure for later projects with a clear need. Basic tests, statistics, data provenance, SQL, leakage control, and evaluation remain in the core.

Random blog posts and videos are not inherently bad, but validate version-sensitive instructions against the relevant official docs. Prefer resources that state prerequisites, expose runnable examples, include exercises, and explain failure modes. Do not treat follower counts or certificate branding as proof of teaching quality.

## Research limitations and access notes

The Colab FAQ and Gradio quick-start page did not return readable content through the research tool. I did not use them as evidence for pricing, hardware guarantees, or installation requirements. The Google ML prework page supports the browser-exercise fallback, and the Hugging Face course supports the later demo-building route. The Git documentation landing page redirects; use the official [Git documentation entry](https://git-scm.com/doc) for your operating system. The supplied notebooks are separately executed and documented in `VALIDATION.md`.

All handbook explanations, original exercises, and synthetic datasets were created for this course. External resources are linked for study; their books and course materials have not been reproduced as a bundled library.
