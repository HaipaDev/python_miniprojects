import subprocess
import os
output_directory = os.path.join(os.path.dirname(__file__), 'output', 'mp4')

print("The output directory is: ",output_directory)
url="-"
while(url=="-" and url!=""):
    url=input("[MP4 DOWNLOAD] Input the url: ")
    if(url!=""):
        subprocess.run(f"yt-dlp -f mp4 {url} -P {output_directory}")
        url="-"
#subprocess.Popen(r'explorer /select,"output\m4a\"')
#subprocess.Popen(['explorer', '/select', output_directory])
os.startfile(output_directory)