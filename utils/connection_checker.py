import pyaudio
import pvporcupine
from jarvis_voice_assistant.config import (
    PV_PORCUPINE_API_KEY,
    LLM_PROVIDER,
    GEMINI_API_KEY,
    CLAUDE_API_KEY,
    CHATGPT_API_KEY,
    TTS_ENGINE,
    JARVIS_VOICE_FILE,
)

def check_microphone():
    """Checks if a microphone is available."""
    pa = pyaudio.PyAudio()
    try:
        if pa.get_default_input_device_info():
            print("Microphone found.")
            return True
    except IOError:
        print("No microphone found.")
        return False
    finally:
        pa.terminate()

def check_wake_word():
    """Checks if the wake word model is available."""
    try:
        pvporcupine.create(access_key=PV_PORCUPINE_API_KEY, keyword_paths=[pvporcupine.KEYWORD_PATHS["jarvis"]])
        print("Wake word engine connected.")
        return True
    except Exception as e:
        print(f"Wake word engine connection failed: {e}")
        return False

def check_ai_provider():
    """Checks if the selected AI provider is configured."""
    if LLM_PROVIDER == "gemini" and not GEMINI_API_KEY:
        print("Gemini API key is not configured.")
        return False
    elif LLM_PROVIDER == "claude" and not CLAUDE_API_KEY:
        print("Claude API key is not configured.")
        return False
    elif LLM_PROVIDER == "chatgpt" and not CHATGPT_API_KEY:
        print("ChatGPT API key is not configured.")
        return False
    print(f"AI provider '{LLM_PROVIDER}' is configured.")
    return True

def check_tool_server():
    """Placeholder for checking the tool server connection."""
    print("Tool server connection check not implemented yet.")
    return True

def check_tts():
    """Checks if the selected TTS engine is configured."""
    if TTS_ENGINE == "jarvis" and not JARVIS_VOICE_FILE:
        print("Jarvis voice file is not configured.")
        return False
    print(f"TTS engine '{TTS_ENGINE}' is configured.")
    return True

def check_all_connections():
    """Checks all connections."""
    print("Checking all connections...")
    mic_ok = check_microphone()
    wake_word_ok = check_wake_word()
    ai_provider_ok = check_ai_provider()
    tool_server_ok = check_tool_server()
    tts_ok = check_tts()
    print("-" * 20)
    if all([mic_ok, wake_word_ok, ai_provider_ok, tool_server_ok, tts_ok]):
        print("All connections are working.")
    else:
        print("Some connections are not working.")
