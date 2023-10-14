import yt_dlp as youtube_dl

def descargar_playlist_en_mp3(url):
    opciones = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': 'descargas/%(title)s.%(ext)s',
        'noplaylist': False,
        'ignoreerrors': True,  # Ignorar errores y continuar con la siguiente descarga
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(opciones) as ydl:
        try:
            ydl.download([url])
        except youtube_dl.utils.DownloadError:
            print(f"Error al descargar: {url}. Saltando...")

url = input("Introduce la URL de la lista de reproducción de YouTube: ")
descargar_playlist_en_mp3(url)
