# Jarvis Voice Assistant

A voice assistant that uses pvporcupine for wake word detection and can be configured to use Ollama, Gemini, Claude, or ChatGPT as the LLM.

## Features

- Wake word detection using "Hey Jarvis".
- Speech-to-text (STT) using various engines.
- Text-to-speech (TTS) using various engines.
- Language model integration with Ollama, Gemini, Claude, and ChatGPT.
- Built-in tools:
  - Search
  - Screenshots
  - Commands
  - Media control
- Ability to add custom MCP servers.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/jarvis-voice-assistant.git
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure the assistant by editing the `config.py` file.
4. Run the assistant:
   ```bash
   python main.py
   ```

## Usage

- Say "Hey Jarvis" to activate the assistant.
- Speak your command or question.
- The assistant will respond and perform the requested action.

## Custom Voice

To use a custom voice, you need to:

1.  Install the `voice-cloning` library:
    ```bash
    pip install voice-cloning
    ```
2.  Obtain a `.wav` file of the desired voice.
3.  Update the `JARVIS_VOICE_FILE` variable in `config.py` to the path of the `.wav` file.
4.  Change the `TTS_ENGINE` variable in `config.py` to `"jarvis"`.
