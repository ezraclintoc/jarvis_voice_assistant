import pyaudio
import json
import whisper
import numpy as np
from vosk import Model, KaldiRecognizer
from jarvis_voice_assistant.config import STT_ENGINE

class SpeechToText:
    def __init__(self):
        if STT_ENGINE == "vosk":
            self.model = Model(model_name="vosk-model-small-en-us-0.15")
            self.recognizer = KaldiRecognizer(self.model, 16000)
        elif STT_ENGINE == "whisper":
            self.model = whisper.load_model("base")
        else:
            raise ValueError(f"Unsupported STT engine: {STT_ENGINE}")

        self.pa = pyaudio.PyAudio()
        self.audio_stream = self.pa.open(
            rate=16000,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=8192
        )

    def listen(self):
        print("Listening for command...")
        if STT_ENGINE == "vosk":
            while True:
                data = self.audio_stream.read(4096)
                if self.recognizer.AcceptWaveform(data):
                    result = json.loads(self.recognizer.Result())
                    text = result.get("text", "")
                    if text:
                        print(f"Recognized: {text}")
                        return text
        elif STT_ENGINE == "whisper":
            audio_data = self.audio_stream.read(4096 * 8) # Read more data for whisper
            audio_np = np.frombuffer(audio_data, dtype=np.int16).astype(np.float32) / 32768.0
            result = self.model.transcribe(audio_np)
            text = result["text"]
            print(f"Recognized: {text}")
            return text


    def __del__(self):
        if hasattr(self, 'audio_stream') and self.audio_stream:
            self.audio_stream.close()
        if hasattr(self, 'pa') and self.pa:
            self.pa.terminate()
