from gtts import gTTS
import uuid

def text_to_speech(text: str) -> str:
    file_name = f"audio_{uuid.uuid4()}.mp3"
    tts = gTTS(text)
    tts.save(file_name)
    return file_name
