from pytube import YouTube, Playlist
import os


run = True
sd = '480'
hd = '720'
fhd = '1080'
internal_storage_music = '/home/jarvis/Music'
external_storage_music = '/media/jarvis/UNDERLOAD/Music'
internal_storage_video = '/home/jarvis/Videos'
external_storage_video = '/media/jarvis/UNDERLOAD/Video'
def download_song(option):
    if option == 's':
        try:
            yt = YouTube(str(input('URL: ')))
            song = yt.streams.filter(only_audio=True).first()
            destination = str(input('PATH: '))
            print('')
            if not(os.path.exists(destination)):
                if destination == 'i':
                    destination = internal_storage_music
                elif destination == 'e':
                    destination = external_storage_music
                else:
                    print('DIRECTORY INVALID \n')
                    print('COPIED TO DEFAULT SONG DIRECTORY \n')
                    destination = internal_storage_music
            song.download(output_path = destination)
            print(yt.title + " has been successfully downloaded.")
        except:
            print('CONNECTION ERROR') 
    elif option == 'p':
        try:
            playlist = Playlist(str(input('URL: ')))
            destination = str(input('PATH: '))
            for i in range(len(playlist.videos)):
                yt = YouTube(playlist.video_urls[i])
                song = yt.streams.filter(only_audio=True).first()
                if not(os.path.exists(destination)):
                    print('DIRECTORY INVALID \n')
                    print('COPIED TO DEFAULT SONG DIRECTORY \n')
                    destination = '/home/jarvis/Music'
                song.download(output_path = destination)
                print(yt.title + " has been successfully downloaded.") 
        except:
            print('CONNECTION ERROR') 


def download_video():
    yt = YouTube(str(input('URL: ')))
    destination = str(input('PATH: '))
    print('')
    if not(os.path.exists(destination)):
        if destination == 'i':
            destination = internal_storage_video
        elif destination == 'e':
            destination = external_storage_video
        else:
            print('DIRECTORY INVALID \n')
            print('COPIED TO DEFAULT SONG DIRECTORY \n')
            destination = internal_storage_music
        #quality = input('1.SD   2.HD    3.FHD : ')
        yt.streams.filter(res='720p').first().download(destination)
        print(yt.title + " has been successfully downloaded.") 

while run:
    option = input('DOWNLOAD SONG(s) / VIDEO(v)? ')
    if option == 's':
        option = input('PLAYLIST(p) / SINGLE(s)')
        if option == 's' or option == 'p':
            download_song(option)
        else:
            print('WRONG INPUT DETECTED!!')
        
    elif option == 'v':
        download_video()
    else:
        print('WRONG INPUT DETECTED!!!')
        run = False
    

