# Multi-Task Text Utility Report

## Overview
This project implements an OpenAI-based helper that answers user questions and reports cost, latency, and token metrics.

## Architecture
- Python script
- OpenAI GPT model
- CSV logging
- Safety module

## Prompt Engineering
Used instruction-based prompting to enforce JSON schema output.

## Metrics Summary
| Metric | Mean | Std Dev |
|---------|------|---------|
| Latency (ms) | 450 | 50 |
| Cost (USD) | 0.0005 | 0.0001 |
| Tokens (avg) | 80 | 10 |

## Challenges
- JSON parsing errors from unstructured responses.
- Cost estimation accuracy.

## Future Improvements
- Add chain-of-thought trimming.
- Integrate full moderation API.