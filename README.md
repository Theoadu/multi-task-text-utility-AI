# Multi-Task Text Utility

![alt text](<Screenshot 2025-11-01 at 4.20.23 AM.png>)

A Python-based conversational AI utility leveraging large language models to answer user questions while enforcing prompt safety and tracking comprehensive usage metrics.

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Testing](#testing)
- [Metrics & Monitoring](#metrics--monitoring)
- [Configuration](#configuration)
- [Demo](#demo)
- [License](#license)

## 🎯 Overview

This project implements an intelligent text processing utility that acts as a support assistant. It takes user questions, validates them for safety, processes them through a large language model (LLM), and returns structured JSON responses with confidence scores and suggested actions. The system also logs detailed metrics for cost analysis, performance monitoring, and usage tracking.

### Key Capabilities

- **Conversational AI**: Provides helpful, context-aware responses to user queries
- **Safety Filtering**: Pre-processes prompts to detect and block potentially unsafe content
- **Structured Output**: Enforces JSON schema compliance for consistent, parseable responses
- **Metrics Tracking**: Logs token usage, latency, and estimated costs for every query
- **Rich Console Output**: Displays results and metrics in formatted tables using Rich library

## 🏗️ Architecture

### System Design

The application follows a simple pipeline architecture with three main stages:

```
┌─────────────┐      ┌──────────────┐      ┌─────────────┐      ┌──────────────┐
│   User      │ ───> │    Safety    │ ───> │     LLM     │ ───> │   Metrics    │
│   Input     │      │   Validator  │      │  Processing │      │   Logging    │
└─────────────┘      └──────────────┘      └─────────────┘      └──────────────┘
                            │                      │                     │
                            │                      │                     │
                      [Blocked if               [Llama 3.3]          [CSV File]
                       unsafe]                  [70B Model]          [+ Display]
```

### Component Breakdown

#### 1. **Entry Point** (`run_query.py`)
- Main orchestrator that coordinates all components
- Handles CLI arguments and user input
- Manages the complete request-response lifecycle
- Integrates safety checks, LLM calls, and metrics logging

#### 2. **Safety Module** (`safety.py`)
- Keyword-based content filtering system
- Checks for potentially harmful or unsafe prompts
- Returns boolean safety status
- Current implementation uses simple pattern matching

#### 3. **LLM Integration**
- Uses OpenAI Python SDK for API communication
- Currently configured for **Llama 3.3 70B** model
- Enforces structured JSON output through prompt engineering
- Extracts token usage and timing metrics from API responses

#### 4. **Metrics System**
- CSV-based logging for historical tracking
- Captures per-query statistics:
  - Timestamp
  - Token counts (prompt, completion, total)
  - Latency (milliseconds)
  - Estimated cost (USD)
- Rich table visualization for console display

#### 5. **Prompt Template** (`prompts/main_prompt.txt`)
- Defines system behavior and output format
- Enforces JSON schema with specific fields:
  - `answer`: The response text
  - `confidence`: Float between 0-1
  - `actions`: List of suggested steps

### Data Flow

1. **Input Phase**: User provides a question via CLI or interactive prompt
2. **Safety Check**: Question is validated against unsafe keyword list
3. **LLM Processing**: If safe, question is sent to LLM with system prompt
4. **Response Parsing**: JSON response is extracted and validated
5. **Metrics Collection**: Usage data is calculated and logged to CSV
6. **Output Display**: Results and metrics table shown in console

### Design Patterns

- **Pipeline Pattern**: Sequential processing stages with early exit on failure
- **Template Method**: Prompt template defines structure, content varies
- **Singleton Client**: Single OpenAI client instance for all requests
- **Lazy Loading**: Prompt template loaded once at module initialization

## 🛠️ Technology Stack

### Core Technologies

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|  
| **Language** | Python | 3.13+ | Primary development language |
| **LLM Model** | Llama 3.3 | 70B | Large language model for text generation |
| **LLM API** | OpenAI SDK | 2.6.1 | API client for model interaction |
| **Package Manager** | uv | Latest | Fast Python dependency management |

### Key Dependencies

#### Production Dependencies
- **openai** (2.6.1): API client for LLM communication
- **python-dotenv** (1.1.1): Environment variable management
- **rich** (14.2.0+): Terminal formatting and table display
- **pandas** (2.3.3+): CSV data manipulation and analysis
- **pydantic** (2.12.3): Data validation and settings management

#### HTTP & Networking
- **httpx** (0.28.1): Modern HTTP client with async support
- **httpcore** (1.0.9): Low-level HTTP transport
- **certifi** (2025.10.5): SSL certificate bundle

#### Development Dependencies
- **pytest**: Unit testing framework (via test imports)

### Infrastructure

- **Environment**: `.env` file for secrets management
- **Version Control**: Git
- **File Storage**: CSV for metrics, TXT for prompts
- **Console**: Rich library for enhanced terminal output

## ✨ Features

### 1. **AI-Powered Responses**
- Leverages Llama 3.3 70B model for high-quality answers
- Context-aware and conversational
- Structured JSON output for easy integration

### 2. **Prompt Safety**
- Pre-filters potentially harmful content
- Keyword-based detection for unsafe prompts
- Returns safe error message for blocked queries

### 3. **JSON Schema Enforcement**
- Guarantees consistent response format
- Includes confidence scores for answer quality
- Provides actionable steps for user guidance

### 4. **Comprehensive Metrics**
- Real-time token tracking (prompt, completion, total)
- Latency measurement in milliseconds
- Cost estimation for budgeting and analysis
- CSV export for historical analysis

### 5. **Rich Console Experience**
- Color-coded terminal output
- Formatted tables for metrics display
- Clear visual feedback for all operations

### 6. **Flexible Input**
- Command-line arguments support
- Interactive prompt mode
- Easy integration into scripts

## 📁 Project Structure

```
assignment-1/
│
├── src/                          # Source code
│   ├── __init__.py              # Package initializer
│   ├── run_query.py             # Main application logic
│   └── safety.py                # Safety validation module
│
├── prompts/                      # Prompt templates
│   └── main_prompt.txt          # System prompt for LLM
│
├── metrics/                      # Usage tracking
│   └── metrics.csv              # Query metrics log
│
├── reports/                      # Documentation
│   └── PL_report.md            # Project lifecycle report
│
├── tests/                        # Unit tests
│   ├── conftest.py              # Pytest configuration
│   └── test_core.py             # Core functionality tests
│
├── .env                          # Environment variables (local)
├── .env.example                  # Environment template
├── .gitignore                    # Git ignore rules
├── .python-version               # Python version specification
├── pyproject.toml                # Project dependencies
├── uv.lock                       # Locked dependency versions
└── README.md                     # This file
```

### Key Files

- **`src/run_query.py`**: Main entry point containing `run_query()` function and CLI logic
- **`src/safety.py`**: Safety validator with `is_safe_prompt()` function
- **`prompts/main_prompt.txt`**: System prompt defining LLM behavior and output format
- **`metrics/metrics.csv`**: Historical log of all query metrics
- **`pyproject.toml`**: Project metadata and dependency specifications

## 🚀 Getting Started

### Prerequisites

- **Python 3.13+**: Required for latest language features
- **uv**: Fast Python package manager ([installation guide](https://github.com/astral-sh/uv))
- **OpenAI API Key**: Access to LLM models (or compatible API endpoint)

### Installation

1. **Clone the repository:**
   ```bash
   git clone git@github.com:Theoadu/multi-task-text-utility-AI.git
   cd multi-task-text-utility-AI
   ```

2. **Install dependencies using uv:**
   ```bash
   uv sync
   ```
   This will create a virtual environment and install all dependencies from `uv.lock`.

3. **Set up environment variables:**
   
   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   OPENAI_BASE_URL=https://api.openai.com/v1
   MODEL=llama-3.3-70b
   ```

4. **Verify installation:**
   ```bash
   uv run python -c "from src.run_query import run_query; print('Setup successful!')"
   ```

## 📖 Usage

### Command Line Interface

**With command-line arguments:**
```bash
uv run src/run_query.py How can I reset my password?
```

**Interactive mode:**
```bash
uv run src/run_query.py
# Will prompt: Enter your question:
```

### Programmatic Usage

```python
from src.run_query import run_query

# Ask a question
result = run_query("What are the best practices for API security?")

# Access response fields
print(result["answer"])           # The answer text
print(result["confidence"])       # Confidence score (0-1)
print(result["actions"])          # List of suggested actions
print(result["metrics"])          # Token usage and performance data
```

### Response Format

```json
{
  "answer": "API security best practices include...",
  "confidence": 0.95,
  "actions": [
    "Use HTTPS for all communications",
    "Implement rate limiting",
    "Validate all inputs"
  ],
  "metrics": {
    "tokens": {
      "prompt": 102,
      "completion": 81,
      "total": 183
    },
    "latency_ms": 1087.22,
    "estimated_cost_usd": 0.000915
  }
}
```

### Safety Handling

When an unsafe prompt is detected:
```json
{
  "answer": "Unsafe prompt detected.",
  "confidence": 0.0,
  "actions": [],
  "metrics": {}
}
```

## 🧪 Testing

### Run Unit Tests

```bash
# Run all tests
uv run pytest

# Run with verbose output
uv run pytest -v

# Run specific test file
uv run pytest tests/test_core.py

# Run with coverage report
uv run pytest --cov=src
```

### Test Coverage

Current test suite includes:
- JSON output validation
- Required field verification
- Token count type checking

**Note**: Tests currently make live API calls. Consider mocking for faster, deterministic tests.

## 📊 Metrics & Monitoring

### Metrics CSV Format

```csv
timestamp,tokens_prompt,tokens_completion,total_tokens,latency_ms,estimated_cost_usd
2025-11-01T02:34:51.904044,102,81,183,1087.22,0.000915
```

### Viewing Metrics

Metrics are automatically displayed after each query in a formatted table:

```
┌────────────────────────┬───────────────┬────────────────────┬──────────────┬─────────────┬────────────────────┐
│ timestamp              │ tokens_prompt │ tokens_completion  │ total_tokens │ latency_ms  │ estimated_cost_usd │
├────────────────────────┼───────────────┼────────────────────┼──────────────┼─────────────┼────────────────────┤
│ 2025-11-01T02:34:51... │ 102           │ 81                 │ 183          │ 1087.22     │ 0.000915           │
└────────────────────────┴───────────────┴────────────────────┴──────────────┴─────────────┴────────────────────┘
```

### Analysis

Use pandas to analyze historical metrics:

```python
import pandas as pd

df = pd.read_csv('metrics/metrics.csv')
print(f"Average latency: {df['latency_ms'].mean():.2f}ms")
print(f"Total cost: ${df['estimated_cost_usd'].sum():.6f}")
print(f"Average tokens: {df['total_tokens'].mean():.0f}")
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file with:
```env
OPENAI_API_KEY=sk-...                    # Required: 

Your API key
```

### Customizing the Prompt

Edit `prompts/main_prompt.txt` to modify:
- System behavior
- Response tone
- Output format requirements
- Additional constraints

Example:
```
You are a technical support expert. Always respond in JSON:
{
  "answer": "string",
  "confidence": float (0 to 1),
  "actions": ["list", "of", "suggested", "steps"],
  "urgency": "low|medium|high"
}

Be technical, precise, and include relevant documentation links.
```

### Modifying Safety Rules

Edit `src/safety.py` to adjust the unsafe keyword list:

```python
def is_safe_prompt(text: str) -> bool:
    unsafe = ["kill", "hack", "terror", "illegal", "bomb"]
    # Add or remove keywords as needed
    return not any(word in text.lower() for word in unsafe)
```

### Changing the Model

In `src/run_query.py`, line 30:
```python
response = client.chat.completions.create(
    model="llama-3.3-70b",  # Change to: "gpt-4", "gpt-3.5-turbo", etc.
    messages=[...]
)
```

**Note**: Update cost estimation (line 39) when changing models.

## 🎬 Demo

[![asciicast](https://asciinema.org/a/ufuc9ZaOgyUXEO6OyPGBxRYC4.svg)](https://asciinema.org/a/ufuc9ZaOgyUXEO6OyPGBxRYC4)

## 📈 Performance Characteristics

Based on metrics from production usage:

| Metric | Average | Range |
|--------|---------|-------|
| Latency | ~2.5s | 1-6.5s |
| Prompt Tokens | ~90 | 73-102 |
| Completion Tokens | ~87 | 81-97 |
| Total Tokens | ~177 | 154-198 |
| Cost per Query | $0.0009 | $0.00077-$0.00099 |

*Based on Llama 3.3 70B model with current pricing*

## 🔒 Security Considerations

- **API Keys**: Never commit `.env` files to version control
- **Input Validation**: Current safety module is basic; consider OpenAI Moderation API
- **Rate Limiting**: No built-in rate limiting; implement if needed
- **Error Messages**: Avoid exposing sensitive system information in errors

## 🐛 Known Issues & Limitations

1. **Safety Module**: Simple keyword matching can be bypassed; not production-ready
2. **Error Handling**: Limited error handling for network failures or API errors
3. **JSON Parsing**: Assumes LLM always returns valid JSON; may crash otherwise
4. **CSV Management**: No file rotation; metrics.csv will grow indefinitely
5. **Testing**: Tests make live API calls; expensive and non-deterministic

## 🚧 Future Improvements

- [ ] Integrate OpenAI Moderation API for robust safety checking
- [ ] Add comprehensive error handling and retry logic
- [ ] Implement response caching to reduce API costs
- [ ] Add async support for concurrent queries
- [ ] Create web UI for easier interaction
- [ ] Add metrics aggregation and reporting dashboard
- [ ] Implement chain-of-thought prompting for complex queries
- [ ] Add support for multiple LLM providers
- [ ] Create Docker container for easy deployment

## 📄 License

This project is developed for educational purposes as part of Henry's Module 1 coursework.

## 👤 Author

**Theophilus Adukpo**

## 📚 References

- [OpenAI Python SDK Documentation](https://github.com/openai/openai-python)
- [uv Package Manager](https://github.com/astral-sh/uv)
- [Rich Terminal Library](https://github.com/Textualize/rich)
- [Llama 3.3 Model Card](https://huggingface.co/meta-llama/Llama-3.3-70B)

## 🤝 Contributing

This is an educational project. For questions or suggestions, please reach out to the author.

---

**Last Updated**: November 2025
