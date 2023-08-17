## Code by HyperGamesDev | https://hypergamesdev.github.io ##
## This script requires ffmpeg installed as well as obviously yt-dlp ##
## You can download yt-dlp on GitHub at: https://github.com/yt-dlp/##
## And FFMPEG at: https://ffmpeg.org/download.html ##

import subprocess
import os
import sys

_type="m4a"
url="-"
url_set=False

if(__name__ == "__main__"):
    if(len(sys.argv) > 1):
        _type = sys.argv[1]
    if(len(sys.argv) > 2):
        if(sys.argv[2]!=""):
            url = sys.argv[2]
            url_set=True


output_directory = os.path.join(os.path.dirname(__file__), 'output', _type)

print("The output directory is: ",output_directory)
subprocess.run("yt-dlp -U")
while(url!=""):
    if(url=="-"):
        print(f"\n[{_type.upper()} DOWNLOAD]")
        print(f"Input the url\n(if you want a section - follow the url by * and separate start from end by ^\nso for example 'url'*01:03^01:37)")
        url=input(f"or type 'o' to open the directory, or press Enter without anything to stop the program: ")
    if(url=="o"):
        os.startfile(output_directory)
        url="-"
    if(url!="" and url!="-" and url!="o"):
        print("\n")
        if("*" in url):
            _url=url.split("*")[0]
            _start=url.split("*")[1].split("^")[0]
            _end=url.split("*")[1].split("^")[1]
        else:
            _url=url

        if(_type=="mp3"):
            if("*" in url):
                subprocess.run([
                    "yt-dlp", _url, "-P", output_directory,
                    "-x", "--audio-format", "mp3",
                    "--external-downloader", "ffmpeg",
                    "--external-downloader-args", f"-ss {_start} -to {_end}"
                ])
            else:
                subprocess.run(f"yt-dlp -x --audio-format mp3 {_url} -P {output_directory}")
        elif(_type=="m4a"):
            if("*" in url):
                subprocess.run([
                    "yt-dlp", _url, "-P", output_directory,
                    "-f", "m4a",
                    "--external-downloader", "ffmpeg",
                    "--external-downloader-args", f"-ss {_start} -to {_end}"
                ])
            else:
                subprocess.run(f"yt-dlp -f m4a {_url} -P {output_directory}")
        elif(_type=="mp4"):
            if("*" in url):
                subprocess.run([
                    "yt-dlp", _url, "-P", output_directory,
                    "-f", "mp4",
                    "--external-downloader", "ffmpeg",
                    "--external-downloader-args", f"-ss {_start} -to {_end}"
                ])
            else:
                subprocess.run(f"yt-dlp -f mp4 {_url} -P {output_directory}")
        if(url_set==False):   url="-"
        else:   url=""
os.startfile(output_directory)