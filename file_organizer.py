import os
import shutil

path = "."

files = os.listdir(path)

for file in files:
    
    if file.endswith(".jpg") or file.endswith(".png"):
        os.makedirs("Images", exist_ok=True)
        shutil.move(file, "Images/" + file)

    elif file.endswith(".pdf") or file.endswith(".txt"):
        os.makedirs("Documents", exist_ok=True)
        shutil.move(file, "Documents/" + file)

    elif file.endswith(".mp3"):
        os.makedirs("Audio", exist_ok=True)
        shutil.move(file, "Audio/" + file)

