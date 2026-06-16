import os 
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

# connecting to Groq API
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

audio_folder = "audio"
output_folder = "transcripts"

os.makedirs(output_folder, exist_ok=True)

for file_name in os.listdir(audio_folder):
     if file_name.endswith((".mp3", ".wav", ".m4a")):
        print(f"\nProcessing {file_name}...")

        file_path = os.path.join(audio_folder, file_name)

        # Transcribe audio
        with open(file_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                file=audio_file,
                model="whisper-large-v3"

            )
        transcript = transcription.text
        print("\nRaw Transcript:\n")
        print(transcript)


        # adding prompt for ai 

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

print("\nSpeaker Transcript:\n")
print(speaker_transcript)
