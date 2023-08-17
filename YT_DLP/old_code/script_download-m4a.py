import subprocess
import os
output_directory = os.path.join(os.path.dirname(__file__), 'output', 'm4a')

print("The output directory is: ",output_directory)
url="-"
while(url=="-" and url!=""):
    url=input("[M4A DOWNLOAD] Input the url: ")
    if(url!=""):
        subprocess.run(f"yt-dlp -f m4a {url} -P {output_directory}")
        url="-"
#subprocess.Popen(['explorer', '/select', output_directory])
os.startfile(output_directory)