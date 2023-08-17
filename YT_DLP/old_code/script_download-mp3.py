import subprocess
import os
output_directory = os.path.join(os.path.dirname(__file__), 'output', 'mp3')

print("The output directory is: ",output_directory)
url="-"
while(url=="-" and url!=""):
    url=input("[MP3 DOWNLOAD] Input the url: ")
    if(url!=""):
        #subprocess.run(f"ffmpeg -i input.m4a -c:a libmp3lame -q:a 8 output.mp3")
        subprocess.run(f"yt-dlp {url} -P {output_directory} -x --audio-format mp3")
        url="-"
#subprocess.Popen(['explorer', '/select', output_directory])
os.startfile(output_directory)

## This script requires ffmpeg installed ##