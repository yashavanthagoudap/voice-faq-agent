import os
import tempfile
import streamlit as st

from voice_agent import VoiceAgent
from stt import speech_to_text
from tts import text_to_speech

st.set_page_config(page_title="AI Voice FAQ Agent")

# agent = VoiceAgent("data/NTTA VEHICLE BAN FAQs.FINAL (1) (1).pdf")
agent = VoiceAgent("data")


st.title("📞 AI Voice Customer Support Agent")
st.write("🎤 Click the mic and speak your question")

# 🎙️ MIC INPUT (KEY CHANGE)
audio_bytes = st.audio_input("Speak now")

if audio_bytes is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_bytes.getvalue())  # ✅ FIX HERE
        audio_path = tmp.name

    try:
        with st.spinner("Listening..."):
            user_text = speech_to_text(audio_path)

        st.write("**You said:**", user_text)

        response = agent.handle_query(user_text)

        st.write("**Agent:**", response)

        audio_response = text_to_speech(response)
        st.audio(audio_response)

    except Exception as e:
        st.error(str(e))


if st.button("End Call"):
    st.subheader("📄 Call Transcript")
    st.text(agent.transcript.full_text())
