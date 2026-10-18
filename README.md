import pypandoc, os
content = r"""# System One — Market Question Classification Mini-Exercise

A small Python experiment exploring whether a lightweight local language model can act as a first-pass filter for a market-focused application.

## Objective

The goal is to test `tev1:0.8b` locally through Ollama and check whether it can distinguish market-related questions from unrelated or ambiguous questions before they are passed to a more capable model.

This is a learning exercise and prototype, not a production-ready safety or routing system.

## How it works

1. The script defines a set of 20 test questions, including market-related, unrelated, and ambiguous examples.
2. It sends each question to the local `tev1:0.8b` model through the project's Ollama integration.
3. The model's classification is read from the `is_market_related.noul` result.
4. The script reports the classification and measures response time for each question.
5. At the end, it reports timing statistics, including total, average, fastest, and slowest response time.

### High-level flow

```text
Test question
     |
     v
Python script (main.py)
     |
     v
Local Ollama model: tev1:0.8b
     |
     v
Market-related / unrelated classification
     |
     v
Display result and response-time statistics
```

## Requirements

- Linux, macOS, or Windows
- Python 3
- [Ollama](https://ollama.com/) installed and running
- The `tev1:0.8b` model available locally
- The Python dependencies and Ollama integration used by this project

## Setup

### 1. Check Ollama

Make sure Ollama is installed and its service is running. The local API normally listens on:

```text
http://localhost:11434
```

Confirm that the model is available:

```bash
ollama list
```

If `tev1:0.8b` is not listed, use the model installation command appropriate for the source from which you obtained it.

### 2. Prepare the Python environment

From the project directory, create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the project's dependencies using its dependency file, if one is provided:

```bash
pip install -r requirements.txt
```

If the project does not yet have a `requirements.txt`, install the dependencies required by the current implementation before running the script.

## Run the experiment

From the project directory, with the virtual environment activated and Ollama running:

```bash
python3 main.py
```

The script runs the test questions and prints their classifications and response-time measurements.

## Ollama environment check

If the project includes the `check_ollama.sh` helper script, it can be used to check the local Ollama setup:

```bash
chmod +x check_ollama.sh
./check_ollama.sh
```

The checker was designed to verify items such as the Ollama installation, service/API availability, model availability, and API listing. A successful check means the local environment appears ready for the experiment; it does not prove that the model classifies every question correctly.

## What this exercise evaluates

- **Topic classification:** whether the model recognizes market-related questions.
- **Handling of unrelated questions:** whether it identifies questions outside the intended topic.
- **Ambiguous inputs:** how it responds when a question is not clearly in either category.
- **Latency:** how long individual requests take and how response times vary across the test set.

## Limitations

- A small set of 20 questions is useful for experimentation but is not enough to establish reliable real-world accuracy.
- Timing can vary with hardware load, model warm-up, and other running processes.
- A small language model can misclassify questions or produce inconsistent results.
- A classifier should not be treated as a security boundary. If this filter is later used in an application, validate its output and enforce topic restrictions in the application logic as well.
- This experiment measures classification behavior and latency; it does not by itself demonstrate the quality of financial analysis or market answers.

## Possible next steps

- Record expected labels for all test questions and calculate accuracy, precision, recall, and a confusion matrix.
- Add more examples, especially ambiguous questions and attempts to move the conversation off-topic.
- Compare results and latency with a larger model.
- If the filter performs well enough, evaluate it as an optional first stage before sending market-related questions to a larger model.

## Project status

**Status:** Mini-exercise / local prototype.

The purpose is to learn how a lightweight local model behaves as a topic filter before deciding whether this extra layer is worthwhile in the larger System One application.
"""
out = "/mnt/data/README_System_One_tev1.md"
pypandoc.convert_text(content, "md", format="md", outputfile=out, extra_args=["--standalone"])
print(f"Created: {out}")
