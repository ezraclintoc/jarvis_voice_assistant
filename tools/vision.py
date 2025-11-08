try:
    from moviepy.editor import VideoFileClip
except ImportError:
    VideoFileClip = None
    print("Warning: moviepy is not installed correctly. Video analysis will not be available.")
from PIL import Image
import subprocess

def is_ffmpeg_installed():
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

class Vision:
    def __init__(self):
        if not is_ffmpeg_installed():
            print("Warning: ffmpeg is not installed. Video analysis will not be available.")

    def analyze_video(self, video_path):
        """
        Analyzes a video file and returns its duration, resolution, and fps.
        """
        if not is_ffmpeg_installed():
            return "ffmpeg is not installed. Video analysis is not available."
        if not VideoFileClip:
            return "moviepy is not installed correctly. Video analysis is not available."
        try:
            with VideoFileClip(video_path) as video:
                duration = video.duration
                width, height = video.size
                fps = video.fps
                return f"Video duration: {duration}s, resolution: {width}x{height}, fps: {fps}"
        except Exception as e:
            return f"An error occurred while analyzing the video: {e}"

    def analyze_picture(self, image_path):
        """
        Analyzes an image file and returns its format, size, and mode.
        """
        try:
            with Image.open(image_path) as img:
                format = img.format
                width, height = img.size
                mode = img.mode
                return f"Image format: {format}, size: {width}x{height}, mode: {mode}"
        except Exception as e:
            return f"An error occurred while analyzing the image: {e}"
