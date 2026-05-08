#biblioteca para conseguir baixar os vídeos
import yt_dlp 

def mp3(url):
    yt_opts = {
        "format": "bestaudio/best",
        "outtmpl": "caminho para onde os audios baixados vão /yt_mp3/audio/%(title)s.%(ext)s",
        "cookiefile": "caminho do arquvio cookies.txt /yt_mp3/cookies.txt",
        "postprocessors": [
            {
                "key" : "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "128",
            }
        ],
    }

    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        ydl.download([url])

print ("=== BAIXAR MP3 YOUTUBE ===")
link = input("Insira o link: ")
mp3(link)
