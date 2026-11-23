#!/usr/bin/env python3
# Out-of-office reply (1 sentence, 104 chars, pure stdlib): writes the reply to /output/entry.txt.
import os

REPLY = "I have gone on vacation, where my only scheduled task is to ignore scheduled tasks, starting with yours."

def main():
    os.makedirs("/output", exist_ok=True)
    text = REPLY.strip()
    assert 1 <= len(text) <= 160, f"length {len(text)} out of range"
    assert REPLY == REPLY.strip(), "stray whitespace around reply"
    assert "  " not in text, "double space in reply"
    assert "\n" not in text and "\t" not in text, "stray whitespace in reply"
    # Exactly one sentence: one terminal period, no other sentence terminators.
    assert text.endswith("."), "must end with a terminal period"
    assert "?" not in text and "!" not in text, "no extra sentence terminators"
    assert text.count(".") == 1, "more than one sentence"
    assert ". " not in text, "more than one sentence"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
