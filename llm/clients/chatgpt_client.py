import openai
from jarvis_voice_assistant.config import CHATGPT_API_KEY

class ChatGPTClient:
    def __init__(self):
        self.client = openai.OpenAI(api_key=CHATGPT_API_KEY)

    def get_response(self, prompt, model="gpt-4", tools=None):
        response = self.client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            tools=tools,
            stream=True,
        )
        for chunk in response:
            yield chunk.choices[0].delta.content
