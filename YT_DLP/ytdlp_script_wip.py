## Code by HyperGamesDev | https://hypergamesdev.github.io ##
## This script requires ffmpeg installed as well as obviously yt-dlp ##
## You can download yt-dlp on GitHub at: https://github.com/yt-dlp/ ##
## And FFMPEG at: https://ffmpeg.org/download.html ##

import subprocess
## Install yt-dlp if its not already installed
module_name = "yt_dlp"
subprocess.run(["pip", "install", module_name])

import sys, os
import yt_dlp

_type="mp4"
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

## For getting the filename
ydl_opts = {
    'quiet': True,
    'simulate': True,
    'outtmpl': output_directory + '/%(title)s.%(ext)s',
    'force_generic_extractor': True,
    'skip_download': True,
}

def get_video_filename(url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_title = info_dict.get('title', 'video')
    
    # Modify the filename to include an added ID for duplicates
    base_file_name = f"{video_title}.{_type}"
    file_name = base_file_name
    print(os.path.join(output_directory,file_name))
    exists_id = 1
    file_name = f"{base_file_name}_{exists_id}.{_type}"
    while os.path.exists(os.path.join(output_directory,file_name)):
        file_name = f"{base_file_name}_{exists_id}.{_type}"
        exists_id += 1

    return file_name

def download_file():
    global url
    while(url!=""):
        if(url=="-"):
            print(f"\n[{_type.upper()} DOWNLOAD]")
            print("The output directory is: ",output_directory)
            print(f"Input the url\n(if you want a section; follow the url by * and separate start from end by -\nso for example 'url'*01:03^01:37)")
            url=input(f"or type 'o' to open the directory, or press Enter without anything to stop the program:\n")
        if(url=="o"):
            os.startfile(output_directory)
            url="-"
        if(url!="" and url!="-" and url!="o"):
            print("\n")
            if("*" in url):
                _url=url.split("*")[0]
                _start=url.split("*")[1].split("-")[0]
                _end=url.split("*")[1].split("-")[1]
            else:
                _url=url

            # Modify the filename to include an added ID for duplicates
            file_name = get_video_filename(_url)
            
            ydl_opts = {
                'quiet': False,
                'simulate': False,
                'outtmpl': os.path.join(output_directory, file_name),
                'external_downloader': 'ffmpeg',
                'external_downloader_args': f"-ss {_start} -to {_end}"
            }


            ## Downloading with the right extension type
            if(_type=="mp3"):
                if("*" in url):
                    ydl_opts = {
                        '--audio-format': 'mp3',
                    }
                else:
                    subprocess.run(f"yt-dlp -x --audio-format mp3 {_url} -P {output_directory}")
            elif(_type=="m4a"):
                if("*" in url):
                    ydl_opts = {
                        '-f': 'm4a',
                    }
                else:
                    subprocess.run(f"yt-dlp -f m4a {_url} -P {output_directory}")
            elif(_type=="mp4"):
                if("*" in url):
                    ydl_opts = {
                        '-f': 'mp4',
                    }
                else:
                    pass
                    #subprocess.run(f"yt-dlp -f mp4 {_url} -P {output_directory}")
            if(url_set==False):   url="-"
            else:   url=""


            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([_url])

subprocess.run("yt-dlp -U")
download_file()
os.startfile(output_directory)