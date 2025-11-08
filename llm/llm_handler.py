from jarvis_voice_assistant.config import LLM_PROVIDER, VISION_MODEL
from jarvis_voice_assistant.llm.clients.ollama_client import OllamaClient
from jarvis_voice_assistant.llm.clients.gemini_client import GeminiClient
from jarvis_voice_assistant.llm.clients.claude_client import ClaudeClient
from jarvis_voice_assistant.llm.clients.chatgpt_client import ChatGPTClient
from jarvis_voice_assistant.tools.tool_handler import ToolHandler

class LLMHandler:
    def __init__(self, tool_handler: ToolHandler):
        self.tool_handler = tool_handler
        if LLM_PROVIDER == "ollama":
            self.client = OllamaClient()
        elif LLM_PROVIDER == "gemini":
            self.client = GeminiClient()
        elif LLM_PROVIDER == "claude":
            self.client = ClaudeClient()
        elif LLM_PROVIDER == "chatgpt":
            self.client = ChatGPTClient()
        else:
            raise ValueError(f"Unsupported LLM provider: {LLM_PROVIDER}")

    def get_response(self, prompt):
        tool_definitions = self.tool_handler.get_tool_definitions()
        
        # Check if the prompt is related to vision and use the vision model
        if "analyze" in prompt and ("video" in prompt or "picture" in prompt or "audio" in prompt):
            # This is a conceptual change. The actual implementation will depend on the LLM provider.
            # I will assume a generic way of passing tool definitions to the LLM.
            return self.client.get_response(prompt, model=VISION_MODEL, tools=tool_definitions)
        else:
            return self.client.get_response(prompt, tools=tool_definitions)

