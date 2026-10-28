import subprocess
import time
import os

YOUTUBE_URL = "rtmp://://youtube.com"
STREAM_KEY = os.getenv("STREAM_KEY")
VIDEO_FILE = "video.mp4"

ffmpeg_command = [
    'ffmpeg', '-re', '-stream_loop', '-1', '-i', VIDEO_FILE,
    '-c:v', 'libx264', '-preset', 'veryfast', '-b:v', '2500k',
    '-maxrate', '2500k', '-bufsize', '5000k', '-pix_fmt', 'yuv420p',
    '-g', '50', '-c:a', 'aac', '-b:a', '128k', '-ar', '44100',
    '-f', 'flv', f"{YOUTUBE_URL}/{STREAM_KEY}"
]

print("Starting broadcast loop...")
process = subprocess.Popen(ffmpeg_command)
process.wait()
