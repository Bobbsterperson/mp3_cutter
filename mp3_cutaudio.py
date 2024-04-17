from pydub import AudioSegment
import os
from pytube import YouTube


def download_audio(url):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(filename='audio.mp3')
        print("Here ya go shuga!")
    except Exception as e:
        print("No such thang...", e)


def cut_intro(audio_file, start_time):
   
    audio = AudioSegment.from_file(audio_file)
    
    start_m = int(start_time.split(':')[0]) * 60 * 1000
    start_s = int(start_time.split(':')[1]) * 1000
    start_time_ms = start_m + start_s
    
    intro_removed = audio[start_time_ms:]
    filename_without_extension = os.path.splitext(audio_file)[0]
    intro_removed.export(f"{filename_without_extension}_intro_removed.mp3", format="mp3")
    print("Intro removed successfully!")


def cut_middle(audio_file, start_time, end_time):
    
    audio = AudioSegment.from_file(audio_file)

    start_m = int(start_time.split(':')[0]) * 60 * 1000
    start_s = int(start_time.split(':')[1]) * 1000
    start_time_ms = start_m + start_s

    end_m = int(end_time.split(':')[0]) * 60 * 1000
    end_s = int(end_time.split(':')[1]) * 1000
    end_time_ms = end_m + end_s

    middle_removed = audio[:start_time_ms] + audio[end_time_ms:]
    filename_without_extension = os.path.splitext(audio_file)[0]
    middle_removed.export(f"{filename_without_extension}_middle_removed.mp3", format="mp3")
    print("Middle part removed successfully!")


def cut_end(audio_file, end_time):

    audio = AudioSegment.from_file(audio_file)

    end_m = int(end_time.split(':')[0]) * 60 * 1000
    end_s = int(end_time.split(':')[1]) * 1000
    end_time_ms = end_m + end_s

    end_removed = audio[:end_time_ms]
    filename_without_extension = os.path.splitext(audio_file)[0]
    end_removed.export(f"{filename_without_extension}_end_removed.mp3", format="mp3")
    print("End removed successfully!")


if __name__ == "__main__":
    video_url = input("Whatcha whanna download?!:  ")
    download_audio(video_url)
    audio_file = input("Enter the audio file name (with extension): ")
    cut_what = input("whacha whanna cut nigga? (intro, middle, end)")

    if cut_what == "intro":
        start_time = input("Enter the start time to cut from (mm:ss): ")
        cut_intro(audio_file, start_time)

    elif cut_what == "middle":
        start_time = input("Enter the start time to cut from (mm:ss): ")
        end_time = input("Enter the end time to cut to (mm:ss): ")
        cut_middle(audio_file, start_time, end_time)

    elif cut_what == "end":
        end_time = input("Enter the end time to cut to (mm:ss): ")
        cut_end(audio_file, end_time)
    else:
        print("shits invalid, Please choose 'intro', 'middle', or 'end'. mothafocka!")