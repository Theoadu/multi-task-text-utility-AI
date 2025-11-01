import os, json, csv, time
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime
from src.safety import is_safe_prompt

load_dotenv()
client = OpenAI(
    base_url="https://api.cerebras.ai/v1", api_key=os.getenv("CEREBRAS_API_KEY")
)

PROMPT_TEMPLATE = open("prompts/main_prompt.txt").read()


def run_query(question: str):
    print(is_safe_prompt(question))
    if not is_safe_prompt(question):
        result = {
            "answer": "Unsafe prompt detected.",
            "confidence": 0.0,
            "actions": [],
            "metrics": {},
        }
        print(result)
        return result

    start = time.time()
    response = client.chat.completions.create(
        model="llama-3.3-70b",
        messages=[
            {"role": "user", "content": PROMPT_TEMPLATE + f"\nQuestion: {question}"}
        ],
    )
    end = time.time()

    tokens = response.usage
    latency_ms = (end - start) * 1000
    estimated_cost_usd = tokens.total_tokens * 0.000005

    result = {
        "answer": response.choices[0].message.content.strip(),
        "confidence": 0.9,
        "actions": ["Review and respond"],
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

    print(json.dumps(result, indent=2))
    print(result)
    return result


if __name__ == "__main__":
    import sys

    question = " ".join(sys.argv[1:]) or input("Enter your question: ")
    run_query(question)
