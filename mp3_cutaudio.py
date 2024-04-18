from pydub import AudioSegment
import os
from pytube import YouTube
import argparse



def download_audio(url):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(filename='audio.mp3')
        print("Here ya go shuga!")
    except Exception as e:
        print("No such thang...", e)

def parse_arguments():
    parser = argparse.ArgumentParser(description="export audio file with its intro, middle, end cut out or to download")
    parser.add_argument("-d", action="store_true", help="download")
    parser.add_argument("-i", action="store_true", help="cut out the intro")
    parser.add_argument("-m", action="store_true", help="cut out the middle")
    parser.add_argument("-e", action="store_true", help="cut out the end")
    args = parser.parse_args()

    if args.i:
        return '-i'
    elif args.m:
        return '-m'
    elif args.e:
        return '-e'
    elif args.d:
        return '-d'
    else:
        parser.error("Please specify either -d, -i, -m, or -e")


def cut_intro(audio_file, start_time):
   
    audio = AudioSegment.from_file(audio_file)
    
    start_m = int(start_time.split(':')[0]) * 60 * 1000
    start_s = int(start_time.split(':')[1]) * 1000
    start_time_ms = start_m + start_s
    
    intro_removed = audio[start_time_ms:]
    filename_without_extension = os.path.splitext(audio_file)[0]
    with open(f"{filename_without_extension}_intro_removed.mp3", "wb") as f:
        intro_removed.export(f, format="mp3")
    
    

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
    with open(f"{filename_without_extension}_middle_removed.mp3", "wb") as f:
        middle_removed.export(f, format="mp3")
    
    

def cut_end(audio_file, end_time):

    audio = AudioSegment.from_file(audio_file)

    end_m = int(end_time.split(':')[0]) * 60 * 1000
    end_s = int(end_time.split(':')[1]) * 1000
    end_time_ms = end_m + end_s

    end_removed = audio[:end_time_ms]
    filename_without_extension = os.path.splitext(audio_file)[0]
    with open(f"{filename_without_extension}_end_removed.mp3", "wb") as f:
        end_removed.export(f, format="mp3")
    
    

if __name__ == "__main__":
    
    cut_what = parse_arguments()
    print(cut_what)
    if cut_what == "-i":
        audio_file = input("Enter the audio file name (with extension): ")
        start_time = input("Enter the start time to cut from (mm:ss): ")
        cut_intro(audio_file, start_time)

    elif cut_what == "-m":
        audio_file = input("Enter the audio file name (with extension): ")
        start_time = input("Enter the start time to cut from (mm:ss): ")
        end_time = input("Enter the end time to cut to (mm:ss): ")
        cut_middle(audio_file, start_time, end_time)

    elif cut_what == "-e":
        audio_file = input("Enter the audio file name (with extension): ")
        end_time = input("Enter the end time to cut to (mm:ss): ")
        cut_end(audio_file, end_time)

    elif cut_what == "-d":
        video_url = input("Whatcha whanna download?!:  ")
        download_audio(video_url)
    else:
        print("shits invalid, Please choose 'intro', 'middle', or 'end'. mothafocka!")