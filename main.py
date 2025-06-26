import os
import requests
import yt_dlp

# Get env vars
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

# Sample short video from YouTube
VIDEO_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
OUTPUT_FILENAME = "short_video.mp4"

def download_video():
    ydl_opts = {
        'format': 'best[ext=mp4][height<=360]',
        'outtmpl': OUTPUT_FILENAME,
        'duration': 40  # Limit to short video
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([VIDEO_URL])

def send_to_telegram():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo"

    with open(OUTPUT_FILENAME, 'rb') as video_file:
        files = {'video': video_file}
        data = {
            'chat_id': CHANNEL_ID,
            'caption': "🎬 Auto uploaded short video test",
            'supports_streaming': True
        }

        response = requests.post(url, data=data, files=files)
        print("✅ Telegram response:", response.status_code)
        print(response.json())

if __name__ == "__main__":
    print("⏬ Downloading video...")
    download_video()
    print("🚀 Sending to Telegram...")
    send_to_telegram()
