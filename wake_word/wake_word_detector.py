import pvporcupine
import pyaudio
import struct
from jarvis_voice_assistant.config import PV_PORCUPINE_API_KEY

class WakeWordDetector:
    def __init__(self):
        self.porcupine = pvporcupine.create(
            access_key=PV_PORCUPINE_API_KEY,
            keyword_paths=[pvporcupine.KEYWORD_PATHS["jarvis"]]
        )
        self.pa = pyaudio.PyAudio()
        self.audio_stream = self.pa.open(
            rate=self.porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=self.porcupine.frame_length
        )

    def wait_for_wake_word(self):
        print("Listening for wake word...")
        while True:
            pcm = self.audio_stream.read(self.porcupine.frame_length)
            pcm = struct.unpack_from("h" * self.porcupine.frame_length, pcm)
            result = self.porcupine.process(pcm)
            if result >= 0:
                print("Wake word detected!")
                return

    def __del__(self):
        if self.porcupine:
            self.porcupine.delete()
        if self.audio_stream:
            self.audio_stream.close()
        if self.pa:
            self.pa.terminate()
