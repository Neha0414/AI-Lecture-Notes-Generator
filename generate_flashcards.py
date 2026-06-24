import ollama

with open("transcripts/transcript.txt", "r", encoding="utf-8") as file:
    transcript = file.read()

import ollama
import os

os.makedirs("flashcards", exist_ok=True)

with open("transcripts/transcript.txt", "r", encoding="utf-8") as file:
    transcript = file.read()

prompt = f"""
You are a study flashcard generator.

Create EXACTLY 10 flashcards from the lecture transcript.

RULES:
- Use ONLY English.
- Do NOT use any other language.
- Number flashcards from 1 to 10.
- Each flashcard must contain:
  - Question
  - Answer
- Do NOT include markdown symbols like *, **, or ###.
- Do NOT include transcript text.
- Keep answers short and clear.

FORMAT:

Flashcard 1

Question:
...

Answer:
...

--------------------------------

Flashcard 2

Question:
...

Answer:
...

LECTURE TRANSCRIPT:

{transcript}
"""

response = ollama.chat(
    model="gemma3:1b",
    messages=[{"role": "user", "content": prompt}]
)

flashcards = response["message"]["content"]

with open("flashcards/flashcards.txt", "w", encoding="utf-8") as f:
    f.write(flashcards)

print("Flashcards generated successfully!")

response = ollama.chat(
    model="gemma3:1b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

flashcards = response["message"]["content"]

with open("flashcards/flashcards.txt", "w", encoding="utf-8") as file:
    file.write(flashcards)

print(flashcards)

