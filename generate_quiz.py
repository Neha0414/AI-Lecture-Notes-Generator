import ollama

with open("transcripts/transcript.txt", "r", encoding="utf-8") as file:
    transcript = file.read()

prompt = f"""
You are a quiz generator.

TASK:
Generate exactly 10 multiple-choice questions from the lecture.

RULES:
- Generate ONLY the quiz.
- DO NOT repeat the lecture transcript.
- DO NOT summarize the lecture.
- DO NOT write "Transcript".
- DO NOT include any content other than the quiz.
- Generate exactly 10 questions.
- Each question must have 4 options.
- Include the correct answer.
- Include a short explanation.

FORMAT:

# Quiz

## Question 1

Question text

A. Option A
B. Option B
C. Option C
D. Option D

Correct Answer: A

Explanation: Explanation here.

---

LECTURE:
{transcript}
"""
response = ollama.chat(
    model="gemma3:1b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

quiz = response["message"]["content"]

with open("quizzes/quiz.txt", "w", encoding="utf-8") as file:
    file.write(quiz)

print(quiz)

