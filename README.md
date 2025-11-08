# Jarvis Voice Assistant

A voice assistant that uses pvporcupine for wake word detection and can be configured to use Ollama, Gemini, Claude, or ChatGPT as the LLM.

## Features

-   Wake word detection using "Hey Jarvis".
-   Speech-to-text (STT) using various engines (Vosk, Whisper).
-   Text-to-speech (TTS) using various engines (Google, ElevenLabs, and custom voice cloning).
-   Language model integration with Ollama, Gemini, Claude, and ChatGPT.
-   Built-in tools:
    -   Search the web
    -   Take a screenshot
    -   Execute shell commands
    -   Control media playback (Spotify on Linux)
    -   Analyze video, audio, and image files
-   Ability to add custom MCP servers.
-   Text-based input mode.
-   Connection checker to diagnose issues.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/ezraclintoc/jarvis_voice_assistant.git
    ```
2.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Create a `config.py` file by copying the `config.py.example` file:
    ```bash
    cp config.py.example config.py
    ```
4.  Configure the assistant by editing the `config.py` file:
    *   Get a free `pvporcupine` access key from the [Picovoice Console](https://console.picovoice.ai/) and add it to the `PV_PORCUPINE_API_KEY` variable.
    *   Add your API keys for the desired LLM, STT, and TTS services.

## Usage

*   **Voice Mode:**
    ```bash
    python -m jarvis_voice_assistant.main
    ```
*   **Text Mode:**
    ```bash
    python -m jarvis_voice_assistant.main --text
    ```
*   **Check Connections:**
    ```bash
    python -m jarvis_voice_assistant.main --check-connections
    ```

-   Say "Hey Jarvis" to activate the assistant.
-   Speak your command or question.
-   The assistant will respond and perform the requested action.

## Custom Voice

To use a custom voice, you need to:

1.  Obtain a `.wav` file of the desired voice.
2.  Update the `JARVIS_VOICE_FILE` variable in `config.py` to the path of the `.wav` file.
3.  Change the `TTS_ENGINE` variable in `config.py` to `"jarvis"`.
