# bot/downloader.py

import yt_dlp
import os
from io import BytesIO
import logging

async def search_and_download(query):
    """Search and download the first result from YouTube Music."""
    ydl_opts = {
    'format': 'bestaudio/best',
    'noplaylist': True,
    'quiet': True,
    'default_search': 'ytsearch1',
    'outtmpl': 'downloads/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '128',
    }],
    'retries': 3,
    'nocheckcertificate': True,
    'geo_bypass': True,
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'cookiefile': 'bot/utils/youtube_cookies.txt',
}


    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch1:{query}", download=True)
            if 'entries' in info:
                video = info['entries'][0]
                title = video['title']
                artist = video.get('uploader', 'Unknown Artist')
                thumbnail_url = video.get('thumbnail', '')
                # Prepare file to send
                audio_file_path = ydl.prepare_filename(video).replace(".webm", ".ogg").replace(".m4a", ".ogg")
                with open(audio_file_path, 'rb') as audio_file:
                    audio_data = BytesIO(audio_file.read())
                os.remove(audio_file_path)  # Clean up the file
                return {
                    'file': audio_data,
                    'title': title,
                    'artist': artist,
                    'thumbnail': thumbnail_url
                }
    except Exception as e:
        logging.error(f"Error while downloading: {e}")
    return None

