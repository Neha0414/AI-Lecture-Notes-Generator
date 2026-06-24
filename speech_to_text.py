# import whisper
# import os

# model = whisper.load_model("base")

# # Get all mp3 files in audio folder
# audio_files = [
#     f for f in os.listdir("audio")
#     if f.endswith(".mp3")
# ]

# if not audio_files:
#     raise FileNotFoundError("No MP3 file found in audio folder.")

# # Select the latest uploaded file
# latest_audio = max(
#     [os.path.join("audio", f) for f in audio_files],
#     key=os.path.getmtime
# )

# print(f"Processing: {latest_audio}")

# result = model.transcribe(latest_audio)

# transcript = result["text"]

# os.makedirs("transcripts", exist_ok=True)

# with open(
#     "transcripts/transcript.txt",
#     "w",
#     encoding="utf-8"
# ) as file:
#     file.write(transcript)

# print("Transcript saved successfully!")

from groq import Groq
import os

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

# Find latest uploaded MP3
audio_files = [
    f for f in os.listdir("audio")
    if f.endswith(".mp3")
]

if not audio_files:
    raise FileNotFoundError("No MP3 file found.")

latest_audio = max(
    [os.path.join("audio", f) for f in audio_files],
    key=os.path.getmtime
)

print(f"Processing: {latest_audio}")

with open(latest_audio, "rb") as file:

    transcription = client.audio.transcriptions.create(
        file=file,
        model="whisper-large-v3"
    )

transcript = transcription.text

os.makedirs("transcripts", exist_ok=True)

with open(
    "transcripts/transcript.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(transcript)

print("Transcript saved successfully!")