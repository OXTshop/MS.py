import time
import os
import  random
import yt_dlp as youtube_dl
from datetime import datetime
import shutil

print('Todos os links presentes no arquivo links.txt será\n baixado diretamente na pasta do script .py')
print('Começando em ...')
time.sleep(1)
print('> 1')
time.sleep(1)
print('> > 2')
time.sleep(1)
print('> > > 3')
time.sleep(1)
print(' Goooo Goooo\n')

f = open("links.txt", 'r')
banda = f.readlines()
ia = 0
ib = 0

"""if not os.path.exists('Musicas'):
    os.makedirs('Musicas')

for index in range(len(banda)):
       banda[index] = banda[index].rstrip('\n')
"""
numero = len(banda)
        
def run():
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    print('\n\033[1;36m] >>>', video_info['title'],'\033m\n')
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
        #shutil.move(f'{filename}', 'Musicas')

    print("\n\033[1;32m >>> Download complete... {}\033[m\n".format(filename))

if __name__=='__main__':
    print('\033[1;35m >>>>>> INICIADO <<<<<< \033')
    
for i in range(numero):
    time.sleep(1.5)
    ia = int(1) + ia
    ib = int(1) + ib

    if(ia == ib and ia != numero):
        video_url = banda[ia]
        print('\033[1;35m' ,video_url, '\033')

    else:
        exit()
    try:
        run()
    except UnicodeEncodeError:
        run()