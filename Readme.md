# Audio Conversation Analyzer

## Overview

Audio Conversation Analyzer is a Streamlit-based application that transcribes audio files and automatically organizes conversations by speaker turns using Groq's Whisper and Llama models.

Users can upload an audio file, generate a transcript, identify different speakers in the conversation, and download the formatted output.

---

## Features

* Upload audio files in MP3, WAV, or M4A format
* Speech-to-text transcription using Whisper Large V3
* Speaker turn identification using Llama 3.3 70B
* Structured conversation formatting
* Download generated conversation transcripts
* Simple and interactive Streamlit interface

---

## Tech Stack

* Python
* Streamlit
* Groq API
* Whisper Large V3
* Llama 3.3 70B Versatile
* Python Dotenv

---

## Project Structure

```bash
voice_transcriber/
│
├── main.py
├── transcriber.py
├── requirements.txt
├── .env
├── audio/
├── transcripts/
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/voice-transcriber.git
cd voice-transcriber
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Running the Application

Start the Streamlit app:

```bash
streamlit run main.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## How It Works

1. User uploads an audio file.
2. Whisper Large V3 transcribes the audio into text.
3. The transcript is sent to Llama 3.3 70B.
4. The model identifies speaker turns and restructures the conversation.
5. The formatted conversation is displayed and can be downloaded.

---

## Example Output

```text
Person 1:
Hey, good morning. What can I get for you today?

Person 2:
Morning. Can I get a large latte with oat milk, please?

Person 1:
Sure thing. Would you like any syrup in that?

Person 2:
Yeah, one pump of vanilla would be great.

End of Conversation
```

---

## Supported Audio Formats

* MP3
* WAV
* M4A

---

## Audio Dataset Source

https://www.kaggle.com/datasets/velvetcrystal/audio-dataset

---

## Future Improvements

* Multi-speaker diarization
* PDF export support
* Conversation summarization
* Speaker naming and labeling
* Batch audio processing
* Timestamp support

---

## License

This project is intended for educational and learning purposes.
