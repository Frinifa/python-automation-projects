import os

files = os.listdir()

count = 1

for file in files:
    new_name = "photo" + str(count) + ".jpg"
    os.rename(file, new_name)
    count += 1
