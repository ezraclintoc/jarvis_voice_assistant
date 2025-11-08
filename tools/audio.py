import librosa

class Audio:
    def analyze_audio(self, audio_path):
        """
        Analyzes an audio file and returns its duration, sample rate, and channels.
        """
        try:
            y, sr = librosa.load(audio_path)
            duration = librosa.get_duration(y=y, sr=sr)
            channels = y.shape[0] if len(y.shape) > 1 else 1
            return f"Audio duration: {duration}s, sample rate: {sr}, channels: {channels}"
        except Exception as e:
            return f"An error occurred while analyzing the audio: {e}"
