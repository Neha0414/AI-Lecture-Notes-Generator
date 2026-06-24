# import ollama
# import os

# # Create notes folder if it doesn't exist
# os.makedirs("notes", exist_ok=True)

# # Read transcript
# with open(
#     "transcripts/transcript.txt",
#     "r",
#     encoding="utf-8"
# ) as file:
#     transcript = file.read()

# prompt = f"""
# Create professional study notes from the lecture transcript.

# Output format:

# # Title

# ## Overview
# Short explanation

# ## Key Concepts
# - Point 1
# - Point 2

# ## Important Definitions
# - Term: Definition

# ## Main Points
# 1. Point one
# 2. Point two

# ## Summary
# Brief summary

# ## Exam Notes
# - Important topic
# - Frequently asked concept

# Rules:
# - Use markdown headings
# - Use bullet points
# - Keep notes concise
# - Do not overuse asterisks
# - Do not use decorative symbols

# Transcript:

# {transcript}
# """

# response = ollama.chat(
#     model="gemma3:1b",
#     messages=[
#         {
#             "role": "user",
#             "content": prompt
#         }
#     ]
# )

# notes = response["message"]["content"]

# # Save notes
# with open(
#     "notes/notes.txt",
#     "w",
#     encoding="utf-8"
# ) as file:
#     file.write(notes)

# print("Notes generated successfully!")

import ollama
import os

os.makedirs("notes", exist_ok=True)

with open("transcripts/transcript.txt", "r", encoding="utf-8") as file:
    transcript = file.read()

prompt = f"""
You are an expert teacher.

Convert the lecture transcript into professional study notes.

Requirements:

- Generate a suitable title.
- Create an Overview section.
- Create Key Concepts.
- Create Important Definitions.
- Create Main Points.
- Create a Summary section.
- Create Exam Preparation Notes.
- Use headings and bullet points.
- Keep the notes concise and easy to revise.
- Make the notes suitable for any academic topic.

Format:

# Title

## Overview

## Key Concepts

- Point

## Important Definitions

- Term: Definition

## Main Points

- Point

## Summary

## Exam Preparation Notes

Lecture Transcript:

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

notes = response["message"]["content"]

with open("notes/notes.txt", "w", encoding="utf-8") as file:
    file.write(notes)

print("Notes generated successfully!")