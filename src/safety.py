def is_safe_prompt(text: str) -> bool:
    unsafe = ["kill", "hack", "terror", "illegal", "bomb"]
    return not any(word in text.lower() for word in unsafe)