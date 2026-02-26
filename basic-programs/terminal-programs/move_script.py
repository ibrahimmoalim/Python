# Script for moving downloaded files to correct folders

import os
import shutil

BASE = "/home/ibrahim"
FOLDERS = [
    f"{BASE}",
    f"{BASE}/Downloads"
]

DESTINATIONS = {
    "images": f"{BASE}/pictures",
    "icons": f"{BASE}/pictures/icons",
    "videos": f"{BASE}/videos",
    "audio": f"{BASE}/audio",
    "documents": f"{BASE}/documents"
}

# images
img = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.avif', '.svg')
# videos
vid = ('.webm', '.mov', '.mp4', '.m4p', '.m4v')
# audio
audio = ('.mp3', '.aac', '.aif', '.m4a', '.opus', '.wav', '.wma', '.ogg', '.au')
# documents
doc = ('.pdf', '.ppt', '.pptx', '.doc', '.docx', '.md', '.odt', '.odp',
       '.xls', '.xlsx', '.csv', '.ods', '.json')

def move_file(path, destination):
    try:
        shutil.move(path, destination)
        print(f"Moved {os.path.basename(path)} → {destination}")
    except shutil.Error as e:
        print(e)


for folder in FOLDERS:
    if not os.path.exists(folder):
        continue

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if not os.path.isfile(path):
            continue

        ext = os.path.splitext(file)[1].lower()

        if ext == ".svg":
            move_file(path, DESTINATIONS["icons"])
        elif ext in img:
            move_file(path, DESTINATIONS["images"])
        elif ext in vid:
            move_file(path, DESTINATIONS["videos"])
        elif ext in audio:
            move_file(path, DESTINATIONS["audio"])
        elif ext in doc:
            move_file(path, DESTINATIONS["documents"])