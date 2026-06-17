import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def process_audio(file_path):

    # Transcribe audio
    with open(file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            file=audio_file,
            model="whisper-large-v3"
        )

    transcript = transcription.text

    # Speaker Identification Prompt
    prompt = f"""
This transcript contains a conversation between two people.

Your task:
1. Identify speaker turns.
2. Rewrite the conversation in this format:

Person 1:
text

Person 2:
text

Rules:
- Keep all original content.
- Do not summarize.
- Do not remove any information.
- Only organize the conversation by speakers.
- Once conversation is ended, write "End of Conversation" at the end.

Transcript:

{transcript}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert conversation analyzer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    speaker_transcript = response.choices[0].message.content

    return transcript, speaker_transcript
