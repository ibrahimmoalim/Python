# Script for moving downloaded files to correct folders

import os
import shutil

# images
img = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.avif', '.svg')
# videos
vid = ('.webm', '.mov', '.mp4', '.m4p', '.m4v')
# audio
audio = ('.mp3', '.aac', '.aif', '.m4a', '.opus', '.wav', '.wma', '.ogg', '.au')
# documents
doc = ('.pdf', '.ppt', '.pptx', '.doc', '.docx', '.md', '.odt', '.odp',
       '.xls', '.xlsx', '.csv', '.ods', '.json')

def is_img(file):
    if os.path.splitext(file)[1] == '.svg':
        return 'svg'
    
    return os.path.splitext(file)[1] in img

def is_vid(file):
    return os.path.splitext(file)[1] in vid

def is_audio(file):
    return os.path.splitext(file)[1] in audio

def is_doc(file):
    return os.path.splitext(file)[1] in doc

downloads = os.listdir('/home/ibrahim/downloads/')
home = os.listdir('/home/ibrahim/')

for file in home:
    path = f'/home/ibrahim/{file}'

    if os.path.isfile(path):

        if is_img(file) == 'svg':
            shutil.move(path, '/home/ibrahim/pictures/icons/')
            print(f"{file} has been move to pictures/icons/")
        
        elif is_img(file):
            shutil.move(path, '/home/ibrahim/pictures/')
            print(f"{file} has been move to pictures/")
        
        elif is_vid(file):
            shutil.move(path, '/home/ibrahim/videos/')
            print(f"{file} has been move to videos/")
        
        elif is_audio(file):
            shutil.move(path, '/home/ibrahim/audio/')
            print(f"{file} has been move to audio/")
        
        elif is_doc(file):
            shutil.move(path, '/home/ibrahim/documents/')
            print(f"{file} has been move to documents/")