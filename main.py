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
            transcription = client.audio.transcripts.create(
                file=audio_file,
                model="whisper-large-v3"

            )
        transcript = transcription.text
        print("\nRaw Transcript:\n")
        print(transcript)

