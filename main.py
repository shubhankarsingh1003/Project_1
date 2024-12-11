import os

files = os.listdir("png_file")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"png_file/{file}",f"png_file/{i}.png")
        
        i = i+1
print(files)