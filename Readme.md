# AI Voice Transcriber with Speaker Identification

## Project Overview

This project is a simple AI-powered voice transcription system that converts audio conversations into text and organizes them by speaker.

The idea behind this project was to explore how Large Language Models (LLMs) can be combined with speech recognition models to process conversations automatically.

The application uses:

* Groq Whisper Large V3 for Speech-to-Text
* Llama 3.3 70B for Speaker Identification
* Python for implementation

The final output converts an audio conversation into a structured format such as:

```text
Person 1:
Hello, how are you?

Person 2:
I am doing well. How about you?

Person 1:
I'm good too.

End of Conversation
```

---

## How It Works

### Step 1: Read Audio Files

The program scans the `audio` folder and reads audio files with extensions:

* .mp3
* .wav
* .m4a

### Step 2: Generate Transcript

The audio file is sent to Groq's Whisper Large V3 model.

The model converts speech into plain text.

Example:

```text
Hello, how are you?
I am fine.
What are your plans for today?
```

### Step 3: Identify Speakers

The generated transcript is then sent to Llama 3.3 70B with a custom prompt.

The model analyzes the conversation and restructures it into:

```text
Person 1:
...

Person 2:
...
```

### Step 4: Display Results

The organized conversation is displayed in the terminal and can also be saved to a text file.

---

## Project Structure

```text
voice_transcriber/
│
├── audio/
│   ├── conversation1.mp3
│   └── conversation2.mp3
│
├── transcripts/
│
├── main.py
├── requirements.txt
├── .env
└── README.md
```

---

## Technologies Used

* Python
* Groq API
* Whisper Large V3
* Llama 3.3 70B
* python-dotenv

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/voice-transcriber.git
cd voice-transcriber
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## Running the Project

Place your audio files inside the `audio` folder.

Run:

```bash
python main.py
```

---

## Sample Output

```text
Person 1:
Good morning.

Person 2:
Good morning. How can I help you?

Person 1:
I would like to book an appointment.

Person 2:
Sure, what date would you prefer?

End of Conversation
```

---

## Challenges Faced

One challenge was speaker identification.

The speech-to-text model generates only the transcript and does not explicitly identify speakers.

To solve this, I used Llama 3.3 to analyze the transcript and infer speaker turns based on conversational context.

---

## Learning Outcomes

Through this project, I learned:

* How Speech Recognition systems work
* How to use Groq APIs
* How LLMs can process conversational data
* Prompt Engineering techniques
* Building end-to-end AI applications

---

## Author

Vanshika Yadav

Computer Science Student | AI & Machine Learning Enthusiast
