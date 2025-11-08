import anthropic
from jarvis_voice_assistant.config import CLAUDE_API_KEY

class ClaudeClient:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)

    def get_response(self, prompt, model="claude-3-opus-20240229", tools=None):
        with self.client.messages.stream(
            model=model,
            max_tokens=1024,
            messages=[
                {"role": "user", "content": prompt}
            ],
            tools=tools,
        ) as stream:
            for text in stream.text_stream:
                yield text
