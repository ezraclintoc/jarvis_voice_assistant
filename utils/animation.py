import threading
import time
import sys

class ThinkingAnimation:
    def __init__(self):
        self.stop_event = threading.Event()
        self.animation_thread = None

    def start(self):
        self.stop_event.clear()
        self.animation_thread = threading.Thread(target=self._animate)
        self.animation_thread.start()

    def stop(self):
        self.stop_event.set()
        if self.animation_thread:
            self.animation_thread.join()
        self.animation_thread = None

    def _animate(self):
        chars = "|/-\\"
        while not self.stop_event.is_set():
            for char in chars:
                sys.stdout.write(f"\rThinking... {char}")
                sys.stdout.flush()
                time.sleep(0.1)
        sys.stdout.write("\r" + " " * 20 + "\r") # Clear the line
        sys.stdout.flush()
