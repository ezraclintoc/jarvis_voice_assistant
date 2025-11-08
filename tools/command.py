import os

class Command:
    def execute_command(self, command):
        """
        Executes a shell command.
        """
        try:
            output = os.popen(command).read()
            return output
        except Exception as e:
            return str(e)
