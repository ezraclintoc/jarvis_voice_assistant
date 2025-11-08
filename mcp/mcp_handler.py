import subprocess

class MCPHandler:
    def __init__(self):
        self.process = None

    def start_server(self):
        """
        Starts the MCP server using 'docker mcp gateway run'.
        """
        try:
            self.process = subprocess.Popen(["docker", "mcp", "gateway", "run"])
            print("MCP server started.")
            return "MCP server started."
        except Exception as e:
            print(f"Failed to start MCP server: {e}")
            return f"Failed to start MCP server: {e}"

    def stop_server(self):
        """
        Stops the MCP server.
        """
        if self.process:
            self.process.terminate()
            print("MCP server stopped.")
            return "MCP server stopped."
        return "MCP server is not running."

    def get_tools(self):
        """
        Gets the tools from all registered MCP servers.
        """
        # This is a placeholder. In a real implementation, this would
        # make requests to the MCP servers to get their tool definitions.
        return []
