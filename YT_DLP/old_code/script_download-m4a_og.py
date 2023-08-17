import subprocess

url=input("[M4A DOWNLOAD] Input the url")
subprocess.run(f"yt-dlp -f m4a {url}")