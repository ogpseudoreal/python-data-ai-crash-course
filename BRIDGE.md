# AI applications and career bridge — 40 hours

This stage follows the 160-hour foundation and directly serves your additional goals: building applications with AI models and preparing to demonstrate your skills professionally. Your **full planned route is 200 hours**, approximately **14–20 weeks at 10–15 hours/week**, before extra practice. This is career preparation; it is not a promise of employment readiness after a fixed number of hours.

The supplied eight notebooks teach and verify the core mechanics. The projects below are **learner implementation assignments**, including real model/framework integration. They are not prebuilt, executed applications in this package. This distinction is intentional: completing an original implementation is part of proving independence.

## A. Turn your trained model into an application — 8 hours

**Prerequisites:** Modules 0–14 and a capstone that passes its rubric.

Take the model pipeline you already trained. Define a request with named input fields, allowed values, and units. Write `predict_one(record)` that validates inputs, constructs a one-row DataFrame in the correct schema, calls the fitted pipeline, and returns a structured result. Keep training outside the request handler.

Use a thin local interface: a command-line prompt is sufficient for the first two hours. Then add a small form using a supported UI library, following the demo-building material in [Hugging Face's course](https://huggingface.co/learn/llm-course/chapter1/1). Display the prediction with target units and a brief explanation of the model's intended population. Do not invent a probability or confidence interval if your regression model does not produce one.

Practice request flow:

```text
User enters fields
    → validate names, types, missing values, and ranges
    → apply the fitted preprocessing + model pipeline
    → format prediction and known limitations
    → show a clear error if input is invalid
```

Test: a typical record, an unseen category, a missing required field, an out-of-range numeric value, and an extra unexpected field. Compare application predictions with direct pipeline predictions on identical records. Save the trusted model and document the library versions needed to reload it. Never load a model file from an untrusted source.

**Pass:** someone else can run it locally, enter their own values, get consistent results, and understand rejected inputs. You can explain which code runs at training time and which runs at prediction time.

## B. Use a real pretrained text model — 10 hours

Study model loading and inference in the [Transformers pipeline guide](https://huggingface.co/docs/transformers/pipeline_tutorial). Read a candidate's [model card](https://huggingface.co/docs/hub/model-cards): intended task, language, license, training/evaluation context, model size, and limitations.

Start with a **small English sentiment classifier** on public or invented short reviews. This is easier to evaluate than open-ended generation. Choose a specific model and revision, then record them. Install the current supported framework in a separate environment; do not mutate your verified core environment until you have a reason. Follow the official framework installation instructions for your hardware. Model weights must be downloaded; assess storage and memory before choosing a model. Hosted inference is an alternative, with provider-specific account and cost requirements.

Build a 30-example evaluation file before comparing models: 10 straightforward positive/negative reviews, 10 difficult cases such as negation or mixed sentiment, and 10 out-of-scope cases such as unsupported language or requests unrelated to reviews. Label the first 20 according to a written annotation rule; identify the latter 10 as out of scope rather than pretending a binary label solves them.

Run inference, save predictions, calculate relevant classification metrics on the labeled subset, and inspect errors. A model score is not automatically a calibrated real-world probability. Add maximum input length, error handling, and a clear scope statement to the interface. Compare against a simple word-rule baseline. A weaker result is acceptable if you diagnose it honestly.

**Pass:** record model/version/license, reproduce predictions, explain five mistakes, and demonstrate input validation. You have now integrated an actual pretrained model, rather than merely describing an API.

## C. Build and evaluate a document assistant — 12 hours

Extend Notebook 8's retriever over a small collection of documents you are allowed to use. The course handbook is a suitable initial corpus. Split text into meaningful passages, retain file/section identifiers, and define the retrieval query and ranking policy. Keep the small original lexical system as your baseline before experimenting with learned embeddings.

Create 25 questions: 15 answerable with identified source passages, 5 ambiguous, and 5 with no answer in the corpus. Separate a development set used for improvements from a final set held back until the design is frozen. Define retrieval success independently of answer quality.

Choose a small local instruction-following model or a hosted model. Inspect current documentation and access terms at implementation time. For a hosted model, put the API key in an environment variable, set a small spending limit, set timeouts, and keep credentials out of code and Git. No particular provider or paid subscription is required by this syllabus; choose based on current access and your hardware.

Give the generator a narrow task: answer using supplied passages, cite the passage IDs, and say when evidence is insufficient. Treat retrieved content as untrusted text. Do not give the first version tools that can send messages, modify files, or execute code. Keep the application read-only while learning.

Maintain an evaluation table with these columns:

| Field | What to record |
|---|---|
| Question ID and split | Development or final test |
| Expected evidence | Passage IDs or “not present” |
| Retrieved passages | Actual ranked IDs |
| Retrieval result | Did the top-k contain relevant evidence? |
| Answer correctness | Correct / partly correct / incorrect with explanation |
| Evidence support | Are factual claims supported by cited passages? |
| Unanswerable behavior | Did it acknowledge missing evidence? |
| Latency and cost | Measured elapsed time and actual provider usage if applicable |

Test ordinary questions, typos, unsupported questions, misleading passages, and a passage saying “ignore your instructions.” Do not declare safety from one successful injection test. Summarize what the tests cover and what remains unknown.

**Pass:** demonstrate the full request path, show retrieval and generation scores separately, reproduce five failure analyses, and explain when the system should decline an answer. The demo must execute with a real model; a mocked response does not pass this stage.

## D. Turn the work into career evidence — 10 hours

Create two distinct case studies: your independent analytics/ML capstone and your evaluated AI application. Each needs a question, data/model sources, setup/run instructions, methods, checks, results, failure cases, and a short demo. Screenshots alone are insufficient. Remove credentials and private data before sharing anything publicly.

Spend 3 hours improving the READMEs and code organization; 2 hours adding missing tests and fixing rerun problems; 2 hours writing one-page case studies; 2 hours practicing explanations and SQL/Python problems; 1 hour having another person run a project. If their run fails, repair it and repeat the handoff even if that requires more time.

Practice these interview-style prompts without generated answers:

1. Given duplicate orders and missing prices, define a defensible cleaning policy.
2. Write a grouping calculation in Python, pandas, and SQL; compare the results.
3. Explain why a random split can fail for time series or repeated customers.
4. Choose a metric for a rare-event classifier and defend the tradeoff.
5. Explain a model error and one experiment that could diagnose its cause.
6. Trace a user's request through your model application.
7. Distinguish missing retrieval evidence from an unsupported generated answer.
8. Identify the next improvement you would make with one more day, and why.

**Pass:** both projects rerun from their documented setup; you can answer the eight prompts with reference to your own work; a reviewer can identify at least one original decision and one failure you investigated. Repeat projects in another domain to build experience. A certificate can supplement this evidence but cannot replace it.

## Budget and equipment

The supplied core runs on CPU and needs no paid AI account. This bridge may require model downloads or optional paid hosted inference; exact cost depends on your later model choice and usage. Do not buy a GPU or long subscription to begin. Choose a small test workload, measure its memory/time/cost, and expand only after the evaluation works. Revisit current provider documentation when implementing, since model availability and prices change.
