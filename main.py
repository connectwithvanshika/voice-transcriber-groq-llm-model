import streamlit as st
import os
from transcriber import process_audio

st.set_page_config(
    page_title="Audio Conversation Analyzer",
    page_icon="🎙️",
    layout="wide"
)

st.title("Audio Conversation Analyzer")
st.write("Upload an audio file and get speaker-separated transcript.")

uploaded_file = st.file_uploader(
    "Choose an audio file",
    type=["mp3", "wav", "m4a"]
)

if uploaded_file:

    os.makedirs("audio", exist_ok=True)

    file_path = os.path.join("audio", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully!")

    if st.button("🚀 Process Audio"):

        with st.spinner("Transcribing and identifying speakers..."):

            transcript, speaker_transcript = process_audio(file_path)

        st.subheader("Raw Transcript")

        st.text_area(
            "Transcript",
            transcript,
            height=250
        )

        st.subheader("👥 Speaker-wise Conversation")

        st.text_area(
            "Conversation",
            speaker_transcript,
            height=400
        )

        st.download_button(
            "Download Speaker Transcript",
            speaker_transcript,
            file_name="conversation.txt",
            mime="text/plain"
        )

        st.success("Processing Complete!")