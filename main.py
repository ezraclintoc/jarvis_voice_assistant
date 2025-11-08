import os
import sys
import argparse
import json

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from jarvis_voice_assistant.wake_word.wake_word_detector import WakeWordDetector
from jarvis_voice_assistant.stt.speech_to_text import SpeechToText
from jarvis_voice_assistant.tts.text_to_speech import TextToSpeech
from jarvis_voice_assistant.llm.llm_handler import LLMHandler
from jarvis_voice_assistant.tools.tool_handler import ToolHandler
from jarvis_voice_assistant.mcp.mcp_handler import MCPHandler
from jarvis_voice_assistant.utils.connection_checker import check_all_connections

from jarvis_voice_assistant.utils.animation import ThinkingAnimation

class Jarvis:
    def __init__(self, text_mode=False):
        self.text_mode = text_mode
        if not self.text_mode:
            self.wake_word_detector = WakeWordDetector()
            self.stt = SpeechToText()
        self.tts = TextToSpeech()
        self.tool_handler = ToolHandler()
        self.llm = LLMHandler(self.tool_handler)
        self.mcp_handler = MCPHandler()
        self.animation = ThinkingAnimation()

    def run(self):
        if self.text_mode:
            prompt = input("Enter your command: ")
        else:
            self.wake_word_detector.wait_for_wake_word()
            prompt = self.stt.listen()

        if prompt:
            self.animation.start()
            
            response = self.handle_prompt(prompt)

            while response["type"] == "tool_result":
                print(f"\nTool result: {response['content']}")
                prompt = f"The tool returned the following result: {response['content']}. What should I do next?"
                response = self.handle_prompt(prompt)

            self.animation.stop()
            
            if response["type"] == "speak":
                self.tts.speak(response["content"])


    def handle_prompt(self, prompt):
        response_generator = self.llm.get_response(prompt)
        
        full_response = ""
        for chunk in response_generator:
            full_response += chunk
            print(chunk, end="", flush=True)

        try:
            response_json = json.loads(full_response)
            if "tool" in response_json:
                tool_name = response_json["tool"]
                tool_args = response_json.get("args", [])
                tool_kwargs = response_json.get("kwargs", {})
                tool_result = self.tool_handler.use_tool(tool_name, *tool_args, **tool_kwargs)
                return {"type": "tool_result", "content": tool_result}
        except json.JSONDecodeError:
            pass
        return {"type": "speak", "content": full_response}

def main():
    parser = argparse.ArgumentParser(description="Jarvis Voice Assistant")
    parser.add_argument("--check-connections", action="store_true", help="Check all connections and exit")
    parser.add_argument("--text", action="store_true", help="Run in text mode")
    args = parser.parse_args()

    if args.check_connections:
        check_all_connections()
        sys.exit(0)

    jarvis = Jarvis(text_mode=args.text)
    while True:
        jarvis.run()

if __name__ == "__main__":
    main()
