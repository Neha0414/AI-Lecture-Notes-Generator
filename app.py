import subprocess

print("Step 1: Converting speech to text...")
subprocess.run(["python", "speech_to_text.py"])

print("\nStep 2: Generating notes...")
subprocess.run(["python", "generate_notes.py"])

print("\nStep 3: Generating quiz...")
subprocess.run(["python", "generate_quiz.py"])

print("\nStep 4: Generating flashcards...")
subprocess.run(["python", "generate_flashcards.py"])

print("\nAll files generated successfully!")