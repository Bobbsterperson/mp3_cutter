from pytube import YouTube


def download_audio(url):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(filename='audio.mp3')
        print("Here ya go shuga!")
    except Exception as e:
        print("No such thang...", e)


if __name__ == "__main__":
    video_url = input("Whatcha whanna download?!")
    download_audio(video_url)
