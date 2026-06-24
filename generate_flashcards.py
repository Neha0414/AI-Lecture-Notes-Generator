# import ollama

# with open("transcripts/transcript.txt", "r", encoding="utf-8") as file:
#     transcript = file.read()

# import ollama
# import os

# os.makedirs("flashcards", exist_ok=True)

# with open("transcripts/transcript.txt", "r", encoding="utf-8") as file:
#     transcript = file.read()

# prompt = f"""
# You are a study flashcard generator.

# Create EXACTLY 10 flashcards from the lecture transcript.

# RULES:
# - Use ONLY English.
# - Do NOT use any other language.
# - Number flashcards from 1 to 10.
# - Each flashcard must contain:
#   - Question
#   - Answer
# - Do NOT include markdown symbols like *, **, or ###.
# - Do NOT include transcript text.
# - Keep answers short and clear.

# FORMAT:

# Flashcard 1

# Question:
# ...

# Answer:
# ...

# --------------------------------

# Flashcard 2

# Question:
# ...

# Answer:
# ...

# LECTURE TRANSCRIPT:

# {transcript}
# """

# response = ollama.chat(
#     model="gemma3:1b",
#     messages=[{"role": "user", "content": prompt}]
# )

# flashcards = response["message"]["content"]

# with open("flashcards/flashcards.txt", "w", encoding="utf-8") as f:
#     f.write(flashcards)

# print("Flashcards generated successfully!")

# response = ollama.chat(
#     model="gemma3:1b",
#     messages=[
#         {
#             "role": "user",
#             "content": prompt
#         }
#     ]
# )

# flashcards = response["message"]["content"]

# with open("flashcards/flashcards.txt", "w", encoding="utf-8") as file:
#     file.write(flashcards)

# print(flashcards)


from groq import Groq
import os

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

os.makedirs("flashcards", exist_ok=True)

with open(
    "transcripts/transcript.txt",
    "r",
    encoding="utf-8"
) as file:
    transcript = file.read()

prompt = f"""
You are an expert teacher.

Create EXACTLY 10 study flashcards.

Requirements:
- One concept per flashcard.
- Use simple language.
- Keep answers concise.
- Use only English.
- Do not include transcript text.

Format:

# Flashcards

## Flashcard 1

Question:
...

Answer:
...

---

## Flashcard 2

Question:
...

Answer:
...

Lecture Transcript:

{transcript}
"""

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

flashcards = response.choices[0].message.content

with open(
    "flashcards/flashcards.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(flashcards)

print("Flashcards generated successfully!")
