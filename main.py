# YT_DOWNLOADER V 1.0
# github.com/ridam9999/YT_DOWNLOADER

from pytube import YouTube, Playlist
import os

run = True
internal_storage_music = '/home/jarvis/Music'
external_storage_music = '/media/jarvis/UNDERLOAD/Music'
internal_storage_video = '/home/jarvis/Videos'
external_storage_video = '/media/jarvis/UNDERLOAD/Video'

def download_song():
    yt = None
    playlist = None
    url = str(input('URL: '))
    destination = str(input('PATH: '))
    try:
        yt = YouTube(url)
    except:
        playlist = Playlist(url)
    if yt:
        try:
            song = yt.streams.filter(only_audio=True).first()
            print('')
            if not(os.path.exists(destination)):
                if destination == 'i':
                    destination = internal_storage_music
                elif destination == 'e':
                    destination = external_storage_music
                else:
                    print('DIRECTORY INVALID --------> COPIED TO DEFAULT SONG DIRECTORY')
                    destination = internal_storage_music
            out_file = song.download(output_path = destination)
            #save as mp3
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            print(yt.title + " has been successfully downloaded.")
        except:
            print('CONNECTION ERROR')
    elif playlist:
        try:
            for i in range(len(playlist.videos)):
                yt = YouTube(playlist.video_urls[i])
                song = yt.streams.filter(only_audio=True).first()
                if not(os.path.exists(destination)):
                    print('DIRECTORY INVALID --------> COPIED TO DEFAULT SONG DIRECTORY')
                    destination = '/home/jarvis/Music'
                out_file = song.download(output_path = destination)
                #save as mp3
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
                print(yt.title + " has been successfully downloaded.") 
        except:
            print('CONNECTION ERROR') 

def download_video():
    quality = ['360p', '480p', '720p', '1080p', '1440p']
    yt, playlist = None, None
    url = str(input('URL: '))
    destination = str(input('PATH: '))
    try:
        yt = YouTube(url)
    except:
        playlist = Playlist(url)
    if not(os.path.exists(destination)):
        if destination == 'i':
            destination = internal_storage_video
        elif destination == 'e':
            destination = external_storage_video
        else:
            print('DIRECTORY INVALID --------> COPIED TO DEFAULT VIDEO DIRECTORY')
            destination = internal_storage_video
    try:
        quality_wanted = int(input('1.SD   2.HD    3.FHD : '))
        quality[quality_wanted]
    except:
        quality_wanted = 2
    if yt:
        yt.streams.filter(res=quality[quality_wanted]).first().download(destination)
        print(yt.title + " has been successfully downloaded.") 
    elif playlist:
        for i in range(len(playlist.videos)):  
            playlist.videos[i].streams.filter(res=quality[quality_wanted]).first().download(destination)
            print(playlist.videos[i].title + " has been successfully downloaded.")
    else:
        print('INVALID URL')

while run:
    option = input('DOWNLOAD SONG(s) / VIDEO(v)? ') 
    if option == 's':
        download_song()
    elif option == 'v':
        download_video()
    else:
        print('WRONG INPUT DETECTED!!!')
        run = False
    

