import json
import numpy as np
import soundfile as sf
from vosk import Model, KaldiRecognizer

MODEL_PATH = "models/vosk-model-small-en-us-0.15"
model = Model(MODEL_PATH)

def speech_to_text(audio_path: str) -> str:
    data, samplerate = sf.read(audio_path)

    # Convert stereo → mono
    if len(data.shape) > 1:
        data = data.mean(axis=1)

    # Convert float → int16
    if data.dtype != np.int16:
        data = (data * 32767).astype(np.int16)

    recognizer = KaldiRecognizer(model, samplerate)
    recognizer.AcceptWaveform(data.tobytes())

    result = json.loads(recognizer.Result())
    return result.get("text", "")
