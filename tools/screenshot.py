import os

class Screenshot:
    def take_screenshot(self):
        """
        Takes a screenshot and saves it to the desktop.
        """
        if not os.environ.get('DISPLAY'):
            return "Screenshot tool is not available in this environment."
        try:
            import pyautogui
            screenshot = pyautogui.screenshot()
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            screenshot_path = os.path.join(desktop_path, "screenshot.png")
            screenshot.save(screenshot_path)
            return screenshot_path
        except (ImportError, OSError) as e:
            print(f"Warning: pyautogui could not be imported. Screenshot tool will not be available. Error: {e}")
            return "Screenshot tool is not available."
