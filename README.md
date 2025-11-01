# Multi-Task Text Utility

A Python-based utility leveraging OpenAI GPT models to answer user questions, enforce prompt safety, and log cost, latency, and token metrics.

## Features

- **OpenAI Integration:** Uses GPT-4o-mini for conversational AI.
- **Prompt Safety:** Filters unsafe prompts using a custom safety module.
- **JSON Output:** Ensures responses follow a strict JSON schema.
- **Metrics Logging:** Tracks tokens, latency, and estimated cost per query in CSV.
- **Configurable Prompt:** Easily modify the main prompt template.
- **Unit Tests:** Includes basic tests for output validation.

## Project Structure

```
.
├── main.py
├── src/
│   ├── run_query.py
│   └── safety.py
├── prompts/
│   └── main_prompt.txt
├── metrics/
│   └── metrics.csv
├── tests/
│   └── test_core.py
├── reports/
│   └── PL_report.md
├── .env.example
├── pyproject.toml
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) (for dependency management)

### Installation

1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd assignment-1
   ```

2. **Install dependencies using uv:**
   ```sh
   uv sync
   ```

3. **Set up environment variables:**
   - Copy `.env.example` to `.env` and add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

### Usage

Run the main query script:

```sh
uv run src/run_query.py  # Ensure dependencies are installed
```

Or interactively:

```sh
python src/run_query.py
```

## Testing

Run unit tests with:

```sh
uv run  # Ensure test dependencies are installed
pytest
```

## Configuration

- **Prompt Template:** Edit [`prompts/main_prompt.txt`](prompts/main_prompt.txt) to change system instructions.
- **Safety Module:** Update unsafe keywords in [`src/safety.py`](src/safety.py).
- **Metrics:** Review usage logs in [`metrics/metrics.csv`](metrics/metrics.csv).

## Metrics

Each query logs:
- Prompt, completion, and total tokens
- Latency (ms)
- Estimated cost (USD)

See [`reports/PL_report.md`](reports/PL_report.md) for summary statistics.

## License

This project is for educational purposes.

## Authors

- Theophilus Adukpo

## References

- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [uv](https://github.com/astral-sh/uv)