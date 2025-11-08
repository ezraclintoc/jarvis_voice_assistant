import google.generativeai as genai
from jarvis_voice_assistant.config import GEMINI_API_KEY

class GeminiClient:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')

    def get_response(self, prompt, model=None, tools=None):
        if model:
            # This is a conceptual change. The actual implementation will depend on the Gemini API.
            # I will assume that the model can be changed like this.
            self.model = genai.GenerativeModel(model)
        response = self.model.generate_content(prompt, tools=tools, stream=True)
        for chunk in response:
            yield chunk.text
