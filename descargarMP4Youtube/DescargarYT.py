import yt_dlp as youtube_dl

def descargar_video(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',  # Descarga el formato con mejor calidad disponible
        'outtmpl': '%(title)s.%(ext)s',  # Define el nombre del archivo de salida
        'verbose': True, # Habilitar detalles en la consola
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# URL del video de YouTube
url = "https://www.youtube.com/watch?v=LocWjiSWBLo&ab_channel=Flushed"
descargar_video(url)

# Ejecutar con py .\archivo.py
# Que no se te olvide cambiar la url, sino te descarga el mismo vídeo xd
# La calidad es 360p pero sino es un lio pq tengo que utilizar ffmpeg
