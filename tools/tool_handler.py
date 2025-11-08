from jarvis_voice_assistant.tools.search import Search
from jarvis_voice_assistant.tools.screenshot import Screenshot
from jarvis_voice_assistant.tools.command import Command
from jarvis_voice_assistant.tools.media import Media

from jarvis_voice_assistant.tools.vision import Vision
from jarvis_voice_assistant.tools.audio import Audio

class ToolHandler:
    def __init__(self):
        self.tools = {
            "search": Search().search,
            "screenshot": Screenshot().take_screenshot,
            "command": Command().execute_command,
            "media": Media(),
            "analyze_video": Vision().analyze_video,
            "analyze_picture": Vision().analyze_picture,
            "analyze_audio": Audio().analyze_audio,
        }

    def get_tool_definitions(self):
        return [
            {
                "name": "search",
                "description": "Searches the web for the given query and returns the top 3 results.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "The search query.",
                        },
                    },
                    "required": ["query"],
                },
            },
            {
                "name": "screenshot",
                "description": "Takes a screenshot and saves it to the desktop.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                },
            },
            {
                "name": "command",
                "description": "Executes a shell command.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "command": {
                            "type": "string",
                            "description": "The command to execute.",
                        },
                    },
                    "required": ["command"],
                },
            },
            {
                "name": "analyze_video",
                "description": "Analyzes a video file and returns its duration, resolution, and fps.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "video_path": {
                            "type": "string",
                            "description": "The path to the video file.",
                        },
                    },
                    "required": ["video_path"],
                },
            },
            {
                "name": "analyze_picture",
                "description": "Analyzes an image file and returns its format, size, and mode.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "image_path": {
                            "type": "string",
                            "description": "The path to the image file.",
                        },
                    },
                    "required": ["image_path"],
                },
            },
            {
                "name": "analyze_audio",
                "description": "Analyzes an audio file and returns its duration, sample rate, and channels.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audio_path": {
                            "type": "string",
                            "description": "The path to the audio file.",
                        },
                    },
                    "required": ["audio_path"],
                },
            },
        ]

    def get_tools(self):
        return self.tools

    def use_tool(self, tool_name, *args, **kwargs):
        if tool_name in self.tools:
            return self.tools[tool_name](*args, **kwargs)
        else:
            return f"Tool '{tool_name}' not found."
