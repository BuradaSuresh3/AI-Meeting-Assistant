import streamlit as st
import ollama
import os
import time
from transcriber import transcribe_audio

st.set_page_config(
    page_title="AI Meeting Assistant",
    page_icon="🎙️",
    layout="wide"
)

st.title("🎙️ AI Meeting Assistant")
st.write("Upload a meeting recording and generate an AI-powered summary.")

uploaded_file = st.file_uploader(
    "Upload Meeting Audio",
    type=["mp3", "wav", "mp4", "m4a"]
)

if uploaded_file is not None:

    # Create unique filename
    file_name = f"{int(time.time())}_{uploaded_file.name}"
    file_path = os.path.abspath(file_name)

    # Save uploaded file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Audio uploaded successfully!")

    if st.button("Generate Summary"):

        try:

            # Step 1: Transcribe Audio
            with st.spinner("🎧 Transcribing audio..."):
                transcript = transcribe_audio(file_path)

            st.subheader("📝 Transcript")

            st.text_area(
                "Transcript",
                transcript,
                height=300
            )

            # Limit transcript size for faster local LLM processing
            short_transcript = transcript[:1500]

            # Step 2: Generate Summary
            with st.spinner("🤖 Generating summary..."):

                response = ollama.chat(
                    model="llama3",
                    messages=[
                        {
                            "role": "user",
                            "content": f"""
You are an AI Meeting Assistant.

Read the meeting transcript and provide:

1. Executive Summary
2. Key Decisions
3. Action Items (with owner names)
4. Challenges Discussed
5. Next Steps

Transcript:
{short_transcript}
"""
                        }
                    ]
                )

            summary = response["message"]["content"]

            st.subheader("📋 Meeting Summary")
            st.write(summary)

            # Download Button
            st.download_button(
                label="📥 Download Summary",
                data=summary,
                file_name="meeting_summary.txt",
                mime="text/plain"
            )

            # Delete temporary audio file
            if os.path.exists(file_path):
                os.remove(file_path)

        except Exception as e:
            st.error(f"Error: {str(e)}")