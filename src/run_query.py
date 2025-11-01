import os, json, csv, time
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime
from rich import print
import pandas as pd
from rich.console import Console
from rich.table import Table
from src.safety import is_safe_prompt

load_dotenv()
client = OpenAI()

PROMPT_TEMPLATE = open("prompts/main_prompt.txt").read()


def run_query(question: str):
    if not is_safe_prompt(question):
        result = {
            "answer": "Unsafe prompt detected.",
            "confidence": 0.0,
            "actions": [],
            "metrics": {},
        }
        return result

    start = time.time()
    response = client.chat.completions.create(
        model=os.getenv("MODEL_NAME"),
        messages=[
            {"role": "user", "content": PROMPT_TEMPLATE + f"\nQuestion: {question}"}
        ],
    )
    end = time.time()

    tokens = response.usage
    latency_ms = (end - start) * 1000
    estimated_cost_usd = tokens.total_tokens * 0.000005

    output_llm = response.choices[0].message.content.strip()

    parsed_response = json.loads(output_llm)

    result = {
        **parsed_response,
        "metrics": {
            "tokens": {
                "prompt": tokens.prompt_tokens,
                "completion": tokens.completion_tokens,
                "total": tokens.total_tokens,
            },
            "latency_ms": round(latency_ms, 2),
            "estimated_cost_usd": round(estimated_cost_usd, 6),
        },
    }

    # log metrics
    with open("metrics/metrics.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                datetime.now().isoformat(),
                tokens.prompt_tokens,
                tokens.completion_tokens,
                tokens.total_tokens,
                latency_ms,
                estimated_cost_usd,
            ]
        )

    print(result)

    display_csv_as_table("metrics/metrics.csv")
    return result


def display_csv_as_table(csv_file_path: str):

    console = Console()

    metric_csv = pd.read_csv(csv_file_path)

    table = Table(
        title="Metrics Data from CSV", show_header=True, header_style="bold magenta"
    )
    for column in metric_csv.columns:
        table.add_column(str(column), style="cyan")

    for index, row in metric_csv.iterrows():
        table.add_row(*[str(cell) for cell in row.values])

    console.print(table)


if __name__ == "__main__":
    import sys

    question = " ".join(sys.argv[1:]) or input("Enter your question: ")
    run_query(question)
