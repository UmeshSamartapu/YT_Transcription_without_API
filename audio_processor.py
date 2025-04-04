import yt_dlp
import os

def download_audio(url):
    os.makedirs("outputs/audio", exist_ok=True)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'outputs/audio/%(id)s.%(ext)s',
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ignoreerrors': True,
        'noplaylist': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            if not info:
                raise ValueError("Invalid URL or video unavailable")
            if 'entries' in info:
                raise ValueError("Playlists are not supported")
            if info.get('is_live'):
                raise ValueError("Live streams not supported")
            if info.get('requires_payment'):
                raise ValueError("Paid content cannot be downloaded")
            
            ydl.download([url])
            return f"outputs/audio/{info['id']}.mp3"
            
    except yt_dlp.utils.DownloadError as e:
        raise RuntimeError(f"Download failed: {str(e)}")
