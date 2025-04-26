import yt_dlp
import ffmpeg
from io import BytesIO

async def search_and_download(query):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{query}", download=False)
        if 'entries' in info:
            video = info['entries'][0]
            audio_file = ydl.prepare_filename(video)
            ffmpeg.input(audio_file).output('output.ogg').run()
            with open('output.ogg', 'rb') as f:
                audio_data = BytesIO(f.read())
            return {
                'file': audio_data,
                'title': video['title'],
                'artist': video['uploader']
            }
    return None
