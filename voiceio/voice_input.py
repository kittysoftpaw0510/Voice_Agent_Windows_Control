import whisper
import sounddevice as sd
import numpy as np

model = whisper.load_model("base")
SAMPLE_RATE = 16000
DURATION = 5  # seconds

def listen_for_command():
    print("Please speak your command...")
    audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='float32')
    sd.wait()
    audio = np.squeeze(audio)
    result = model.transcribe(audio, fp16=False, language='en')
    text = result.get('text', '').strip()
    print(f"[Heard]: {text}")
    return text 