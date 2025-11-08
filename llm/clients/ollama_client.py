import requests
import json
from jarvis_voice_assistant.config import OLLAMA_HOST, OLLAMA_MODEL

class OllamaClient:
    def get_response(self, prompt, model=OLLAMA_MODEL, tools=None):
        
        # Ollama doesn't have a direct tool calling feature like OpenAI.
        # We need to format the prompt to include the tool definitions.
        if tools:
            prompt_with_tools = f"{prompt}\n\nYou have the following tools available:\n{json.dumps(tools, indent=2)}\n\nPlease respond with a JSON object with the 'tool' and 'args' keys if you want to use a tool."
        else:
            prompt_with_tools = prompt

        response = requests.post(
            f"{OLLAMA_HOST}/api/generate",
            json={
                "model": model,
                "prompt": prompt_with_tools,
                "stream": True,
            }
        )
        response.raise_for_status()
        
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                json_line = json.loads(decoded_line)
                yield json_line["response"]
