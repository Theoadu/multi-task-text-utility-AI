import json
from src.run_query import run_query

def test_valid_json_output():
    result = run_query("How can I change my password?")
    assert "answer" in result
    assert "confidence" in result
    assert "metrics" in result
    assert isinstance(result["metrics"]["tokens"]["total"], int)