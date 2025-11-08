from gtts import gTTS
import os
from playsound3 import playsound
from TTS.api import TTS
from jarvis_voice_assistant.config import TTS_ENGINE, JARVIS_VOICE_FILE

class TextToSpeech:
    def __init__(self):
        if TTS_ENGINE == "jarvis":
            if os.path.exists(JARVIS_VOICE_FILE):
                self.tts = TTS(model_name="tts_models/en/ljspeech/vits", progress_bar=False, gpu=False)
                self.speaker_wav = JARVIS_VOICE_FILE
            else:
                raise FileNotFoundError(f"Jarvis voice file not found at: {JARVIS_VOICE_FILE}")

    def speak(self, text):
        print(f"Speaking: {text}")
        if TTS_ENGINE == "google":
            tts = gTTS(text=text, lang='en')
            filename = "response.mp3"
            tts.save(filename)
            playsound(filename)
            os.remove(filename)
        elif TTS_ENGINE == "jarvis":
            self.tts.tts_to_file(text=text, speaker_wav=self.speaker_wav, file_path="response.wav")
            playsound("response.wav")
            os.remove("response.wav")
